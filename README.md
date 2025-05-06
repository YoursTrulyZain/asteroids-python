# Asteroids Python

![Asteroids Game](https://img.shields.io/badge/Game-Asteroids-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-red)

A classic Asteroids arcade game recreated in Python using the Pygame library.

## 🚀 Game Overview

In this recreation of the iconic arcade game, you control a spaceship navigating through an asteroid field. Your mission is to survive as long as possible by avoiding or destroying incoming asteroids.

## ✨ Features

- **Spaceship Controls**: Navigate with WASD keys

  - `W` - Thrust forward
  - `S` - Reverse
  - `A` - Rotate counter-clockwise
  - `D` - Rotate clockwise
  - `SPACE` - Fire weapons

- **Asteroid Mechanics**:

  - Asteroids spawn randomly from the edges of the screen
  - Larger asteroids split into smaller ones when shot
  - Various asteroid sizes with different point values

- **Physics System**:
  - Vector-based movement
  - Collision detection for player-asteroid and shot-asteroid interactions

## 🎮 How to Play

1. Avoid colliding with asteroids
2. Shoot asteroids to destroy them and score points
3. Larger asteroids split into smaller ones when shot
4. Game ends when your ship collides with an asteroid

## 🖥️ Installation & Running

### Prerequisites

- Python 3.x
- Pygame 2.6.1

### Setup

1. Clone this repository:

```
git clone https://github.com/YoursTrulyZain/asteroids-python.git
cd asteroids-python
```

2. Set up a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the game:

```
python main.py
```

## 🏗️ Project Structure

- `main.py` - Game initialization and main loop
- `player.py` - Player ship controls and rendering
- `asteroid.py` - Asteroid behavior and splitting mechanics
- `asteroidfield.py` - Manages asteroid spawning
- `shot.py` - Player projectile handling
- `circleshape.py` - Base class for circular game entities
- `constants.py` - Game configuration constants

## 🎯 Future Features I May Add

- Score tracking
- Multiple lives
- Power-ups and special weapons
- Level progression
- High score leaderboard
