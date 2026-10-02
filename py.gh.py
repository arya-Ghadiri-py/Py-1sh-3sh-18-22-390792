import random  


while True :
    menu=("1.oozv  2.exit")
    list1=[]
    while True :
        match menu :
            case "1" :
                x=input("enter a name")
                x.append(list1)

                break
            case "2" :
                print(random.choice(list1))
                break
    break