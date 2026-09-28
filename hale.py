student=[]
java=[]
python=[]
while True :
    menu=input("1.pyhon 2.java 3.exit")
    match menu :
        case "1" :
            while True :
                python1=float(input("nomre.py.bede"))
                student1=input("esm bede")
                python.append(python1)
                python.append(student1)
                break
        case "2" :
            while True :
                java1=float(input("nomre java bede"))
                student1=input("esm bede")
                java.append(java1)
                java.append(student1)
                break
        case "3" :
            print("happy to see you")
            student=["python=",python1,"java=",java1]
            print(student)
    break