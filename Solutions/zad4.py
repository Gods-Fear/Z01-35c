import random


game_round = int(input("Please put how many rounds do you want to play: "))
game_items = ['rock', 'paper', 'scissors']
games_victory = 0
games_lose = 0
games_draw = 0
i = 1


while i <= game_round:
    game_user_choice = input("Plese put your choice \n 1. rock \n 2. paper \n 3. scissors \n")
    random_computer_choice = random.choice(game_items)
    print(f'Computer chose: {random_computer_choice}')

    if game_user_choice == '1' or game_user_choice.lower() == 'rock':
        if random_computer_choice == 'rock':
            print('We have a draw ')
            games_draw += 1
        elif random_computer_choice == 'paper':
            print('You lose :(')
            games_lose += 1
        else:
            print('You won :)')
            games_victory += 1

    elif game_user_choice == '2' or game_user_choice.lower() == 'paper':
        if random_computer_choice == 'rock':
            print('You won :)')
            games_victory += 1
        elif random_computer_choice == 'paper':
            print('We have a draw ')
            games_draw += 1
        else:
            print('You lose :(')
            games_lose += 1

    elif game_user_choice == '3' or game_user_choice.lower() == 'scissors':
        if random_computer_choice == 'rock':
            print('You lose :(')
            games_lose += 1
        elif random_computer_choice == 'paper':
            print('You won :)')
            games_victory += 1
        else:
            print('We have a draw')
            games_draw += 1

    else:
        print('Your choice is wrong !!!')
    print('--' * 15 + '\n')
    i += 1


print(f'You won: {games_victory} times.')
print(f'You lose: {games_lose} times.')
print(f'You had a draw: {games_draw} times.')
