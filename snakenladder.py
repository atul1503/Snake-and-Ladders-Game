import random
def check(player,score):
    snake=[[28,10],[37,3],[47,16],[75,32],[94,71],[96,42]]
    ladder=[[4,56],[12,50],[14,55],[22,58],[41,79],[54,88]]
    for i in range(len(snake)):
        if score is snake[i][0]:
            print(player,'got bit by a snake :(')
            score=snake[i][1]
        elif score is ladder[i][0]:
            print(player,'climbed a ladder :)')
            score=ladder[i][1]    
    return score

def game(player,player_score):
    step=random.choice([1,2,3,4,5,6])
    print(player,'got',step)
    if player_score==0 and step!=6:
        player_score=0
    elif player_score+step>100:
        print(player,'has to get',100-player_score,'to win')
    elif player_score!=0 and step==6:
        player_score=player_score+step
        player_score=game(player,player_score)
    elif player_score==0 and step==6:
        player_score=6
    else:
        player_score+=step
    player_score=check(player,player_score)
    print(player,'score:',player_score)
    input()
    return player_score

print(50*'-','Snake N Ladder Game',50*'-')
user=input('Enter the name of the user:')
user_score=0
computer_score=0
computer='Computer'
count=0
print('--The game starts now--')
print("INSTRUCTIONS:Press 'Enter' after every move")
while user_score!=100 and computer_score!=100:
    print(count,6*'-')
    count+=1
    user_score=game(user,user_score)
    if user_score==100:
        print(25*'-',user,'won the game',25*'-')
        input()
        break
    computer_score=game(computer,computer_score)
    if computer_score==100:
        print(25*'-',computer,'won the game',25*'-')
        input()
print(50*'-','The Game Has Ended',50*'-')
input()
