import random 
def dice(): 
    for i in range(1):
        return random.randint(1,6)   
        
def mo_pl(player,step):
    player=player+step 
    if player>100:
        player=100
    return player 

def sugges(possugg): 
    if possugg==15: 
        print("you rolles the point 1 you will down")
        print("if you get 1 point you will down point of 6") 
    elif possugg==45 or possugg==46:
        print("if you get 1 or 2 points you are goes to position of 26")   
    elif possugg==48:
        print("if you are get 1 or 2 points goes down to 11")   
    elif possugg==55: 
        print("you are get 1 point you will down to 53")    
    elif possugg==60 or possugg==61: 
        print("you are get 1 or 2 points you will down at point of 19")  
    elif possugg==63: 
        print("you are get 1 point, you are down 60 ") 
    elif possugg==86 or possugg==85: 
        print("you are get point 1 or 2, you are get down to 24")  
    elif possugg==92:
        print("you are get position of 93, you are down in position of 73") 
    elif possugg==94 or possugg==93: 
        print("you are get position of 95, you are down in 75")  
    elif possugg==97:
            print("you are get position of 98, you are down in position of 78") 
    elif possugg==1:
        print("you are get 1 point,chance to position of 38")
    elif possugg==3:
        print("you are get 1 point,chance to position of 14")
    elif possugg==8:
        print("you are get 1 point,chance to position of 31")  
    elif possugg==20:
        print("you are get 1 point,chance position of 42") 
    elif possugg==27:
        print("you are get 1 point,chance position of 84")      
    elif possugg==35:
        print("you are get 1 point,chance to position of 44") 
    elif possugg==50:
        print("you are get 1 point,chance to position of 67") 
    elif possugg==71:
        print("you are get 1 point,chance to position of 91") 
    elif possugg==80:
        print("you are get 1 point,chance to position of 90") 
    elif possugg==84:
        print("you are get 1 point,chance to position of 100")      
    return possugg

def snk_lad(pos): 
    snk={16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    lad={1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 90, 85:100}
    if pos in snk: 
        pos=snk[pos]               
        print("you are got down by snake") 
    elif pos in lad:
        pos=lad[pos]                          
        print("you are got the ladder to up") 
    return pos 

def playing(): 
    n=int(input("Enter the count of players:")) 
    plpos=[0]*n
    li=[[]for k in range(n)]
    win=[]
    fin=set()
    while True: 
        finpos=True
        for i in range(n): 
            print("\nplayer",i+1,"Turns") 
            position=sugges(plpos[i])
            print(position)
            input("Press enter to twice") 
            step=dice() 
            print("Player",i+1,"rolled",step) 
            plpos[i]=mo_pl(plpos[i],step) 
            plpos[i]=snk_lad(plpos[i])
            li[i].append(plpos[i])
            print("Player",i+1,"Position is",plpos[i]) 
            for k in range(n): 
                print("position of",k+1,"player =",li[k]) 
            if plpos[i]==100: 
                fin.add(i) 
                if i not in win: 
                    win.append(i) 
                
            if plpos[i]<100:
                finpos=False             
        
        print()
        for i in range(len(win)): 
            if i==0: 
                print(i+1,"st","Winning place is player:",win[i]+1) 
            elif i==1: 
                print(i+1,"nd","Winning place is player:",win[i]+1) 
            elif i==2:
                print(i+1,"rd","Winning place is player:",win[i]+1)    
            elif i<=3: 
                print(i+1,"th","Winning place is player:",win[i]+1)      
        
        if finpos:
            print("GAME OVER! ! !") 
            return             
                 
            
playing()                           


        
