import random

def gameWin(Player1,Player2):
    if Player1==Player2:
        return None
    if Player1=="Stone" and Player2=="Paper":
        return True
    if Player1=="Stone" and Player2=="Scissor":
        return False
    if Player1=="Paper" and Player2=="Scissor":
        return True
    if Player1=="Paper" and Player2=="Stone":
        return False
    if Player1=="Scissor" and Player2=="Paper":
        return False
    if Player1=="Scissor" and Player2=="Stone":
        return True
    
randomNo=random.randint(1,3)

if(randomNo==1):
    comp="Stone"

if(randomNo==2):
    comp="Paper"

if(randomNo==3):
    comp="Scissor"

you=input("What will you choose :\nStone\nPaper or\nScissor:\n")

result=gameWin(comp,you)

print("The computer has chosen: ",comp)

if(result==True):
    print("You Win!")
if(result==False):
    print("You Lose")
if(result==None):
    print("Its a tie")
