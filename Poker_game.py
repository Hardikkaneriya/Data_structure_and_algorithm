# Simplified Poker Rank
# ---------------------
#  
# GIVENS
# ------
# 1. A deck consisting of 36 cards that have values ranging from 1 to 9. 
#    Each number has 4 cards, but there are no suits.
#  
# 2. A simplified poker game is played using this deck between two
#    players.  Players are dealt hands consisting of 4 cards. 
#  
#    The following are possible poker hands ranked from highest
#    value to lowest value:
#   
#    - Four of a kind  [ex. 7777]
#    - Three of a kind [ex. 8882]
#    - Two pairs       [ex. 9966]
#    - One pair        [ex. 3385]
#    - All distinct    [ex. 7931]
#
#    If two hands are equal in terms of the above levels, then the
#    values of the remaining cards in the hand will dictate the winner.
#  
#    For example, 3656 vs 6693.  
#
#      * Both hands have a single pair of 6's.
#
#      * After the pair of 6's, the first hand has 53 and the 
#        second hand has 93. 
#
#      * Since 9 > 5, then the second hand is the winner.
#  
#    If there are any questions regarding how hands should be compared,
#    please consult with the moderator.
#  
#  
# CHALLENGE
# ---------
#  
# Your challenge is to implement a comparison function that takes
# in as inputs two hands, one from Player 1 and one from Player 2,
# and then determines which player is the winner or if there is a tie.
#
# The design of the comparison function is completely up to you. You 
# have full control over how you would like to represent data and also
# how to present results of the comparison.
#  
#  
# ADDITIONAL COMPARISON EXAMPLES
# ------------------------------
#  
# 1122 >  9987  two pairs > one pair
# 6767 <  5545  two pairs < three of a kind
# 4554 == 5544  eq
# 2494 >  3132  one pair, 4 > 3
# 2788 >  5688  one pair, 7 > 6
# 1199 >  7788  two pairs, 9 > 8
# 6444 <  3555  three of a kind, 4 < 5
# 5689 <  4789  all distinct, 7 > 6


test_cases= ['7777', '8882']


def map_cards(test_case):
    dic = {i:0 for i in range(1,10)}
    for i in test_case:
         dic[int(i)] += 1
    return dic
map_cards('7777')


def card_count(test_card, pair ):
    dic = map_cards(test_card)
    for key, value in dic.items() :
        if value == pair:
            return key, value

print(card_count('7777',4))


def poker_games(test_card):
    if card_count(test_card,4) is not None:
        return 5  
    elif card_count(test_card,3) is not None:
        return 4
    elif card_count(test_card,2) is not None: 
        cnt = 0 
        for i in map_cards(test_card).values():
            if i == 2 :
                cnt += 1
        if cnt == 2 :
            return 3
        else:
            return 2
    else:
        return 1
    

print(poker_games('2241'))


def winner(hand_1, hand_2):
    result1= poker_games(hand_1)
    result2= poker_games(hand_2)
    
    if result1 > result2:
        return "hand_1 is a winner"
    elif result1== result2:
            print('dfd')            
    else:
        return "hand_2 is a winner"


