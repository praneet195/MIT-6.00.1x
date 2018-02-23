def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    checkvalue=False
    if word in wordList:
        for k in word:
            if k in hand.keys() and word.count(k) <= hand.get(k, 0):
                checkvalue=True
            else:
                checkvalue=False
                break
    return checkvalue
                