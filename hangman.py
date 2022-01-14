import typer
from logic_pkg import logic
from logic_pkg.player import Player

# Set up game
player = Player()
# Set Puzzle Word
logic.game_setup()

# Start Game Loop
while True:
    # Print current Hangman state
    logic.draw_game_board(player)
    # logic.print_current_hangman(playe
    # Ask player for guess
    guess = input("      Enter guess: ")
    # Check Guess
    logic.check_guess(player, guess)
    # Check Game State
    logic.end_game(player)


if __name__ == "__main__":
    app()
