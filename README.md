# Pacman Clone

![Game gif](assets/demo/demo.gif)
*Example of the game in action.*

## Overview

Welcome to the **Pacman Clone**! This is a Python-based recreation of the classic Pacman game, built using the Pygame library. Navigate Pacman through intricate mazes, collect all the berries, and evade colorful ghosts to achieve the highest score possible. Whether you're a fan of retro games or looking to create your own custom levels, this project offers both nostalgic gameplay and flexibility for customization.

## Features

- **Classic Gameplay:** Experience the timeless Pacman mechanics with mazes, berries, and ghost adversaries.
- **Multiple Ghosts:** Four distinct ghosts (Red, Pink, Orange, Skyblue) each with unique behaviors.
- **Scoring System:** Collect regular and power-up berries to boost your score and gain temporary invincibility.
- **Lives and Levels:** Start with multiple lives and advance through increasingly challenging levels.
- **Custom Level Creation:** Design your own mazes using simple text files, allowing endless gameplay variations.

## Installation

### Prerequisites

- **Python 3.12+**: Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).
- **Pygame 2.6.1**: The game relies on the Pygame library for graphics and input handling.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/nikitosikvn1/pacman.git
   cd pacman/
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

After completing the installation steps:

```bash
python main.py
```

### Game Controls

- **Arrow Keys**: Navigate Pacman Up, Down, Left, and Right.
- **R Key**: Restart the game after a game over.

## Creating Custom Levels

One of the standout features of this Pacman Clone is the ability to create your own custom levels using simple text files. Follow these steps to design and implement your own mazes:

### Step 1: Understand the Maze Format

The game uses a text-based maze representation where each character corresponds to a specific cell type:

- **`1`**: Wall
- **`B`**: Big Dot (Power-up Berry)
- **`P`**: Pacman's Starting Position
- **`r`**: Red Ghost Starting Position
- **`p`**: Pink Ghost Starting Position
- **`o`**: Orange Ghost Starting Position
- **`s`**: Skyblue Ghost Starting Position
- **Space (` `)**: Empty Path (Regular Berry)

### Step 2: Create Your Maze File

1. Navigate to the `assets/levels/` directory.
2. Create a new text file, e.g., `my_custom_maze.txt`.
3. Design your maze using the characters mentioned above. Ensure that all lines have the same length for consistency.

**Simple example:**

```txt
1111111111111
1P    1    r1
1 B1111B11111
1     1    p1
1111B1B1B1111
1     1    o1
1 s         1
1111111111111
```

### Step 3: Launch the Game with Your Custom Maze

Use the `--maze` argument to specify your custom maze file when running the game.

```bash
python main.py --maze assets/levels/my_custom_maze.txt
```

### Tips for Designing Mazes

- **Symmetry:** Classic Pacman mazes are often symmetric. Feel free to experiment with asymmetrical designs for varied gameplay.
- **Ghost Placement:** Ensure ghosts have clear paths to navigate to make the game challenging.
- **Berries Distribution:** Balance regular and big dots to manage game difficulty and scoring.
- **Testing:** Regularly test your maze to ensure there are no dead-ends or unreachable areas unless intended.
