# Aditya-Anand
python project
# 🐦 Flappy Bird Clone

A simple Flappy Bird-style game developed using **Python 3 and Pygame** as part of **Project Series (PS No. 61)**.

The player controls a bird that continuously falls due to gravity and must flap upward to navigate through gaps between pipes. The objective is to avoid obstacles and achieve the highest possible score.

---

## 📌 Project Information

| Detail               | Description                                     |
| -------------------- | ----------------------------------------------- |
| Project Number       | PS No. 61                                       |
| Project Name         | Flappy Bird Clone                               |
| Programming Language | Python 3                                        |
| Game Library         | Pygame                                          |
| Concepts Used        | Gravity, Collision Detection, Game Loop, Events |
| Project Type         | 2D Game Development                             |

## 🎮 Features

- Bird movement controlled using the SPACE key.
- Gravity-based falling movement.
- Flapping mechanism to move the bird upward.
- Randomly generated pipes with gaps.
- Pipes move from right to left.
- Score increases when the bird passes a pipe.
- Collision detection with pipes, ground, and top boundary.
- Game Over screen when the bird collides.
- Restart functionality.
- Real-time score display.

## 🛠️ Technologies Used

- Python 3
- Pygame
- Object-Oriented Programming
- Random module

## 📋 Requirements

- Python 3
- Pygame-compatible installation
- Windows, Linux, or macOS

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/adityanand-CMD/flappy-bird-clone.git
```

### 2. Navigate to the project directory

```bash
cd flappy-bird-clone
```

### 3. Install Pygame

```bash
python -m pip install pygame-ce
```

> Pygame Community Edition (pygame-ce) is an alternative Pygame-compatible package. The source code continues to use `import pygame`.

### 4. Run the game

```bash
python one.py
```

## 🕹️ Game Controls

| Key   | Action                  |
| ----- | ----------------------- |
| SPACE | Flap upward             |
| R     | Restart after Game Over |
| ESC   | Exit the game           |

## ⚙️ Game Specifications

| Parameter              | Value            |
| ---------------------- | ---------------- |
| Window Size            | 400 × 600 pixels |
| Bird Size              | 30 × 30 pixels   |
| Bird Starting Position | x = 100, y = 300 |
| Initial Velocity       | 0                |
| Gravity                | +1 per frame     |
| Flap Velocity          | −10              |
| Pipe Width             | 60 pixels        |
| Pipe Gap               | 150 pixels       |
| Ground Boundary        | y = 600          |

### Physics Logic

Gravity is applied to the bird every frame:

```python
velocity += 1
y += velocity
```

When the player presses SPACE:

```python
velocity = -10
```

The bird moves upward when its velocity is negative and falls downward when its velocity becomes positive.

## 🧪 Test Cases

The project follows the four test cases specified in the assignment.

| Test Case   | Scenario                 | Expected Result                                                        |
| ----------- | ------------------------ | ---------------------------------------------------------------------- |
| Test Case 1 | Normal Input             | Bird position updates according to gravity                             |
| Test Case 2 | Boundary / Minimum Input | Ground and top boundary collisions trigger Game Over                   |
| Test Case 3 | Invalid Input            | Invalid key is ignored                                                 |
| Test Case 4 | Different Valid Scenario | Flapping updates velocity correctly and passing a pipe increases score |

Detailed test cases and expected outputs are documented separately in the project test case PDF.

## 📂 Project Structure

```text
flappy-bird-clone/
│
├── flappy_bird.py
├── README.md
├── PS61_Flappy_Bird_Test_Cases_Sequential.pdf
└── requirements.txt
```

## 📚 Concepts Learned

- Python programming fundamentals
- Game development using Pygame
- Event handling and keyboard input
- Game loop implementation
- Gravity and velocity simulation
- Collision detection using `Rect.colliderect()`
- Object-oriented programming
- Score tracking and game state management

## 🔮 Future Improvements

- Add sound effects and background music.
- Add difficulty levels.
- Implement a high-score system.
- Improve bird and pipe graphics.
- Add animations and a start menu.
- Add mobile-style touch controls.

## 👨‍💻 Author

**Your Name**

Python Developer | Student Project

GitHub: [Aditya Anand](https://github.com/adityanand-CMD)

## 📄 License

This project is developed for educational purposes.

You are welcome to explore, modify, and improve the source code for learning and personal use.

---

⭐ If you find this project useful, consider giving the repository a star!
