from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    permutations = []
    score = 0
    selected_word = None
    
    for i in range(calculate_handlen(hand)):
        permutations += get_perms(hand, i+1)
    
    for i in permutations:
         if i in word_list:
            if get_word_score(i, HAND_SIZE) > score:
                score = get_word_score(i, HAND_SIZE)
                selected_word = i

    return selected_word

    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    score = 0
    tot_score = 0
    
    while True:
        display_hand(hand)
        selected_word = comp_choose_word(hand, word_list)
        if selected_word != None:
            print 'The selected word is:', selected_word
            score = get_word_score(selected_word, HAND_SIZE)
            print 'The score of the word is: ', score
            tot_score += score
            hand = update_hand(hand, selected_word)

        elif selected_word == None:
            break


    print 'No more words available'
    print 'The final score is: ', tot_score

    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    hand = deal_hand(HAND_SIZE)
    hand_original = hand.copy() 
    while True:
        input_mode = raw_input("Input 'n'ew 'r'etry or 'e'xit: ")
        
        if input_mode == 'e':
            break
       
        player_mode = raw_input("'u'ser or 'c'omputer: ")
        
        if player_mode == 'u':
            if input_mode =='n':
                hand = deal_hand(HAND_SIZE)
                hand_original = hand.copy()
                play_hand(hand, word_list)
            elif input_mode == 'r':
                hand = hand_original.copy()
                play_hand(hand, word_list)
            else:
                pass
        elif player_mode == 'c':
            if input_mode == 'n':
                hand = deal_hand(HAND_SIZE)
                hand_original = hand.copy()
                comp_play_hand(hand, word_list)
            elif input_mode == 'r':
                hand = hand_original.copy()
                comp_play_hand(hand, word_list)
            else:
                pass

    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
