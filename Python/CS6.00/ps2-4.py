# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

word = list(choose_word(wordlist))
ans = list('_' * len(word))
guess = 10
used = list()
print word
check = 0

while True:
    letter = raw_input('>Choose a letter: ')
    for i in range(len(word)):
        if letter == word[i]:
            ans[i] = letter
            check = 1
    if check == 0:
        guess -= 1 
    elif check ==1:
        check = 0
    used += list(letter)
    print 'Remaining guesses: %r' % guess
    print 'Letters Used: %r' % ''.join(used)  
    print ' '.join(ans)
    if word == ans:
        print 'YOU WIN'
        break
    elif guess <= 0:
        print 'YOU LOSE'
        print 'The word was: %r' %''.join(word)
        break
        