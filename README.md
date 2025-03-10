
# Rubik's Cube Simulator 🎲

This project is a Rubik's Cube simulator that allows users to execute various moves on a virtual cube. It provides a text-based interface for performing and viewing cube rotations, helping users practice and understand cube notations and algorithms. The simulator supports standard cube moves and displays the cube's state in real-time.

## Features

- **Cube Simulation**: Implements a virtual 3x3 Rubik's Cube with six colored faces represented using Unicode characters.
- **Move Execution**: Supports standard cube notations (U, L, F, R, B, D) with variations like counter-clockwise (') and double moves (2).
- **Real-Time Display**: Updates and prints the cube's state after each move, allowing users to track progress.
- **Scramble Support**: Accepts a list of moves during initialization to simulate a scrambled cube.
- **Input Validation**: Ensures that only valid move notations are accepted, enhancing user experience.
- **Debug Mode**: Allows step-by-step visualization of moves with a delay for analysis.
- **Extensibility**: Modular design enables easy addition of new features or move types.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/rubiks-cube-simulator.git
    ```

## Usage

1. Navigate to the project folder:
    ```bash
    cd rubiks-cube-simulator
    ```
2. Run the script:
    ```bash
    python rubiks_cube_sim.py
    ```
3. Enter a move when prompted (e.g., `U`, `L'`, `F2`). Type `X` to exit.
4. The simulator will display the cube's state after each move.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to **Ernő Rubik** for inventing the iconic Rubik's Cube and inspiring countless puzzle enthusiasts worldwide.
- Inspired by the official Rubik's Cube notations and solving techniques.
