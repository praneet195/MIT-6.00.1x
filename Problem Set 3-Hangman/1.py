def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    a=''
    for let in lettersGuessed:
        if let not in a:
            a+=let
    for let in a:
        if let in secretWord:
            count+=secretWord.count(let)
    if count == len(secretWord):
            return True
    else:
            return False