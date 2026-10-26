from dataclasses import dataclass, field


@dataclass
class Movie:
    id: str
    title_type: str
    original_title: str
    start_year: int
    runtime_minutes: int | None
    genres: list[str]
    rating: float
    num_votes: int


@dataclass
class ReportResults:
    year: int | None = None
    highest_movie: Movie | None = None
    lowest_movie: Movie | None = None
    average_runtime: float = 0.0


    genre: str | None = None
    genre_movie_count: int = 0
    genre_average_rating: float = 0.0


    top_year: int | None = None
    top_movies: list[Movie] = field(default_factory=list)
    vote_weight: int = 0
