import function as f

white = "\033[0;37m"
blue = "\033[1;34m"
orange = "\033[1;33m"

print (blue + "The names of the developers - 'Alon Shaul' and 'Omer Shlomo'\n" + white)

print (orange + "Welcome to the game 'Hangman' : \n" + white)

game_word = f.challenge()

f.play(game_word)