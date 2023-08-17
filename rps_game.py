import random
l=["rock","paper","scissors"]
print("Welcome to the ultimate game challenge-RPS")

while True:
    uc=int(input('''
     
    game start.....
      1.yes
      2.exit
       
         '''))
    ucount=0
    ccount=0
    if uc==1:
        for a in range(0,5):
            userinput=int(input('''
            
              choose.....
              1.rock
              2.paper
              3.scissors
            
            
            '''))
           
            
            
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="paper"
            elif userinput==3:
                uchoice="scissors" 
            

            cchoice = random.choice(l)  
           
            if uchoice==cchoice:
                print("game drawn")
                print("user choice",uchoice)
                print("computer choice",cchoice)
                ucount=ucount+1
                ccount=ccount+1     

            elif (uchoice=="rock" and cchoice=="scissors") or (uchoice=="paper" and cchoice=="rock") or(uchoice=="scissors"and cchoice=="paper") :

                print("user wins")
                print("user choice",uchoice)
                print("computer choice",cchoice)
                ucount=ucount+1     

            else:
                 print("computer wins")
                 print("user choice",uchoice)
                 print("computer choice",cchoice)  
                 ccount=ccount+1 
            if ucount==ccount:
                print("Draw match and the scores are:")
            elif ucount>ccount:
                print("user win and the scores are:")
            else:
                print("computer wins and the scores are:")        

        print(ucount)
        print(ccount)   

    else:
        break

 