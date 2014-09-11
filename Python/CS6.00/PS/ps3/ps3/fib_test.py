def update_hand(hand, word):
	word = list(word)
	for i in word:
		hand[i] -= 1

	return hand 
hand =  {'a':0, 'q':1, 'l':1, 'm':1, 'u':0, 'i':1}
hand1 = hand.copy()
update_hand(hand, 'quail')
print hand1

