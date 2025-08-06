#--------SORTING SUPERHEROES:bynamelength----------------------
def sortheroes():
    n=int(input("Enter how many heros: "))
    names=[]
    temp=0
    for i in range(n):
        name=input(f"Enter name{i+1} : ")
        names.append(name)
    print("Original list: ",names)
    for i in range(n): 
        for j in range(0, n - i - 1): 
            if len(names[j])<len(names[j+1]):
                temp=names[j+1]
                names[j+1]=names[j]
                names[j]=temp
    print("Descending order: ",names)
    
sortheroes()
