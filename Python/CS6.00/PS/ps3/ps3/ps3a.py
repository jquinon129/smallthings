# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    score = 0
    word = list(word)
    
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i] * len(word)
    if len(word) == n:
        score += 50
    return score

    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO...
    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
	word = list(word)
	#hand_new = hand.copy()
	for i in word:
		hand[i] -= 1 #hand_new
	return hand #hand_new

    # TO DO ...

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):

    word_dic = get_frequency_dict(word)
    
    if word in word_list:
        for i in word_dic:
            if hand.get(i, 0) - word_dic.get(i, 0) < 0:
                return False
        return True
    
    else: 
        return False

    # TO DO...

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
	total_score = 0
	while True:
		display_hand(hand)
		input_word = raw_input('Enter word or a "." to indicate you are finished: ')
		
		if input_word == '.' or calculate_handlen(hand) == 0:
			print "Total Score: %r" % total_score
			break

		elif is_valid_word(input_word, hand, word_list) == True:
			hand = update_hand(hand, input_word)
			score = get_word_score(input_word, HAND_SIZE)
			print ('%r earned %r points.') % (input_word, score)
			total_score+= score
			print ('Total score: %r \n') % total_score

    # TO DO ...

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
	hand = deal_hand(HAND_SIZE)
	hand_original= hand.copy()
	
	while True:
		input_mode = raw_input("Input 'n'ew 'r'etry or 'e'xit: ")
		
		if input_mode =='n':
			hand = deal_hand(HAND_SIZE)
			hand_original = hand.copy()
			play_hand(hand, word_list)
		elif input_mode == 'r':
			hand = hand_original.copy()
			play_hand(hand, word_list)
		elif input_mode == 'e':
			break
		else:
			pass

    # TO DO...

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
