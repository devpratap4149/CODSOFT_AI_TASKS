# Task 2: Tic-Tac-Toe AI

This project was developed as part of the **CodSoft Artificial Intelligence Internship**.

## Project Overview

This project is a Tic-Tac-Toe game where a human player plays against an AI opponent.

The player uses `X`, while the AI uses `O`. The AI uses the Minimax algorithm to check possible future moves and choose the best move.

## Features

- Human vs AI gameplay
- AI uses the Minimax algorithm
- AI checks possible future moves
- Prevents invalid and repeated moves
- Detects wins and draws
- Simple command-line interface
- AI is designed to be unbeatable

## Technologies Used

- Python
- Minimax Algorithm
- Game Theory
- Recursion
- Conditional Statements

## Installation

No external library is required.

Make sure Python is installed on your system.

## How to Run

Open the terminal inside the Task 2 folder and run:

```bash
python tic_tac_toe.py
```

## Position Guide

Use the following numbers to select a position:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

The player uses `X`, and the computer uses `O`.

## How It Works

The Minimax algorithm checks all possible future game states.

It gives scores to the possible results:

```text
AI wins     = 1
Draw        = 0
Player wins = -1
```

The AI chooses the move with the highest score.

## Project Structure

```text
Task_2
│
├── tic_tac_toe.py
├── README.md
└── screenshot.png
```


## Learning Outcomes

- Learned how the Minimax algorithm works
- Understood basic game theory
- Learned how recursion checks future moves
- Learned how to handle player input
- Learned how to detect wins and draws

## Future Improvements

- Add a graphical user interface
- Add difficulty levels
- Add a restart option
- Add a score counter
- Create a web-based version

## Author

**Dev Pratap Singh**