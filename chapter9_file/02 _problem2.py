import random

def game():
    print("You are playing the game ! ")
    score = random.randint(1,62)
    #Fetch the highdcore 
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0
        
    print(f"Your score: {score}")
    if(score>highscore):
        with open("hoscore.txt","w") as f:
            f.write(str(score))
            
    return score

game()