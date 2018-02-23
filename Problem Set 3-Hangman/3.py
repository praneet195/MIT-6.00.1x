def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a=''
    b='abcdefghijklmnopqrstuvwxyz'
    for let in b:
        if let not in lettersGuessed:
            a+=let
    return a     