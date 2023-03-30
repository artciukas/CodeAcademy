"""
Create a deck of cards class. 
Internally, the deck of cards should use another class, a card class. 
Your requirements are:
The Deck class should have a deal method to deal a single card from the deck
After a card is dealt, it is removed from the deck.
There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
"""
import random

class Deck:
   

    def get_card(self):
        pass

    def remove_from_deck(self):
        pass

    def check_52_cards_and_redeal(self):
        pass


class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    pass




deck = Deck()
