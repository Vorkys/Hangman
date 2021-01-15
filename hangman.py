import random

#list of words the player can get
words = ["pen", "iron", "book", "cat", "snake", "objective", "human", "monkey", "car", "mouse", "microphone", "hashtag", "keyboard", "disc", "skateboard", "algorithm",
         "eye", "ball", "programing", "curtains", "window", "teacher", "beer", "alcohol", "ship", "camp", "shop", "violin", "scooter", "swing", "towel", "mirror", "duvet",
         "computer", "sport", "desk", "money", "virtual", "faith", "cactus", "chocolate", "sweet", "comics", "radiator", "loan", "leak", "screen"]
def game():
    """this handles the whole "guess the word" part
    I will split it into 2 parts.
    1. pick and create the word to be guessed
    2. the part where the player is guessing the word"""
    global words
    #1.part - creates the word to guess#
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]     #these are the letters that the player can pick top guess the word
    used_letters = []
    word = [n for n in str(words[random.randrange(0, len(words) - 1)])]         #randomly choose a word from words and keep it in list char by char exp.:["p", "e", "n"]
    word_guess = []

    for letter in word:                                                         #print the "_" so the player can see how many letters there are
        word_guess.append("_")
    
    #2.part - actually the guesses#
    lives = 8
    correct = 0
    lost = False
    while correct != len(word):                                                 #while the word isnt complete
        print(52 * "=")

        if lives == 0:                                                          #no lives left -> it ends the game and reveal the word
            print("You lost. The word was: ")
            print(" ".join(map(str, word)))
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

    if lost == False:
        print("You won! The word was: ")
        print(" ".join(map(str, word)))


def play_game():
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
        print("Game over.")

#rules#
print("Rules & informations: ")
print("1) diacritics arent counted")
print("2) should be possible to play infinitely")
print("3) words, which the player adds wont be keeped after restart(WIP to even remove a word)")
print("4) you can add a word by typing add when asked to")
print("5) you can stop to guess at anytime, just write stop")

play_game()
