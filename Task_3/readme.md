# Task 3: Movie Recommendation System

This project was developed as part of the **CodSoft Artificial Intelligence Internship**.

## Project Overview

This is a content-based movie recommendation system built using Python.

The user enters the name of a movie, and the system recommends similar movies based on genres, themes, and descriptive keywords.

## Features

- Recommends similar movies
- Uses content-based filtering
- Handles small spelling mistakes
- Displays five movie recommendations
- Provides a simple command-line interface

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Difflib

## Installation

Install the required libraries using:

```bash
python -m pip install pandas scikit-learn
```

## How to Run

Open the terminal inside the project folder and run:

```bash
python movie_recommendation.py
```

Enter the name of a movie from the available list.

Example:

```text
Enter the name of a movie you like: Krrish
```

The system will display five similar movie recommendations.

## How It Works

The system stores movie names along with genres and descriptive keywords.

TF-IDF Vectorizer converts the movie descriptions into numerical values.

Cosine Similarity compares the selected movie with all other movies and finds the most similar ones.

The `difflib` module helps match movie names even when the user makes a small spelling mistake.

## Project Structure

```text
TASK_4_RECOMMENDATION_SYSTEM
│
├── movie_recommendation.py
├── README.md
└── screenshot.png
```

## Output

The program displays:

- A list of available movies
- The matched movie name
- Five similar movie recommendations


## Learning Outcomes

- Learned how recommendation systems work
- Understood content-based filtering
- Learned how TF-IDF converts text into numerical form
- Learned how Cosine Similarity compares items
- Learned how to use Pandas and Scikit-learn

## Future Improvements

- Add a graphical user interface
- Use a larger movie dataset
- Add movie ratings, posters, and release years
- Build a web-based recommendation system
- Add personalized user recommendations

## Author

**Dev Pratap Singh**