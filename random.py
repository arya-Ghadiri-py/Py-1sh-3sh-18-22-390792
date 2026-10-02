import random 


while True :
    list1=[]
    list3=[]
    list2=[]
    menu=input("1.esm 2.kado 3.exit==")
    while True :
        match menu :
            case "1" :
                name=input("enter a name")
                list1.append(name)
                break
            case "2" :
                kadoo=input("enter kadoo ha ")
                list2.append(kadoo)
                break
            case "3" :
                list3.append(random.choices(list1),"win",random.choices(list2))
                print(list3)