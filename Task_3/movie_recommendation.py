import difflib

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Movie names with their genres and important keywords
movie_data = {
    "movie_name": [
        "3 Idiots",
        "Taare Zameen Par",
        "Dangal",
        "Chhichhore",
        "Super 30",
        "PK",
        "Lagaan",
        "Swades",
        "Zindagi Na Milegi Dobara",
        "Yeh Jawaani Hai Deewani",
        "Dil Chahta Hai",
        "Bajrangi Bhaijaan",
        "Drishyam",
        "Andhadhun",
        "Kahaani",
        "Shershaah",
        "Raazi",
        "Uri The Surgical Strike",
        "Krrish",
        "Robot"
    ],

    "movie_details": [
        "comedy drama education friendship college",
        "drama education child family school",
        "sports drama biography wrestling family",
        "comedy drama friendship college motivation",
        "biography drama education mathematics motivation",
        "comedy drama science religion social",
        "sports drama history cricket village",
        "drama social village development patriotism",
        "adventure comedy drama friendship travel",
        "romance comedy drama friendship travel",
        "comedy drama friendship romance",
        "drama family adventure emotional",
        "crime thriller mystery family",
        "crime thriller mystery comedy music",
        "crime thriller mystery drama",
        "war biography drama patriotism",
        "spy thriller drama patriotism",
        "action war drama patriotism",
        "action science fiction superhero adventure",
        "science fiction action robot technology"
    ]
}


# Convert the dictionary into a table
movies = pd.DataFrame(movie_data)


# Convert movie descriptions into numerical values
vectorizer = TfidfVectorizer()

movie_vectors = vectorizer.fit_transform(
    movies["movie_details"]
)


# Compare all movies with each other
similarity_scores = cosine_similarity(movie_vectors)


def show_movie_list():
    print("\nAvailable Movies:\n")

    for number, movie_name in enumerate(
        movies["movie_name"],
        start=1
    ):
        print(f"{number}. {movie_name}")


def recommend_movies(user_movie):
    available_movies = movies["movie_name"].tolist()

    # Find the closest movie name
    matching_movies = difflib.get_close_matches(
        user_movie,
        available_movies,
        n=1,
        cutoff=0.4
    )

    if not matching_movies:
        print("\nSorry, this movie was not found.")
        print("Please choose a movie from the available list.")
        return

    selected_movie = matching_movies[0]

    # Find the row number of the selected movie
    selected_movie_index = movies[
        movies["movie_name"] == selected_movie
    ].index[0]

    # Get similarity scores for the selected movie
    movie_scores = list(
        enumerate(
            similarity_scores[selected_movie_index]
        )
    )

    # Arrange movies from most similar to least similar
    sorted_movies = sorted(
        movie_scores,
        key=lambda movie: movie[1],
        reverse=True
    )

    print(
        f"\nMovies similar to {selected_movie}:\n"
    )

    recommendation_number = 1

    for movie_index, score in sorted_movies:
        recommended_movie = movies.iloc[
            movie_index
        ]["movie_name"]

        # Do not recommend the same movie
        if recommended_movie == selected_movie:
            continue

        print(
            f"{recommendation_number}. "
            f"{recommended_movie}"
        )

        recommendation_number += 1

        # Stop after showing 5 movies
        if recommendation_number > 5:
            break


print("=" * 50)
print("       CODSOFT MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

show_movie_list()


while True:
    print("\nType 'exit' to close the program.")

    user_choice = input(
        "Enter the name of a movie you like: "
    ).strip()

    if user_choice.lower() in [
        "exit",
        "quit",
        "stop"
    ]:
        print("Recommendation system closed.")
        break

    recommend_movies(user_choice)