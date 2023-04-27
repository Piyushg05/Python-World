import random
n=random.randint(1,100)
atmpt=int(input("ENTER THE ATTEMPT: "))
while(atmpt):
    n2=int(input("\nENTER THE NUMBER: "))
    if n2==n:
        print("----YOU WON----")
        break
    elif n2<n:
        print("---WRONG ATTEMPT---\n")
        print("YOUR GUESS IS SMALLER")
    elif n2>n:
        print("---WRONG ANSWER---\n")
        print("YOUR GUESS IS LARGER")
    atmpt-=1    
else:
    print("YOUR ATTEMPT IS OVER\n")
    print("---YOU LOSE---")
print("YOUR CHOICE IS ",n2)
print("SYSTEM CHOICE IS ",n)        
