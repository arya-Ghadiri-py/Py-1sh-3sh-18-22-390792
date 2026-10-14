from majol1 import*

def foroshgah() :
    kif_pool=0
    admin_id="arya1234"
    sabad_kala={}
    while True :
        menu=input(" 1.sharzh kif 2.add 3.show 4.delete 5.kharid 6.exit ")
        match menu:
            case "1" :
                case1()
            case "2" :
                password=input("password bede")
                if password==admin_id :
                    product_id=int(input("adad bede"))
                    name=input("esm kala")
                    price=int(input("gheymat"))
                    sabad_kala[product_id]={"name":name,"price":price}
                    return(sabad_kala)
                    
                else :
                    return("ramz eshtebahe")
                    
            case "3" :
                product_id=int(input("adad bede"))
                if product_id in sabad_kala :
                    return(sabad_kala[product_id])
            case "4":
                product_id=int(input("adad bede"))
                if product_id in sabad_kala :
                    sabad_kala=sabad_kala.pop(product_id)
                    return(sabad_kala)
                    
                else :
                    return("ghalate")
                    
            case "5" :
                name=int(input("esm kala"))
                if name in sabad_kala :
                    price=int(input("poolo bezan"))
                    if kif_pool>=price :
                        kif_pool=kif_pool-price
                        return(kif_pool)
                        
                    else :
                        return("mojodi")
                        
                else :
                    break
            case "6":
                return("khosh amadid")

                