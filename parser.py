import csv

from models import Movie

NULL_VALUE = "\\N"


class MovieCsvParser:
    def load(self, file_path: str) -> list[Movie]:
        movies = []
        with open(file_path, encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie = self._parse_row(row)
                if movie is not None:
                    movies.append(movie)
        return movies

    def _parse_row(self, row: dict[str, str]) -> Movie | None:
        try:
            runtime = row["runtimeMinutes"]
            genres = row["genres"]
            return Movie(
                id=row["id"],
                title_type=row["titleType"],
                original_title=row["originalTitle"],
                start_year=int(row["startYear"]),
                runtime_minutes=None if runtime == NULL_VALUE
                else int(runtime),
                genres=[] if genres == NULL_VALUE else genres.split(","),
                rating=float(row["rating"]),
                num_votes=int(row["numVotes"]),
            )
        except (KeyError, ValueError):
            return None
