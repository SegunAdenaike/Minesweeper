# Minesweeper Grid Solver

This program solves a Minesweeper grid by counting the number of adjacent mines for each spot in the grid. It takes a grid as input, where mines are represented by "#" and empty spots are represented by "-". The program returns a new grid with the count of adjacent mines for each spot.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation

To use this program locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/SegunAdenaike/Minesweeper.git
   ```

2. Change to the project directory:

   ```shell
   cd minesweeper
   ```

3. Run the program:

   ```shell
   python minesweeper.py
   ```

## Usage

1. Open the `minesweeper.py` file.

2. Modify the `test` variable to represent your Minesweeper grid. Use "#" to denote mines and "-" for empty spots.

   ```python
   test = [
       ["-", "-", "-", "#", "#"],
       ["-", "#", "-", "-", "-"],
       ["-", "-", "#", "-", "-"],
       ["-", "#", "#", "-", "-"],
       ["-", "-", "-", "-", "-"]
   ]
   ```

3. Save the file and run it:

   ```shell
   python minesweeper.py
   ```

4. The program will generate a new grid with the count of adjacent mines for each spot.

   ```
   - - - # #
   1 # 2 1 1
   1 3 # 2 0
   2 # # 2 0
   1 2 2 1 0
   ```

5. Use the result to play or analyze the Minesweeper grid.

## Credits

This program was created by [Olusegun Adenaike](https://github.com/SegunAdenaike).

If you have any questions or suggestions, please feel free to contact me.
