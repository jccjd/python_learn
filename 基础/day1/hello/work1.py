import random
# stone = 0
# bu = 1
# x = 2
player = [2,2,2,0,0]
def rule(player1,player2):
    if player1 == player2:
        return 3
    elif player1 > player2 and player1 - 1 == player2:
        return player1
    elif player2 > player1 and player2 - 1 == player1:
        return player2
    elif player2 > player1 and player2 -2 == player1:
        return player1
    elif player1 >player2 and player1 - player2 == 2:
        return player2

while True:
    count = 0
    computer_count = []
    for i in player:
        computer = random.randint(0,2)
        computer_count.append(computer)
        if i == rule(i,computer):
            count += 1
            print(f'computer is {computer},you is {i},you win')
        elif computer == rule(i,computer):
            print(f'computer is {computer},you is {i},you loss')
        else:
            print(f'computer is {computer},you is {i},win win')

    print("win count: ", count)
    print("computer list: ", computer_count)
    print('player list: ', player)
    break
