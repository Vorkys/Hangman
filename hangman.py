import random

#list of words the player can get
words = ["pen", "iron", "book", "cat", "snake", "objective", "human", "monkey", "car", "mouse", "microphone", "hashtag", "keyboard", "disc", "skateboard", "algorithm",
         "eye", "ball", "programing", "curtains", "window", "teacher", "beer", "alcohol", "ship", "camp", "shop", "violin", "scooter", "swing", "towel", "mirror", "duvet",
         "computer", "sport", "desk", "money", "virtual", "faith", "cactus", "chocolate", "sweet", "comics", "radiator", "loan", "leak", "screen", "screenshot", "history book",
         "textbook", "power", "access", "index", "human race", "race car", "membership", "neighbor", "origin", "problem", "augmented reality", "long-range", "umbrella",
         "wellness"]
def game():
    """this handles the whole "guess the word" thing - I will split it into 2 parts.
    1. pick and create the word to be guessed
    2. the part where the player is guessing the word"""
    global words
    #1.part - creates the word to guess#
    #these are the letters that the player can pick top guess the word
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    used_letters = []
    word = [n for n in str(words[random.randrange(0, len(words) - 1)])]         #randomly choose a word from words and keep it in list char by char exp.:["p", "e", "n"]
    word_guess = []
    correct = 0

    for letter in word:                                                         #create the list for the word_guess
        if letter == "-":
            word_guess.append("-")
            correct += 1
        elif letter == " ":
            word_guess.append(" ")
            correct += 1
        else:
            word_guess.append("_")
    
    #2.part - actually the guesses#
    lives = 8
    lost = False
    while correct != len(word):                                                 #while the word isnt complete
        print(52 * "=")

        if lives == 0:                                                          #no lives left -> it ends the game and reveal the word
            print("You lost. The word was: ")
            print(" ".join(map(str, word)))
            print(52 * "=")
            lost = True
            break

        print("Lives: {}".format(lives))
        print("Word: ")
        print(" ".join(map(str, word_guess)))                                   #print the word in the state that the player achieved
        print("Unused letters: ")
        print(" ".join(map(str, letters)))                                      #print the letters that can be used
        print("Used letters: ")
        print(" ".join(map(str, used_letters)))                                 #print the letters that were used
        
        guess = input("Letter: ")                            #the player can write the letter uppercase or lowercase - doesnt change anything
        guess_up = guess.upper()
        guess_down = guess.lower()

        position = 0
        bad = True

        if guess_up in letters and len(guess) == 1:                 #letter not in word -> -1 health
            for _letter in word:
                if _letter == guess_down:                           #if the letter is in the world it reveals the letter and add it to the used_letters list aswel as removing it in the letter that are able to be used
                    correct += 1
                    word_guess[position] = word[position]
                    bad = False

                    if guess_up in letters:                         #needed if the letter is in word more than once otherwise it crashes
                        letters.remove(guess_up)
                        used_letters.append(guess_up)

                position += 1
            
            if bad == True:                                         #if the letter isnt in the word
                lives -= 1
                print("Wrong. You lost 1 health.")

                letters.remove(guess_up)
                used_letters.append(guess_up)

            position = 0

        elif guess_up == "STOP":                                    #stops the current game
            print("The word was: ")
            print(" ".join(map(str, word)))
            lost = True
            break
        else:                                                       #input isnt one letter or in the list of pickable letters - will reask the player while also reshowing the "game"
            print("invalid input")

    if lost == False:                                               #word is guessed, play_game() is called again
        print("You won! The word was: ")
        print(" ".join(map(str, word)))
        print(52 * "=")

def play_game():
    """main menu for the player"""
    n = input("Add a word(add) | New game(1/ano/yes): ")
    start = n.upper()
    if start == "1" or start == "ANO" or start == "YES":                #asks if the player wish to play a new game
        game()
        play_game()
    elif start == "ADD":                                                #player can add a word
        n = input("Word you wish to add: ")
        words.append(n)
        play_game()
    else:                                                               #ends the program
        print("Press 'enter' to exit...")
        input()

#rules#
print("Rules & informations: ")
print("1) no diacritics")
print("2) should be possible to play a new game 1000 time")
print("3) words, which the player adds wont be kept after restart(WIP to even remove a word)")
print("4) you can add a word by typing add when asked to")
print("5) you can stop guessing at any moment, just write 'stop'")
print("6) to end the program just write anything when asked if you want a new game")

play_game()
