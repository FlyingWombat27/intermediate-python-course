import random

def main():
    team_name1 = str(input('What is the name of team one?'))
    team_name2 = str(input('What is the name of team two?'))
    who_goes_first = str(input('Who will go first?'))
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    who_goes_second = str()
    dice_sum = 0
    
    if who_goes_first == team_name1:
        who_goes_second == team_name2
    else:
        who_goes_second == team_name1
        
    for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'{who_goes_first} rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'{who_goes_first} rolled a {roll}! Critical Success')
        else:
            print(f'{who_goes_first} rolled a {roll}')
    print(f'{who_goes_first} rolled a total of {dice_sum}')


if __name__== "__main__":
  main()