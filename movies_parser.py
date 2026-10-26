import argparse
import os
import sys

from parser import MovieCsvParser
from reports import ReportCalculator, ReportGenerator

ENV_FILE_PATH = "MOVIES_CSV_PATH"
MIN_YEAR = 1800
MAX_YEAR = 2100


def year_type(value: str) -> int:
    try:
        year = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid year")
    if not MIN_YEAR <= year <= MAX_YEAR:
        raise argparse.ArgumentTypeError(
            f"year must be between {MIN_YEAR} and {MAX_YEAR}")
    return year


def genre_type(value: str) -> str:
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("genre must not be empty")
    return value


def build_argument_parser() -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(
        usage="movies_parser.py [-r YEAR] [-g GENRE] [-y YEAR]")
    arg_parser.add_argument(
        "-r", dest="year_reports", type=year_type, action="append",
        metavar="YEAR")
    arg_parser.add_argument(
        "-g", dest="genre_reports", type=genre_type, action="append",
        metavar="GENRE")
    arg_parser.add_argument(
        "-y", dest="top_reports", type=year_type, action="append",
        metavar="YEAR")
    return arg_parser


def get_file_path(arg_parser: argparse.ArgumentParser) -> str:
    file_path = os.environ.get(ENV_FILE_PATH)
    if not file_path:
        arg_parser.error(
            f"environment variable {ENV_FILE_PATH} is not set")
    if not os.path.isfile(file_path):
        arg_parser.error(f"file not found: {file_path}")
    return file_path


def main() -> None:
    arg_parser = build_argument_parser()
    args = arg_parser.parse_args()

    if not (args.year_reports or args.genre_reports or args.top_reports):
        arg_parser.error("specify at least one report: -r, -g or -y")

    file_path = get_file_path(arg_parser)
    movies = MovieCsvParser().load(file_path)

    calculator = ReportCalculator()
    generator = ReportGenerator()
    blocks = []

    for year in args.year_reports or []:
        blocks.append((generator.print_year_report,
                       calculator.year_results(movies, year)))
    for genre in args.genre_reports or []:
        blocks.append((generator.print_genre_report,
                       calculator.genre_results(movies, genre)))
    for year in args.top_reports or []:
        blocks.append((generator.print_top_ten_report,
                       calculator.top_ten_results(movies, year)))

    for index, (printer, results) in enumerate(blocks):
        if index:
            print()
        printer(results)


if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        sys.exit(f"Error reading file: {error}")
