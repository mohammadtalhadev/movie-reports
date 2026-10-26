import math

from models import Movie, ReportResults

MAX_CIRCLES = 80
TOP_COUNT = 10


class ReportCalculator:
    def year_results(self, movies: list[Movie], year: int) -> ReportResults:
        year_movies = [m for m in movies if m.start_year == year]
        if not year_movies:
            return ReportResults(year=year)

        highest = max(year_movies, key=lambda m: m.rating)
        lowest = min(year_movies, key=lambda m: m.rating)


        runtimes = [m.runtime_minutes for m in year_movies
                    if m.runtime_minutes is not None]
        average = sum(runtimes) / len(runtimes) if runtimes else 0.0

        return ReportResults(year=year, highest_movie=highest,
                             lowest_movie=lowest, average_runtime=average)

    def genre_results(self, movies: list[Movie], genre: str) -> ReportResults:
        wanted = genre.lower()
        genre_movies = [m for m in movies
                        if wanted in (g.lower() for g in m.genres)]
        if not genre_movies:
            return ReportResults(genre=genre)

        count = len(genre_movies)
        average = sum(m.rating for m in genre_movies) / count
        return ReportResults(genre=genre, genre_movie_count=count,
                             genre_average_rating=average)

    def top_ten_results(self, movies: list[Movie],
                        year: int) -> ReportResults:
        year_movies = [m for m in movies if m.start_year == year]
        if not year_movies:
            return ReportResults(top_year=year)

        ranked = sorted(year_movies,
                        key=lambda m: (m.num_votes, m.rating),
                        reverse=True)
        top_movies = ranked[:TOP_COUNT]
        vote_weight = max(1, math.ceil(
            top_movies[0].num_votes / MAX_CIRCLES))
        return ReportResults(top_year=year, top_movies=top_movies,
                             vote_weight=vote_weight)


class ReportGenerator:
    def print_year_report(self, results: ReportResults) -> None:
        if results.highest_movie is None or results.lowest_movie is None:
            print(f"No movies found for year {results.year}")
            return
        print(f"Highest rating: {results.highest_movie.rating} - "
              f"{results.highest_movie.original_title}")
        print(f"Lowest rating: {results.lowest_movie.rating} - "
              f"{results.lowest_movie.original_title}")
        print(f"Average mean minutes: {results.average_runtime:.1f}")

    def print_genre_report(self, results: ReportResults) -> None:
        if results.genre_movie_count == 0:
            print(f"No movies found for genre {results.genre}")
            return
        print(f"Movies found: {results.genre_movie_count}")
        print(f"Average mean rating: {results.genre_average_rating:.1f}")

    def print_top_ten_report(self, results: ReportResults) -> None:
        if not results.top_movies:
            print(f"No movies found for year {results.top_year}")
            return
        for movie in results.top_movies:
            circles = round(movie.num_votes / results.vote_weight)
            print(f"{movie.original_title}  "
                  f"{' '.join('●' * circles)} {movie.num_votes}")
