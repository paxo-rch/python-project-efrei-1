# Fort Boyard: The Game

## 1. General Presentation

### Project Title

Fort Boyard: The Game

### Contributors

*   **Gabriel:** Developer (Logical Challenges, Chance Challenges, GUI, the Pere Fouras Challenge)
*   **Jules:** Developer (Math Challenges, Final Challenge, Utility Functions, the Pere Fouras Challenge, No-GUI part)

### Description

This project is a text-based and GUI-based adventure game inspired by the French TV show "Fort Boyard." Players navigate through a series of challenges to collect keys and ultimately reach the treasure room. The game features a variety of mini-games, including mathematical problems, logical puzzles, chance-based games and riddles, designed to test the player's skills and luck.

### Key Features

*   **Variety of Challenges:** The game offers a diverse set of challenges:
    *   **Math Challenges:** Factorial calculations, linear equation solving, prime number identification, and math roulette.
    *   **Logical Challenges:**  A strategic Nim game (against a "master" AI) and Tic Tac Toe.
    *   **Chance Challenges:** A shell game and a dice-rolling game.
    *   **Pere Fouras Challenge**: A riddle challenge where you have to find the answer based on a question.
    *   **Final Challenge:** A word-guessing game based on clues.
*   **GUI-based and No-GUI based Interface:** Most challenges offer both a console-based and a graphical user interface (GUI) version using Pygame.
*   **Multiplayer Support:** The game supports 1 to 3 players.
*   **Progress Tracking:** The game keeps track of the number of keys each player has collected.
*   **Dynamic Gameplay:**  Random elements in challenges ensure replayability.
*   **Introduction and Storytelling:** Engaging text-based introduction and progress updates.

### Technologies Used

*   **Programming Language:** Python
*   **Libraries:**
    *   `pygame`: For graphics, user interface, video and event handling.
    *   `random`: For generating random numbers and choices.
    *   `json`: For loading riddles and clues from JSON files.
    *   `time`: For managing time-related events and animations.
    *   `math`: For mathematical calculations.
    *   `pygamevideo`: To play videos.
*   **Tools:**
    *   Git (for version control)

### Installation

1. **Clone the Git Repository:**

    ```bash
    git clone <repository_url>
    ```

    Replace `<repository_url>` with the actual URL of your project's Git repository.
2. **Set up the Development Environment:**

    *   **Python:** Ensure you have Python 3.x installed.
    *   **Pygame:** Install the required libraries using pip:

        ```bash
        pip install pygame pygamevideo
        ```

### How to Use

1. **Run the Application:**

    *   Navigate to the project directory in your terminal.
    *   Execute the `main.py` file:

        ```bash
        python main.py
        ```
2. **Gameplay:**

    *   Follow the on-screen instructions (either in the console or the GUI).
    *   The game will guide you through the introduction, player setup, and challenges.
    *   In GUI mode, interact with buttons and input fields using your mouse and keyboard.

## 2. Technical Documentation

### Game Algorithm

1. **Start Menu:**
    *   Display the game title and a "PRESS SPACE TO PLAY" prompt.
    *   Play an intro video.
2. **Introduction:**
    *   Display a text-based introduction to the game's story and objectives.
3. **Player Count Selection:**
    *   Prompt the user to choose the number of players (1-3).
4. **Player Information Input:**
    *   For each player, prompt for their name, profession, and whether they are the leader (if no leader is selected, the first player is automatically assigned as the leader).
5. **Challenge Menu:**
    *   Present a menu to choose a challenge type: Math, Logic, Chance, or Pere Fouras (riddle).
6. **Player Choice:**
    *   Ask the user to choose which player will attempt the challenge.
7. **Challenge Execution:**
    *   Run the selected challenge.
    *   Determine if the player won (got a key) or lost.
    *   Update the player's key count accordingly.
8. **Key Check:**
    *   After each challenge, check if the total number of keys collected by all players is 3 or more.
9. **Final Challenge (if 3 or more keys):**
    *   If enough keys are collected, proceed to the treasure room challenge.
    *   Present 3 clues initially, then more if needed.
    *   Prompt the player to guess the code word.
    *   Determine if the player won or lost the final challenge.
10. **Game End:**
    *   Display a "You won!" or "You lost!" message based on the final challenge outcome.
    *   Show the scores of each player (name and number of keys).

### Functions

Here's a simplified overview of the functions, grouped by file. Details about parameters and specific behaviors are found within the code comments.

#### `chance_challenges.py`

*   `shell_game()`: Simulates a shell game.
*   `roll_dice_game()`: Simulates a dice-rolling game.
*   `chance_challenge()`: Randomly selects and runs a chance challenge.
*   `shell_game()`: GUI version of the shell game.
*   `roll_dice_game()`: GUI version of the dice-rolling game.
*   `chance_challenge(player)`: GUI for selecting and playing chance challenges.

