import random

print("Python Number Gambling Game")
print('-----------------------------------------------------------\n') 

low = 1
high = 100
money = 0

while True:
    guess = int(input(f'\nGuess a random number between {low} - {high} (0 to quit): '))
    money -= 2500
    random_num = random.randint(low, high)
    off = str(guess - random_num)
    
    if off[0] == '-':
        off = off[1:]
    
    low_range1 = random_num - 3
    high_range1 = random_num + 3
    
    low_range2 = random_num - 5
    high_range2 = random_num + 5
    
    low_range3 = random_num - 10
    high_range3 = random_num + 10
    
    low_range4 = random_num - 15
    high_range4 = random_num + 15
    
    while guess < 0 or guess > high:
        guess = int(input(f'Number must be above {low - 1} and below {high} (0 to quit): '))
        
    if guess == 0:
        money += 2500
        break
    
    elif guess == random_num:
        money += 50000
        loss_gain = 50000
        won_lost = 'won'
    
    elif guess in range(low_range1, high_range1):
        money += 45000
        loss_gain = 45000
        won_lost = 'won'
        
    elif guess in range(low_range2, high_range2):
        money += 35000
        loss_gain = 35000
        won_lost = 'won'
        
    elif guess in range(low_range3, high_range3):
        money += 25000
        loss_gain = 25000
        won_lost = 'won'
        
    elif guess in range(low_range4, high_range4):
        money += 10000
        loss_gain = 10000
        won_lost = 'won'
        
    else:
        money -= 2500
        won_lost = 'lost'
        loss_gain = -2500
        
    print(f'The number was {random_num}, you were {off} off!')
            
    print('\n-----------------------------------------------------------')
    print('You spent A$2,500')
    print(f'You {won_lost} A${loss_gain:+,}')
    print(f'Your total balance is now A${money:+,}')
    print('-----------------------------------------------------------')
        
print(f'\nYou finished with A${money:+,}')
