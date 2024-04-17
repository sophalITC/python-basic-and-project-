 #input
    #brospov : Python variables , data type,user input
    #visal   : lists,if/elif
    #david   : date , math , comments
 #output
    #brospov present fucntion that input size of water bottle
    #visal present funtion input number level sugar
    #david present function input age that can purchase or not
    

x= ("welcome to Drink store.")
y=("Please login")
print(x)
print(y)
name=str(input( "Enter your name :"))
num=int(input("Phone number :"))
add=input("Address:")
instock=["a.coca-cola","b.sting","c.pepsi","d.cambodia beer \n","e.cambodia water"
         ,"f.fanta","g.fresh milk","h.jelly","i.pro vida water","j.matcha",'k.ice latte',
         'l.coffee','m.strawberry milk','n.banana milk','o.vital water','p.oishi',
         'q.lemon juice','r.kiwi milk','s.orange juice','t.jinro strawberry',
         'u.coconut juice','v.grape juice','w.almond milk' ,'x.soda lemon',
         'y.soda ','z.coca-cola zero sugar',"a1.coca-cola no calories",'a2.grape juice'
         ,"a3.green tea",'a5.chocolate','a4.milo','a6.lactasoy','a7.aloe vera','a8.spy red'
         ,'a9.spy black',"a10.spy blue",'b1.olatte',"b2.v-active","c4.7-up",'b3.angkor puro'
         ,"b4.pocari sweat",'b5.wurkz','b6.bacchus','b7.dutch milk','b8.meiji'
         ,'b9.angkor milk','b10.kirisu','c1.samurai' ,'c2.ize','c3.vigor']
instock.sort()
print(instock)
dri=input("Add to your cart :")
many=int(input("How many ? :")) 
import datetime
x=datetime.datetime.now()
if dri=="a" :
    dri=("coca-cola")
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n"
          ,"-----------------------------\n",
          "Order :",dri,': 2 x',many,"pc" ,"\n" 
          ,"Total :",total,'$\n',
          "-----------------------------\n"
          ,"Total number of item sold :",many,'\n','costumer:',name,"\n","TEL: +885",num
          ,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
   
    print(x)
elif dri=='b':
    dri=('sting')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date :13/11/\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='c':
    dri=('pepsi')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='d':
        dri=('cambodia beer')
        age=int(input("how old are you :"))
        if 99>=age>=18:
                    total=(3*many)
                    print("\n")
                    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
                      "Order :",dri,': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
                      "-----------------------------\n","Total number of item sold :",many,'\n'
                      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
                      ,'Thank You For Your Order\n'
                      ,"PLEASE COME AGAIN")
                    print("ABA : 500 609 384")
                    print("AC : 0888905923")
                    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
                    print("Power by group 1")
                    print(x)
        else:
            print("YOU CAN NOT BUY", "\n","TRY AGAIN KID!!","\n",";(")
            print(x)
elif dri=="e" :
    dri=("cambodia water")
    size=input("a.350ml,b.500ml,c.1l :")
    if size=='a':
         size=("350ml") 
         total=(0.5*many)
         print("\n")
         print('',"Drink store\n","cash receipt\n","-----------------------------\n",
               "Order :",dri,': 0.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
               "-----------------------------\n","Total number of item sold :",many,'\n'
               ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
               ,'Thank You For Your Order\n'
               ,"PLEASE COME AGAIN")
         print("ABA : 500 609 384")
         print("AC : 0888905923")
         print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
         print("Power by group 1")
         print(x)
    elif size=='b':
          size=("500ml")
          total=(1.*many)
          print("\n")
          print('',"Drink store\n","cash receipt\n","-----------------------------\n",
                "Order :",dri,': 1 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
                "-----------------------------\n","Total number of item sold :",many,'\n'
                ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
                ,'Thank You For Your Order\n'
                ,"PLEASE COME AGAIN")
          print("ABA : 500 609 384")
          print("AC : 0888905923")
          print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
          print("Power by group 1")
          print(x)
    elif size=='c':
         size=("1l")
         total=(1.5*many)
         print("\n")
         print('',"Drink store\n","cash receipt\n","-----------------------------\n",
               "Order :",dri,': 1.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
               "-----------------------------\n","Total number of item sold :",many,'\n'
               ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
               ,'Thank You For Your Order\n'
               ,"PLEASE COME AGAIN")
         print("ABA : 500 609 384")
         print("AC : 0888905923")
         print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
         print("Power by group 1")
         print(x)
elif dri=='f':
    dri=('fanta')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11//2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
    
elif dri=='g':
   dri=('fresh milk')
   total=(3*many)
   print("\n")
   print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11//2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
   print("ABA : 500 609 384")
   print("AC : 0888905923")
   print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
   print("Power by group 1")
   print(x)
   
