mail=input()
leng=int(input())
olmayankarakterler=".,!<>&#$%{[]}/()+?*/~¨|'"
okson=",!<>&#$%{[]}/()+?*/~¨|'0123456789"
def mailDogrulama(mail):
    for x in  mail:
        if(x=="@"):
           index=mail.find("@")
           ilk=list(mail[0:index])
           son=list(mail[index+1:])
           uzSon=len(son)
           sayac=0
           
           for z in son:
               if(z=="."):
                   d=sayac
                   q=son[d+leng+1]
                   i=uzSon-4-d
                   if(q==".")and(leng==i):
                       return True
                       
                   else:
                       return False
                       
                   break

               else:
                   sayac+=1

           a=-1
           while a<index-1:
               a+=1
               
               if(olmayankarakterler.count(ilk[a])>0):
                   return False
               else:
                   return True
               b=-1 
           for s in son:
               b+=1
               if(okson.count(s)>0):
                   return False
               else:
                   return False
   
        
    else:
        return False         
            

if(mailDogrulama(mail)==False):
    print("Mail adresiniz yanlıştır.")
else:
    print("Mail adresiniz doğrudur.")



 
