#case 1
def case1() :
    price_card=int(input("sharzh kon"))
    price_=int(input("sharzh kon"))
    if price_card>=price_ :
        kif_pool+=price_
        return(kif_pool)
    else:
        return("mojodi nadari")

case1()