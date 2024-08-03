# Games

This repository contains several small games implemented in different programming languages. Each game is stored in its own directory. Below is a brief description of each game and instructions on how to run them.

## Games Overview

### 1. BlackJack (Python)
A simple implementation of the BlackJack card game.

**Files:**
- `art.py`
- `main.py`

**How to run:**
```sh
python main.py
```

### 2. Guess the Number (C)
A number guessing game where the player tries to guess a randomly generated number.

**Files:**
- `Guess_the_number.c`

**How to compile and run:**
```sh
gcc Guess_the_number.c -o Guess_the_number
./Guess_the_number
```

### 3. Matchstick Game (C)
A game where players take turns removing matchsticks. There are fair and unfair versions.

**Files:**
- `Matchstick_game.c`
- `Matchstick_game_unfair.c`

**How to compile and run:**
```sh
# Fair version
gcc Matchstick_game.c -o Matchstick_game
./Matchstick_game

# Unfair version
gcc Matchstick_game_unfair.c -o Matchstick_game_unfair
./Matchstick_game_unfair
```

### 4. Ping Pong (Python)
A classic ping pong game with paddle and ball. The speed of the paddle increases each time the player hits the ball, adding an extra layer of challenge and excitement.

**Files:**
- `ball.py`
- `main.py`
- `paddle.py`
- `scoreboard.py`

**How to run:**
```sh
python main.py
```

### 5. Snake Game (Python)
The classic snake game where the player controls a snake to eat food and grow.

**Files:**
- `food.py`
- `main.py`
- `scoreboard.py`
- `snake.py`

**How to run:**
```sh
python main.py
```

### 6. Stone Paper Scissor (C)
A command-line version of the classic stone-paper-scissor game with fair and unfair versions.

**Files:**
- `Stone_paper_scissor.c`
- `Stone_paper_scissor_unfair.c`

**How to compile and run:**
```sh
# Fair version
gcc Stone_paper_scissor.c -o Stone_paper_scissor
./Stone_paper_scissor

# Unfair version
gcc Stone_paper_scissor_unfair.c -o Stone_paper_scissor_unfair
./Stone_paper_scissor_unfair
```

### 7. Turtle Crossing Game (Python)
A game where the player controls a turtle to cross a road filled with moving cars.

**Files:**
- `cars.py`
- `main.py`
- `player.py`
- `scoreboard.py`

**How to run:**
```sh
python main.py
```

### 8. US States Game (Python)
A game to identify US states on a map.

**Files:**
- `50_states.csv`
- `blank_states_img.gif`
- `main.py`

**How to run:**
```sh
python main.py
```

## Contributing

Feel free to fork this repository, make improvements, and create pull requests. All contributions are welcome!
