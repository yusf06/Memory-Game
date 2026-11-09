# Memory Game

A Simon-style memory game built with Python and Tkinter. Watch the sequence of colored buttons flash, then repeat it from memory. Each round adds one more color and the game gets faster.

## Screenshots

| Start screen | Sequence playing | Your turn |
|:---:|:---:|:---:|
| ![Start screen](screenshot1.png) | ![Sequence playing](screenshot2.png) | ![Your turn](screenshot3.png) |

> Rename the image files above to match the screenshots in your main directory.

## Features

- 4 colored buttons: red, blue, green and yellow
- Each color has its own sound (400 Hz to 700 Hz)
- The game starts with a sequence of 4 colors
- One new color is added every round
- The same color never appears twice in a row
- The sequence speeds up each round (down to a minimum speed)
- High score tracking, shown at the top right of the window
- Clear status messages: memorize, your turn, correct, game over

## Requirements

- **Windows** (the game uses the `winsound` module, which only exists on Windows)
- **Python 3.6 or newer**
- No extra packages needed: `tkinter`, `random`, `time`, `winsound` and `threading` all come with Python

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/memory-game.git
   cd memory-game
   ```
2. Make sure Python is installed:
   ```bash
   python --version
   ```

## How to Run

```bash
python memory_game.py
```

(Replace `memory_game.py` with the name of your file.)

## Generate the .exe File

You can turn the game into a standalone Windows executable with [PyInstaller](https://pyinstaller.org), so it runs without Python installed.

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --name MemoryGame memory_game.py
   ```
   - `--onefile` creates a single `.exe` file
   - `--windowed` hides the console window (the game only uses a Tkinter window)
   - `--name MemoryGame` sets the name of the executable
3. Find your game in the `dist` folder:
   ```
   dist/MemoryGame.exe
   ```

Optional: add a custom icon with `--icon=icon.ico`.

The `build` folder, the `dist` folder and the `.spec` file are created automatically. You can delete the `build` folder and the `.spec` file after building, and you can add `build/` and `dist/` to your `.gitignore`.

## How to Play

1. Click **Start Game**.
2. Watch the buttons flash and listen to the sounds. Memorize the order.
3. When the message says **"Your turn!"**, click the buttons in the same order.
4. If you are correct, a new color is added and the next round begins.
5. If you click a wrong color, the game is over. Your round number is displayed.
6. Click **Start Game** again to play another game and try to beat your high score.

## How It Works

| Function | Description |
|----------|-------------|
| `start_game()` | Resets the game and creates the first 4-color sequence |
| `next_round()` | Adds a new color and starts the next round |
| `play_sequence()` | Plays the sequence with flashes and sounds, faster each round |
| `flash_button()` | Flashes a button and plays its sound |
| `check_user_input()` | Checks each click against the sequence |
| `update_high_score()` | Updates the high score label |

The sequence is played in a separate thread so the window does not freeze.

## Possible Improvements

- Save the high score to a file so it is kept between sessions
- Add difficulty levels
- Make it cross-platform by replacing `winsound`
- Add a restart button after game over

## Author

Made by Youssef.