#### `final_challenge.py`

*   `treasure_room()`: No-GUI version of the treasure room challenge.
*   `final_challenge(players)`: GUI version of the final challenge.
*   `winner(who, players)`: Displays the game over screen and player scores.

#### `logical_challenges.py`

*   `display_sticks(n)`: Displays sticks for the Nim game.
*   `player_removal(n)`: Gets player input for Nim.
*   `master_removal(n)`: AI logic for Nim.
*   `nim_game()`: Main Nim game logic.
*   `display_grid(grid)`: Displays the Tic Tac Toe grid.
*   `check_victory(grid, symbol)`: Checks for a win in Tic Tac Toe.
*   `master_move(grid)`: AI logic for Tic Tac Toe.
*   `player_turn(grid)`: Gets player input for Tic Tac Toe.
*   `master_turn(grid)`: Executes the master's turn in Tic Tac Toe.
*   `full_grid(grid)`: Checks if the Tic Tac Toe grid is full.
*   `check_result(grid)`: Checks for a win or draw in Tic Tac Toe.
*   `tictactoe_game()`: Main Tic Tac Toe game logic.
*   `nim_game(player)`: GUI version of the Nim game.
*   `winner(who)`: Displays the game over screen for Nim.

#### `math_challenges.py`

*   `Factorial(n)`: Calculates the factorial of n.
*   `math_challenge_factorial()`: Factorial challenge.
*   `solve_linear_equation()`: Generates a linear equation.
*   `math_challenge_equation()`: Linear equation challenge.
*   `math_roulette_challenge()`: Math roulette challenge.
*   `is_prime(n)`: Checks if a number is prime.
*   `nearest_prime(n)`: Finds the nearest prime to n.
*   `math_challenge_prime()`: Nearest prime challenge.
*   `math_challenge()`: Randomly selects and runs a math challenge.
*   `equation_challenge()`: GUI version of the equation challenge.
*   `factorial_challenge()`: GUI version of the factorial challenge.
*   `prime_challenge()`: GUI version of the prime challenge.
*   `math_challenge(player)`: GUI for selecting and playing math challenges.

#### `the_pere_fouras_challenge.py`

*   `load_riddles(file)`: Loads riddles from a JSON file.
*   `pere_fouras_riddles()`: No-GUI version of the Pere Fouras riddle challenge.
*   `pere_fouras_riddles(player)`: GUI version of the Pere Fouras riddle challenge.

#### `utility_functions.py`

*   `StartMenufunc()`: Displays the start menu.
*   `Introduction()`: Displays the game introduction.
*   `PlayerCount()`: Prompts for the number of players.
*   `Compose_Equipe(nbr)`: Gets player information.
*   `ChallengeMenu()`: Displays the challenge selection menu.
*   `PlayerChoice(game)`: Handles player selection for challenges and game logic.

#### `Utils.py`

*   `history(text)`: Logs text to the `history.txt` file.
*   `nuage_forward(w, c=None)`: Animates clouds moving forward.
*   `nuage_backward(w)`: Animates clouds moving backward.

#### `objects.py`

*   `Object`: Base class for all GUI objects.
*   `Box`: A customizable box widget.
*   `Label`: A text label widget.
*   `Input`: A text input widget.
*   `Grid`: A grid widget.
*   `Win`: The main window widget.
*   `convertToGrid(l, forEach=None)`: Converts a list to a grid of widgets.

### Input and Error Management

*   **Input Validation:**
    *   The `player_removal` function in `logical_challenges.py` validates that the player's input in the Nim game is within the allowed range (1, 2, or 3).
    *   The `player_turn` function in `logical_challenges.py` validates that the player's input in Tic Tac Toe is within the allowed range and that the chosen cell is empty.
    *   In general, user input is cast to the appropriate data type (e.g., `int`, `float`) and checked for validity where necessary.
*   **Error Handling:**
    *   The `load_riddles` function uses a `try-except` block to handle potential `FileNotFoundError` when loading JSON files.
    *   The `loadImage` method of the `Object` class includes error handling for loading images in the GUI.
    *   The game includes basic error handling for unexpected input types.
*   **Intervals:**
    *   The `nim_game` function ensures that the player can only remove 1, 2, or 3 sticks.
    *   The `tictactoe_game` ensures that players can only place their symbol in empty cells within the 3x3 grid.
*   **Known Bugs:**
    *   In `final_challenge.py`, in the `keyboard_listener` function, the keys are limited to letters and backspace, the numbers don't work, they should be added.
    *   In `math_challenges.py`, in the `equation_challenge` function, the numbers generated for a and b don't take into account negative values, they should be added.

