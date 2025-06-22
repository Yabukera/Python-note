import random

signs = ('rock', 'paper', 'scissor')

class player:
    
    def __init__(self):
        
        self.hand = None
        
class computer:
    
    def __init__(self):
        
        sign = random.randint(0,2)
        self.hand = signs[sign]

def check(players, computers):
    
    if players == 'rock':
        
        if computers == 'rock':
        
            print("no one wins")
        
        elif computers == 'paper':
        
            print("tne computer won")
        
        elif computers == 'scissor':
            
            print("congratulations\n")
            print("you won")
        
    elif players == 'paper':
        
        if computers == 'rock':
        
            print("congratulations\n")
            print("you won")
        
        elif computers == 'paper':
        
            print("no one wins")
        
        elif computers == 'scissor':
            
            print("tne computer won")
            
    elif players == 'scissor':
        
        if computers == 'rock':
        
            print("tne computer won")
        
        elif computers == 'paper':
        
            print("congratulations\n")
            print("you won")
        
        elif computers == 'scissor':
        
            print("no one wins")

yabu = player()
com = computer()

print("****************************************\n")

print("let's play rock paper scissors\n")
print("1. choose  /'r/' for rock")
print("2. choose  /'p/' for paper")
print("3. choose  /'s/' for scissor\n")

print("****************************************")

choice = input("choose one from the above: ")

if choice == 'r':
    
    yabu.hand = 'rock'
    
elif choice == 'p':
    
    yabu.hand = 'paper'
    
elif choice == 's':
    
    yabu.hand = 'scissor'
    
else:
    
    print("you chose an invalid one")
    

print(f"you chose {yabu.hand}")

print(f"the computer chose {com.hand}")

check(yabu.hand, com.hand)