elif dri=='h':
    dri=('jelly')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
   
elif dri=="i" :
    dri=("pro vida water")
    size=input("a.350ml,b.500ml,c.1l :")
    if size=='a':
         size=("350ml") 
         total=(0.5*many)
         print("\n")
         print('',"Drink store\n","cash receipt\n","-----------------------------\n",
               "Order :",dri,size,': 0.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
               "-----------------------------\n","Total number of item sold :",many,'\n'
               ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
               ,'Thank You For Your Order\n'
               ,"PLEASE COME AGAIN")
         print("ABA : 500 609 384")
         print("AC : 0888905923")
         print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
         print("Power by group 1")
         print(x)
    elif size=='b':
          size=("500ml")
          total=(1.*many)
          print("\n")
          print('',"Drink store\n","cash receipt\n","-----------------------------\n",
                "Order :",dri,': 1 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
                "-----------------------------\n","Total number of item sold :",many,'\n'
                ,"date :13/11//2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
                ,'Thank You For Your Order\n'
                ,"PLEASE COME AGAIN")
          print("ABA : 500 609 384")
          print("AC : 0888905923")
          print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
          print("Power by group 1")
          print(x)
    elif size=='c':
         size=("1l")
         total=(1.5*many)
         print("\n")
         print('',"Drink store\n","cash receipt\n","-----------------------------\n",
               "Order :",dri,': 1.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
               "-----------------------------\n","Total number of item sold :",many,'\n'
               ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
               ,'Thank You For Your Order\n'
               ,"PLEASE COME AGAIN")
         print("ABA : 500 609 384")
         print("AC : 0888905923")
         print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
         print("Power by group 1")
    
elif dri=='j':
        dri=('matcha')
        total=(3*many)     
        print("select sugar level")
        sug=int(input("sugar level :"))
        if 100>= sug >=0:
          print("\n")
          print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
          print("ABA : 500 609 384")
          print("AC : 0888905923")
          print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
          print("Power by group 1")
          print(x)
        else :
             print("!! error !! Try again !!")
             print(x)
elif dri=='k':
    dri=('ice latte')
    total=(3*many)
   
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
   