## 3. Logbook

### Project Chronology

*   **2023-11-27:** Project, repository creation, initial file structure setup, implementation of the start menu and introduction sequence.
*   **2023-11-28:** Development of core game logic, including player count selection and team composition. Implemented basic challenge selection menu.
*   **2023-11-29:** Work on the first versions of the math and logic challenges. Integration of the Pere Fouras riddle challenge.
*   **2023-11-30:** Implementation of chance challenges. Development of the initial version of the final challenge.
*   **2023-12-01:** Introduction of the GUI using Pygame for math and logic challenges. Started work on enhancing the user interface.
*   **2023-12-02:** Continued development of the GUI for chance challenges and the final challenge. Refinement of game aesthetics.
*   **2023-12-03:** Implementation of cloud animation for transitions between game screens.
*   **2023-12-04:** Finalization of the GUI for all challenges. Bug fixes and improvements to user interaction.
*   **2023-12-05:** Code optimization and final touches to the user interface.
*   **2023-12-06:** Final review, writing of documentation, and project submission.

**Decisions Made:**

*   Using Pygame for the GUI to enhance player engagement.
*   Implementing a cloud animation for smoother transitions between game phases.

**Problems Encountered:**

*   Initial difficulties with Pygame event handling, resolved by restructuring the event loop.
*   Challenges in synchronizing animations with game logic, addressed through code optimization.

### Task Distribution

*   **Gabriel:**
    *   Implementation of the GUI for most challenges.
    *   Development of the cloud animation.
    *   Design and implementation of the Pere Fouras riddle challenge with GUI.
*   **Jules:**
    *   Development of the initial game structure and core logic.
    *   Implementation of the math challenges, both console-based and GUI versions.
    *   Design and implementation of the final challenge.
    *   Creation of utility functions and overall code organization.

## 4. Testing and Validation

### Test Strategies

*   **Unit Tests:** Individual functions were tested during development to ensure they work correctly in isolation (e.g., `Factorial`, `is_prime`, `nearest_prime`).
*   **Integration Tests:** Challenges were tested together to ensure they integrate correctly with the main game loop and player data.
*   **Gameplay Tests:** The entire game was played multiple times to test the flow, challenge selection, key collection, and final challenge.
*   **Input Validation Tests:**  Various inputs were tested to ensure the game handles them correctly (e.g., valid numbers, invalid numbers, empty strings).
*   **GUI Tests:** The GUI was tested to ensure buttons, input fields, and labels work as expected and the layout is correct.

### Specific Test Cases and Results

1. **Nim Game:**
    *   Test Case: Player inputs 1, 2, and 3.
        *   Result: Game proceeds correctly.
    *   Test Case: Player inputs 0, 4.
        *   Result: Game prompts the player to re-enter a valid number.
2. **Tic Tac Toe:**
    *   Test Case: Player tries to place a symbol in an occupied cell.
        *   Result: Game prompts the player to choose an empty cell.
    *   Test Case: Player wins the game.
        *   Result: Game declares the player as the winner.
3. **Math Challenges:**
    *   Test Case: Correct and incorrect answers for each type of math problem.
        *   Result: Game correctly identifies correct and incorrect answers and awards keys accordingly.
4. **Chance Challenges:**
    *   Test Case: Run each chance challenge multiple times to ensure randomness.
        *   Result: Games behave randomly as expected.
5. **Pere Fouras Challenge:**
    *   Test Case: Correct and incorrect answers for different riddles.
        *   Result: Game correctly identifies correct and incorrect answers and awards keys accordingly.
6. **Final Challenge:**
    *   Test Case: Correct and incorrect code word guesses.
        *   Result: Game correctly identifies correct and incorrect guesses, provides additional clues, and determines the winner or loser.

### Screenshots

Here are some screenshots showing the tests in action (you would replace these with actual screenshots from your game):

**GUI Nim Game**

![GUI Nim Game](resources/images/nim_game_gui.png)

**GUI Tic Tac Toe**

![GUI Tic Tac Toe](resources/images/tictactoe_gui.png)

**GUI Math Challenge**

![GUI Math Challenge](resources/images/math_challenge_gui.png)

**GUI Chance Challenge**

![GUI Chance Challenge](resources/images/chance_challenge_gui.png)

**GUI Pere Fouras Challenge**

![GUI Pere Fouras Challenge](resources/images/riddle_challenge_gui.png)

**GUI Final Challenge**

![GUI Final Challenge](resources/images/final_challenge_gui.png)

**Start Menu**

![Start Menu](resources/images/start_menu.png)

**Player Selection**

![Player Selection](resources/images/player_selection.png)

**Challenge Selection**

![Challenge Selection](resources/images/challenge_selection.png)