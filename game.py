import random

results=[("stone","scissors"),("paper","stone"),("scissors","paper"),("paper","spok"),("stone","lizard"),("scissors","lizard"),("lizard","spok"),("lizard","paper"),("spok","stone"),("spok","scissors"),("stone","lizard")]
moves=[result[1] for result in results]

player_score,computer_score,tie_score=(0,0,0)
player=input("Enter stone / paper / scirssors / lizard / spok / quit : ").lower()

while player !="quit":
    computer=random.choice(moves)
    print("Player chose {} , Computer chose {}".format(player,computer))
    if player == computer:
        tie_score +=1
        print("it's a tie!")
        print("Current Score")
        print("Player={} , Computer={} , No.of ties={}".format(player_score,computer_score,tie_score))
    elif (player,computer) in results:
        print("Player won!")
        player_score +=1
        print("Current Score")
        print("Player={} , Computer={} , No.of ties={}".format(player_score,computer_score,tie_score))
    elif (computer,player) in results:
        print("Computer won!")
        computer_score +=1
        print("Current Score")
        print("Player={} , Computer={} , No.of ties={}".format(player_score,computer_score,tie_score))
    else:
        print("Invalid input! Try again;)")
    player=input("Enter rock / paper / scirssors / lizard / spok / quit : ")
print("\n\nFINAL SCORES: \n")
print("PLAYER={} , COMPUTER={} , TIE={}\n".format(player_score,computer_score,tie_score))
if player_score>computer_score:
    print("Player wins!!😎\n")
elif computer_score>player_score:
    print("Computer wins!!🥳\n")
elif player_score==computer_score:
    print("It's a tie!!🥳\n")