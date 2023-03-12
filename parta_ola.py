#Vasiliki Katogianni
players=eval(input("Please input numbers of players: "))
beans=int(input("Please input number of beans per player: "))
import random
from random import randint
round=0
Pot=0
ex=0
budget=beans-1
lst=[x for x in range(1,players+1)]
player=int(randint(1,len(lst)))
d= dict.fromkeys(lst,beans)
while Pot==0 and ex==0:
    round=round+1
    print("-"*70)
    print("Round ",round," begins: everyone puts 1")
    for i in lst:
        if d[i]>0:
            Pot=Pot+1
    for i in lst:
        d[i]-=1
    print("Current state:")
    print("Pot: %i"%(Pot))
    for i in lst:
        if d[i]<0:
            print("Player",i,"is eliminated")
        else:
            print("Player",i,"'s budget: ",d[i])
    for z in lst:
        if d[z]<0:
            d.pop(z)
            lst.remove(z)       
    while Pot >0 and ex==0:
        print(""*120)
        orders=["put one","put two","everyone puts","take one","take two","take all"]
        while True:     
            if player<players: 
                player+=1
            elif player==players:
               player= 1
            if player in lst:
                break
        if len(lst)>1:
            spin1=orders[randint(0,len(orders)-1)]
            print("Player",player,"spinned ",spin1)
            if spin1 is orders[0]:    
                if d[player]>=1:Pot=Pot+1
                d[player]-=1
            if spin1 is orders[1]:      
                if d[player]>=2:
                    Pot=Pot+2
                elif d[player]==1:
                    Pot=Pot+1
                d[player]=d[player]-2 
            if spin1 is orders[2]:     
                for i in lst:
                    if d[i]>=1:Pot=Pot+1
                    d[i]=d[i]-1  
            if spin1 is orders[3]:     
                Pot=Pot-1
                d[player]+=1    
            if spin1 is orders[4]:     
                if Pot>=2:
                    Pot=Pot-2
                    d[player]+=2
                else:
                    Pot=Pot-1
                    d[player]+=1
            if spin1 is orders[5]:     
                d[player]=d[player]+Pot
                Pot=0
            print("Current state:")
            print("Pot: %i"%(Pot))  
            for i in lst:
                if d[i]<0:
                    print("Player",i,"is eliminated")
                else:
                    print("Player",i,"'s budget: ",d[i])
            lst2=lst[:]        
            for z in lst2:
                if d[z]<0:
                    d.pop(z)
                    lst.remove(z)
        if len(lst)==1:    
            for m in lst:
                if d[m]>=0:
                    print("Game finished: Player",m," wins")
            ex=1        
            break
        if len(lst)==0:
            ex=1
            print("Nobody wins.Game over.")
            break
        if Pot==0:
            print("Pot is zero: round ends")
            break           
