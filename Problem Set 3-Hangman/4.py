def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    trackGuesses=''
    chances=8
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    while chances>0:
        print("-"*10)
        print("You have",chances,"guesses left")
        print("Available Letters:",getAvailableLetters(trackGuesses))
        char=input("Please guess a letter: ")
        char=char.lower()
        if char in trackGuesses:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,trackGuesses))
            continue
        else:
            trackGuesses+=char
            if char not in secretWord:
                print("Oops! That letter is not in my word: ",getGuessedWord(secretWord,trackGuesses))
                chances-=1
            else:
                print("Good guess: ",getGuessedWord(secretWord,trackGuesses))
            if isWordGuessed(secretWord,trackGuesses):
                 break
    print("-"*10)  
    if isWordGuessed(secretWord,trackGuesses):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was",secretWord)