def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    i = 0
    removeDuplicates=''
    listofWord=list(secretWord)
    copyofword=listofWord[:]
    if len(lettersGuessed)==0:
        for i in range(len(secretWord)):
            copyofword[i]='_'
    else:
        for let in lettersGuessed:
            if let not in removeDuplicates:
                removeDuplicates+=let
        for i in range(len(listofWord)):
            for let in removeDuplicates:
                if listofWord[i]==let:
                    copyofword[i]=let
                    break
                else:
                    copyofword[i]='_'
    return " ".join(copyofword)