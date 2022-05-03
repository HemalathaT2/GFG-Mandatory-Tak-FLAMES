def Flames(name1,name2):
    add=name1+name2
    
    for i in add:
        if add.count(i)!=1:
            add=add.replace(i,"")

    l=""
    rem=len(add)%6
    print("Feeling Bored?")
    print("Let's play FLAMES :)")
    print("FYI\nF: Friends\nL: Love\nA: Affection:\nM: Marriage\nE: Enemy\nS: Siblings\n")

    if(rem==0):
        l+="Siblings"

    elif(rem==1):
        l+="Friends"

    elif(rem==2):
        l+="Love"

    elif(rem==3):
        l+="Affection"

    elif(rem==4):
        l+="Marriage"

    else:
        l+="Enemy"

    return l

n1=input("Enter Name1: ")
n2=input("Enter Name2: ")
n3=print("\t\t",(Flames(n1,n2)).upper(),"\t\t")
