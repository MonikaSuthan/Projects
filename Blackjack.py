import random



suits={'Hearts','Diamonds','Spades','Clubs'}

ranks={'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace'}

values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
        'Jack':10,'Queen':10,'King':10,'Ace':11}
class card():
    
    def __init__(self,suit,rank):
        
        self.suit=suit
        self.rank=rank
        self.values=values[rank]
        
    def __str__(self):
        
        return f"{self.rank} of {self.suit}"
new_card=card('Hearts','Three')
print(new_card)
class Deck():
    
    def __init__(self):
        
        self.all_cards=[]
        
        for suit in suits:
            
            for rank in ranks:
                
                created_card=card(suit,rank)
                self.all_cards.append(created_card)
                
    def __str__(self):
        
        print(self.all_cards)
    
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal(self):
        
        return self.all_cards.pop(0)
mycard=Deck()
class Player_Hand():
    
    def __init__(self):
        
        self.cards=[]
        self.value=0
        self.aces=0
        
    def add_card(self,card):
        
        
        self.cards.append(card)
            
        self.value += values[card.rank]

    def adjust_for_ace(self):
            
            if self.value>17:
                
                self.cards.append(Chosen_card)
            
                self.value += 1
                
            if self.value<17:
                
                self.cards.append(Chosen_card)
            
                self.value += 11
player_hand=Player_Hand()
class Dealer_Hand():
    
    def __init__(self):
        
        self.cards=[]
        self.value=0
        self.aces=0
        
    def add_card(self,card):
        
        
        self.cards.append(card)
            
        self.value += values[card.rank]

    def adjust_for_ace(self):
            
            if self.value>17:
                
                self.cards.append(Chosen_card)
            
                self.value += 1
                
            if self.value<17:
                
                self.cards.append(Chosen_card)
            
                self.value += 11
dealer_hand=Dealer_Hand()
class Player_chips():
    
    def __init__(self):
        
        self.total=100
        self.bet=0
        
    def win_bet(self):
        
        self.total += self.bet
        
    def lose_bet(self):
        
        self.total -= self.bet
player_chips=Player_chips()
class Dealer_chips():
    
    def __init__(self):
        
        self.total=100
        self.bet=0
        
    def win_bet(self):
        
        self.total += self.bet
        
    def lose_bet(self):
        
        self.total -= self.bet
dealer_chips=Dealer_chips()
def take_bet():
    
    while True:
    
        try:

            player_chips.bet=int(input('Please enter a bet value: '))
            print(f"The bet amount is {player_chips.bet}")
            break

        except:
             print("That's an invalid input!Please enter a correct input")
take_bet()
def hit(deck,hand):
    
    if player_hand.value<17:
        
        player_hand.add_card(mycard.deal())
def hit_or_stand(deck,hand):
    
    global playing
    
    while True:
    
        choice=input("Do you want to hit('x') or stand('s')?: ")
        
        if choice=='x':
            
            hit(deck,hand)
            
        if choice=='s':
            
            print("Player opts to stand. Dealer plays")
            playing=False
        
        break
def show_some():
    print("Dealer's cards:")
    print("<card hidden>")
    print(dealer_hand.cards[1])
    print("\n")
    print("Player's cards:")
    print(player_hand.cards[0])
    print(player_hand.cards[1])
    print("\n")
    
def show_all():
    print("Dealer's cards:")
    print(*dealer_hand.cards,sep='\n')
    
    print("\n")
    print("Player's cards:")
    print(*player_hand.cards,sep='\n')
    print("\n")
def player_busts():
    
    
        print("Player Busts")
        player_chips.lose_bet()
        
    
def player_wins():
    
    
        print("Player wins")
        player_chips.win_bet()

def dealer_busts():
    
    
        print("Dealer Busts")
        dealer_chips.lose_bet()
    
    
def dealer_wins():
    
    
        print("Dealer wins")
        dealer_chips.win_bet()

def push():
    print("Dealer and Player tie! It's a push.")
from IPython.display import clear_output
gameon=True

playing=True

while gameon==True:
    
    clear_output()
    
    print("Welcome to Blackjack!")
    
    mycard=Deck()
    mycard.shuffle()
    
    dealer_chips=Dealer_chips()
    player_chips=Player_chips()
    
    take_bet()
    
    player_hand=Player_Hand()
    player_hand.add_card(mycard.deal())
    player_hand.add_card(mycard.deal())
    
    dealer_hand=Dealer_Hand()
    dealer_hand.add_card(mycard.deal())
    dealer_hand.add_card(mycard.deal())
    
    show_some()
    
    show_all()
    
    while playing:
        
        hit_or_stand(mycard,player_hand)
    
        show_all()
        
        if player_hand.value>=21:
        
            player_busts()
            
            break
            
        if player_hand.value>dealer_hand.value and player_hand.value!=21:
            
            player_wins()
            
            break
            
        if dealer_hand.value>=21:
            
            dealer_busts()
            
            break
            
        if player_hand.value<dealer_hand.value and dealer_hand.value!=21:
            
            dealer_wins()
            
            break
            
    print(f"Player's winnings stand at {player_chips.total}")
        
    result=input("Do you want to continue?(y or n): ")
    
    if result=="y":
        
        gameon =True
    
    if result=="n":
        
        gameon=False

            
        