elif dri=='l':
    dri=('coffee')
    total=(2.5*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
    
elif dri=="m" :
    dri=("strawberry milk")
    total=(3.5*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
elif dri=='n':
    dri=('banana milk')
    total=(3.5*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
    
elif dri=='o':
    dri=('vital water')
    total=(1*many)
    size=input("a.350ml,b.500ml,c.1l :")
    if size=='a':
        size=("350ml") 
        total=(0.5*many)
        print("\n")
        print('',"Drink store\n","cash receipt\n","-----------------------------\n",
              "Order :",dri,': 0.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
              "-----------------------------\n","Total number of item sold :",many,'\n'
              ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
              ,'Thank You For Your Order\n'
              ,"PLEASE COME AGAIN")
        print("ABA : 500 609 384")
        print("AC : 0888905923")
        print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
        print("Power by group 1")
        print(x)
    elif size=='b':
         size=("500ml")
         total=(1.*many)
         print("\n")
         print('',"Drink store\n","cash receipt\n","-----------------------------\n",
               "Order :",dri,': 1 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
               "-----------------------------\n","Total number of item sold :",many,'\n'
               ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
               ,'Thank You For Your Order\n'
               ,"PLEASE COME AGAIN")
         print("ABA : 500 609 384")
         print("AC : 0888905923")
         print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
         print("Power by group 1")
         print(x)
    elif size=='c':
        size=("1l")
        total=(1.5*many)
        print("\n")
        print('',"Drink store\n","cash receipt\n","-----------------------------\n",
              "Order :",dri,': 1.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
              "-----------------------------\n","Total number of item sold :",many,'\n'
              ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
              ,'Thank You For Your Order\n'
              ,"PLEASE COME AGAIN")
        print("ABA : 500 609 384")
        print("AC : 0888905923")
        print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
        print("Power by group 1")
        print(x)
elif dri=='p':
    dri=('oishi')
    total=(1.5*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 1.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=="q" :
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
elif dri=='r':
    dri=('kiwi milk')
    total=(3.5*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date : =13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
elif dri=='s':
    dri=('orange juice')
    total=(2.5*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
   
elif dri=='t':
    dri=('jinro strawberry')
    total=(2*many)
    age=int(input("how old are you :"))
    if 99>=age>=18:
                    total=(2*many)
                    print("\n")
                    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
                      "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
                      "-----------------------------\n","Total number of item sold :",many,'\n'
                      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
                      ,'Thank You For Your Order\n'
                      ,"PLEASE COME AGAIN")
                    print("ABA : 500 609 384")
                    print("AC : 0888905923")
                    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
                    print("Power by group 1")
                    print(x)
    else:
            print("YOU CAN NOT BUY", "\n","TRY AGAIN KID!!")
            print("\n",";(")
            print(x)

    
elif dri=="u" :
     dri=("coconut juice")
     total=(2.5*many)
     sug=int(input("sugar level :"))
     if 100>= sug >=0:
       print("\n")
       print('',"Drink store\n","cash receipt\n","-----------------------------\n",
       "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
       "-----------------------------\n","Total number of item sold :",many,'\n'
       ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
       ,'Thank You For Your Order\n'
       ,"PLEASE COME AGAIN")
       print("ABA : 500 609 384")
       print("AC : 0888905923")
       print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
       print("Power by group 1")
       print(x)
     else :
          print("!! error !! Try again !!")
          print(x)
 
elif dri=='v':
     dri=('grape juice')
     total=(2.5*many)
     sug=int(input("sugar level :"))
     if 100>= sug >=0:
       print("\n")
       print('',"Drink store\n","cash receipt\n","-----------------------------\n",
       "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
       "-----------------------------\n","Total number of item sold :",many,'\n'
       ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
       ,'Thank You For Your Order\n'
       ,"PLEASE COME AGAIN")
       print("ABA : 500 609 384")
       print("AC : 0888905923")
       print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
       print("Power by group 1")
       print(x)
     else :
          print("!! error !! Try again !!")
          print(x)
 
elif dri=='w':
     dri=('almond milk')
     total=(3.5*many)
     print("\n")
     print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,': 3.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
     print("ABA : 500 609 384")
     print("AC : 0888905923")
     print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
     print("Power by group 1")
     print(x)
    
elif dri=='x':
     dri=('soda lemon')
     total=(2.5*many)
     sug=int(input("sugar level :"))
     if 100>= sug >=0:
       print("\n")
       print('',"Drink store\n","cash receipt\n","-----------------------------\n",
       "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
       "-----------------------------\n","Total number of item sold :",many,'\n'
       ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
       ,'Thank You For Your Order\n'
       ,"PLEASE COME AGAIN")
       print("ABA : 500 609 384")
       print("AC : 0888905923")
       print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
       print("Power by group 1")
       print(x)
     else :
          print("!! error !! Try again !!")
          print(x)
     
elif dri=="y" :
    dri=("soda")
    total=(1.5*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
    
elif dri=='z':
    dri=('coca-cola zero sugar')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='a1':
    dri=('coca-cola low fat')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='a2':
    dri=('grape juice')
    total=(3.5*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
elif dri=='a3':
        dri=('green tea')
        total=(2*many)
        sug=int(input("sugar level :"))
        if 100>= sug >=0:
          print("\n")
          print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
          print("ABA : 500 609 384")
          print("AC : 0888905923")
          print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
          print("Power by group 1")
          print(x)
        else :
             print("!! error !! Try again !!")
             print(x)
elif dri=='a4':
            dri=('milo')
            total=(2*many)
            print("\n")
            print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
            print("ABA : 500 609 384")
            print("AC : 0888905923")
            print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
            print("Power by group 1")
            print(x)
elif dri=='a5':
    dri=('chocolate milk')
    total=(3.5*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
elif dri=='a6':
    dri=('lactasoy')
    total=(2*many)
    sug=int(input("sugar level :"))
    if 100>= sug >=0:
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
elif dri=='a7':
    dri=('aloe vera')
    total=(1.5*many)
    x=50
    y=75
    z=100
    print(x,y,z)
    sug=input("sugar level :")
    if sug ==( x,y,z):
      print("\n")
      print('',"Drink store\n","cash receipt\n","-----------------------------\n",
      "Order :",dri,sug,"%",': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
      "-----------------------------\n","Total number of item sold :",many,'\n'
      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
      ,'Thank You For Your Order\n'
      ,"PLEASE COME AGAIN")
      print("ABA : 500 609 384")
      print("AC : 0888905923")
      print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
      print("Power by group 1")
      print(x)
    else :
         print("!! error !! Try again !!")
         print(x)
elif dri=='a8':
    dri=('spy red')
    total=(3*many)
    age=int(input("how old are you :"))
    if 99>=age>=18:
                    total=(3*many)
                    print("\n")
                    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
                      "Order :",dri,': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
                      "-----------------------------\n","Total number of item sold :",many,'\n'
                      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
                      ,'Thank You For Your Order\n'
                      ,"PLEASE COME AGAIN")
                    print("ABA : 500 609 384")
                    print("AC : 0888905923")
                    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
                    print("Power by group 1")
                    print(x)
    else:
            print("YOU CAN NOT BUY", "\n","TRY AGAIN KID!!")
            print("\n",";(")
            print(x)
elif dri=='a9':
    dri=('spy black')
    total=(3*many)
    if 99>=age>=18:
                    total=(3*many)
                    print("\n")
                    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
                      "Order :",dri,': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
                      "-----------------------------\n","Total number of item sold :",many,'\n'
                      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
                      ,'Thank You For Your Order\n'
                      ,"PLEASE COME AGAIN")
                    print("ABA : 500 609 384")
                    print("AC : 0888905923")
                    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
                    print("Power by group 1")
                    print(x)
    else:
            print("YOU CAN NOT BUY", "\n","TRY AGAIN KID!!")
            print("\n",";(")
            print(x)
elif dri=='a10':
    dri=('spy blue')
    total=(3*many)
    if 99>=age>=18:
                    total=(3*many)
                    print("\n")
                    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
                      "Order :",dri,': 3 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
                      "-----------------------------\n","Total number of item sold :",many,'\n'
                      ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
                      ,'Thank You For Your Order\n'
                      ,"PLEASE COME AGAIN")
                    print("ABA : 500 609 384")
                    print("AC : 0888905923")
                    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
                    print("Power by group 1")
                    print(x)
    else:
            print("YOU CAN NOT BUY", "\n","TRY AGAIN KID!!")
            print("\n",";(")
            print(x)
elif dri=='b1':
    dri=('olatte')
    total=(2.5*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,': 2.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='b2':
    dri=('v-active')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date :13/11/22023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='b3':
    dri=('angkor puro')
    total=(1*many)
    size=input("a.350ml,b.500ml,c.1l :")
    if size=='a':
         size=("350ml") 
         total=(0.5*many)
         print("\n")
         print('',"Drink store\n","cash receipt\n","-----------------------------\n",
               "Order :",dri,': 0.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
               "-----------------------------\n","Total number of item sold :",many,'\n'
               ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
               ,'Thank You For Your Order\n'
               ,"PLEASE COME AGAIN")
         print("ABA : 500 609 384")
         print("AC : 0888905923")
         print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
         print("Power by group 1")
         print(x)
    elif size=='b':
          size=("500ml")
          total=(1.*many)
          print("\n")
          print('',"Drink store\n","cash receipt\n","-----------------------------\n",
                "Order :",dri,': 1 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
                "-----------------------------\n","Total number of item sold :",many,'\n'
                ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
                ,'Thank You For Your Order\n'
                ,"PLEASE COME AGAIN")
          print("ABA : 500 609 384")
          print("AC : 0888905923")
          print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
          print("Power by group 1")
          print(x)
    elif size=='c':
         size=("1l")
         total=(1.5*many)
         print("\n")
         print('',"Drink store\n","cash receipt\n","-----------------------------\n",
               "Order :",dri,': 1.5 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
               "-----------------------------\n","Total number of item sold :",many,'\n'
               ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
               ,'Thank You For Your Order\n'
               ,"PLEASE COME AGAIN")
         print("ABA : 500 609 384")
         print("AC : 0888905923")
         print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
         print("Power by group 1")
         print(x)
elif dri=='b4':
    dri=('pocari sweat')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='b5':
    dri=('wurkz')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='b6':
    dri=('bachhus')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL:  +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='b7':
    dri=('dutch milk')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
          "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
          "-----------------------------\n","Total number of item sold :",many,'\n'
          ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
          ,'Thank You For Your Order\n'
          ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='b8':
    dri=('meiji')
    total=(2.2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2.2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date :13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='b9':
    dri=('angkor milk')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='b10':
    dri=('kirisu milk')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11//2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='c1':
    dri=('samurai')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='c2':
    dri=('ize')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11//2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='c3':
    dri=('vigor')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
elif dri=='c4':
    dri=('7-up')
    total=(2*many)
    print("\n")
    print('',"Drink store\n","cash receipt\n","-----------------------------\n",
         "Order :",dri,': 2 x',many,"pc" ,"\n" ,"Total :",total,'$\n',
         "-----------------------------\n","Total number of item sold :",many,'\n'
         ,"date : 13/11/2023\n",'costumer:',name,"\n","TEL: +885",num,"\n","Address :",add,"\n"
         ,'Thank You For Your Order\n'
         ,"PLEASE COME AGAIN")
    print("ABA : 500 609 384")
    print("AC : 0888905923")
    print("number for contact us :\n * 090883400 *\n * 098718216 *\n * 0888905923 *")
    print("Power by group 1")
    print(x)
else:
    dri=("DON'T HAVE INSTOCK")
    print("TRY AGAIN ^^")
    print(x)
    


        
