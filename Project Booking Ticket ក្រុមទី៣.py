def funtion(x,y):
     print("---------------------------------------------------------------------")
     print("              Welcome To Maflix Cinema                             ")
     print("The largest cinema in Cambodia that can accommodate up to 400 spectators with a house. ")
     area=x*y
     print("Cinema is a area:",area,"m^2.")
     print("                                                                                        ")
     print("     Please complete Your about!")           
funtion(2,500)
print("                                                                                               ")
name=input("Enter your name: ")                          
sex=str(input("Enter your sex: "))
age=int(input("Enter your age: "))
gmail=input("Enter Your gmail: ")
num=int(input("Enter your phone number: "))
print(" All the movie let show 20/11/2023 until 24/11/2023.")
date=input("Enter Date your booking Ticket movie: ")
print("                                                                            ")
print("Please you booking Movie Tickets under!")

print("                                                                       ")
print("The movie")
Movie=['1: FREE BIRDS(ACTION)'
       ,'2: MARIO BROS(ADVANTURE)'
       ,'3: KUNG FU PANDA(ACTION)'
       ,'4: TITANIC(HORROR)'
       ,'5: FIST FIGHT COMEDY(Camedy)'
       ,'6: THE BFG(Advanture)'
       ,'7: KING KONG(ADVANTURE)'
       ,'8: AVATAR(ADVANTURE)'
       ,'9: SPAYDER MAN(ACTION)'
       ,'10: CITY OF EMBER(Camedy)'
       ,'11: WEDNESDAY(HORROR)'
       ,'12: THE LAST OF US(HORROR)'
       ,'13: I AM GROOT(ADVANTURE)'
       ,'14: SUPERMAN(ACTION)'
       ,'15: WATER WORLD(HORROR)'
       ,'16: JIM BUTTON AND LUKE THE EBGINE(ADVANTURE)'
       ,'17: JURASSIC WORLD(ADVANTURE)'
       ,'18: BEAST(ACTION)'
       ,'19: HELLBOY(ACTION)'
       ,'20: WILD MEN(ACTION)'
       ,'21: JONH WICK(ACTION)'
       ,'22: SERENITY(HORROR)'
       ,'23: STEALTH(HORROR)'
       ,'24: SAMARITAN(ADVANTURE)'
       ,'25: TURBO KID(camedy)'
       ,'26: FAST X(ACTION)'
       ,'27: THE NUN II(HORROR)'
       ,'28: NOWHERE(hORROR)'
       ,'29: THE MEG(Camedy)'
       ,'30: COBWEB(HORROR)']
print(Movie,end=",")
print("                                                                      ")
print("                                                                      ")
print("Please chose Type Movie (1=Comedy, 2=Advanter, 3=horror, 4=Action)")
typ=int(input("Comedy, Advanter, Horror, Action: "))
if(typ==1):
    print(" 5: FIST FIGHT COMEDY(Camedy), 10: CITY OF EMBER(Camedy)")
    print("29: THE MEG(Camedy),25: TURBO KID(camedy)")
elif(typ==2):
    print("2: MARIO BROS(ADVANTURE), 7: KING KONG(ADVANTURE)") 
    print("8: AVATAR(ADVANTURE), 6: THE BFG(Advanture)") 
    print("16: JIM BUTTON AND LUKE THE EBGINE(ADVANTURE), 24: SAMARITAN(ADVANTURE)")
    print("17: JURASSIC WORLD(ADVANTURE), 13: I AM GROOT(ADVANTURE)")
elif(typ==3):
    print("4: TITANIC(HORROR), 11: WEDNESDAY(HORROR), 12: THE LAST OF US(HORROR)")
    print("15: WATER WORLD(HORROR), 22: SERENITY(HORROR), 23: STEALTH(HORROR)")
    print("27: THE NUN II(HORROR), 28: NOWHERE(hORROR), 30: COBWEB(HORROR)")
elif(typ==4):
    print("1: FREE BIRDS(ACTION), 3: KUNG FU PANDA(ACTION), 9: SPAYDER MAN(ACTION)")
    print("14: SUPERMAN(ACTION), 18: BEAST(ACTION), 19: HELLBOY(ACTION)")
    print("20: WILD MEN(ACTION), 21: JONH WICK(ACTION), 26: FAST X(ACTION)")
print("                                                                           ")
print("                   Please check Time show Movie!!                            ")
print("                                                                           ")
print("# Theatre1 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 20/11/2023 !!!")
print("Theatre1 show: 1: FREE BIRDS(ACTION),  2: MARIO BROS(ADVANTURE)")
print("                                                                           ")
print("# Theatre2 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 20/11/2023 !!!")    
print("Theatre2 show: 3: KUNG FU PANDA(ACTION),  4: TITANIC(HORROR)")
print("                                                                           ")
print("# Theatre3 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 20/11/2023 !!!")
print("Theatre3 show: 5: FIST FIGHT COMEDY(Camedy),  6: THE BFG(Advanture)")
print("                                                                           ")
print("# Theatre1 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 21/11/2023 !!!")
print("Theatre1 show: 7: KING KONG(ADVANTURE),  8: AVATAR(ADVANTURE), ")
print("                                                                           ")
print("# Theatre2 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 21/11/2023 !!!") 
print("Theatre2 show: 9: SPAYDER MAN(ACTION),  10: CITY OF EMBER(Camedy)")
print("                                                                           ")
print("# Theatre3 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 21/11/2023 !!!")
print("Theatre3 show: 11: WEDNESDAY(HORROR),  12: THE LAST OF US(HORROR)")
print("                                                                           ")
print("# Theatre1 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 22/11/2023 !!!")
print("Theatre1 show: 13: I AM GROOT(ADVANTURE),  14: SUPERMAN(ACTION)")
print("                                                                           ")
print("# Theatre2 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 22/11/2023 !!!") 
print("Theatre2 show: 15: WATER WORLD(HORROR), 16: JIM BUTTON AND LUKE THE EBGINE(ADVANTURE)")
print("                                                                           ")
print("# Theatre3 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 22/11/2023 !!!")
print("Theatre3 show: 17: JURASSIC WORLD(ADVANTURE),  18: BEAST(ACTION)")
print("                                                                           ")
print("# Theatre1 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 23/11/2023 !!!")
print("Theatre1 show: 19: HELLBOY(ACTION),  20: WILD MEN(ACTION)")
print("                                                                           ")
print("# Theatre2 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 23/11/2023 !!!")
print("Theatre2 show: 21: JONH WICK(ACTION),  22: SERENITY(HORROR)")
print("                                                                           ")
print("# Theatre3 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 23/11/2023 !!!")
print("Theatre3 show: 23: STEALTH(HORROR),  24: SAMARITAN(ADVANTURE)")
print("                                                                           ")
print("# Theatre1 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 24/11/2023 !!!")
print("Theatre1 show:  25: TURBO KID(camedy),  26: FAST X(ACTION)")
print("                                                                           ")
print("# Theatre2 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 24/11/2023 !!!")
print("Theatre2 show: 27: THE NUN II(HORROR),  28: NOWHERE(hORROR)")
print("                                                                           ")
print("# Theatre3 show at 5:00PM to 7:45 and 8:00PM to 9:45PM on 24/11/2023 !!!")
print("Theatre3 show: 29: THE MEG(Camedy),   30: COBWEB(HORROR)")
print("                                                                                               ")

theatre=int(input("Which Theatre(Enter: 1=Theatre1 , 2=Theatre2 , 3=Theatre3) do you want to watch movie: "))
if(theatre==1):
    print("Theatre 1 in floor1 room F1")
if(theatre==2):
    print("Theatre 2 in floor2 room F2")
if(theatre==3):
    print("Theatre 3 in floor3 room F3")
print("                                                                         ")
print("Please you chose chair !!")
chair=['chair A=5$'
      ,'chair B=4$'
      ,'chair C=3$']
print(chair)
print("chair 5$")
n=3
for i in range(n):
   for j in range(1,5):
         print("5$",end="") 
         for k in range(1,4):
             print("5$",end="")
   print()
print("chair 4$")
n=4
for i in range(n):
   for j in range(1,5):
         print("4$",end="") 
         for k in range(1,4):
             print("4$",end="")
   print()
print(" chair 3$")
n=5
for i in range(n):
   for j in range(1,5):
         print("3$",end="") 
         for k in range(1,4):
             print("3$",end="")
   print()


print("                                                                                      ")
print("All the  Movie start show at Time!. ")

print("                                                                                         ")
ti=int(input("Please you chose booking Movie follow number of Movie Tickets) for you want:  ​"))
if (ti==1):
    print("Movie FREE BIRDS(ACTION). ")
elif (ti==2):
    print("Movie MARIO BROS(ADVANTURE).")
elif (ti==3):
    print("Movie KUNG FU PANDA(ACTION). ")
elif (ti==4):
    print("Movie TITANIC(HORROR).")
elif (ti==5):
    print("Movie FIST FIGHT COMEDY(ACTION). ")
elif (ti==6):
    print("Movie THE BFG(Advanture). ")    
elif (ti==7):
    print("Movie KING KONG(ADVANTURE). ")    
elif (ti==8):
    print("Movie AVATAR(ADVANTURE). ")
elif (ti==9):
    print("Movie SPAYDER MAN(ACTION). ")    
elif (ti==10):
    print("Movie CITY OF EMBER(HORROR). ")    
elif (ti==11):
    print("Movie WEDNESDAY(HORROR). ")  
elif (ti==12):
    print("Movie THE LAST OF US(HORROR). ")
elif (ti==13):
    print("Movie I AM GROOT(ADVANTURE). ")    
elif (ti==14):
    print("Movie SUPERMAN(ACTION). ")      
elif (ti==15):
    print("Movie WATER WORLD(HORROR). ")    
elif (ti==16):
    print("Movie JIM BUTTON AND LUKE THE EBGINE(ADVANTURE).")    
elif (ti==17):
    print("Movie JURASSIC WORLD(ADVANTURE). ")    
elif (ti==18):
    print("Movie BEAST(ACTION). ")        
elif (ti==19):
    print("Movie HELLBOY(ACTION). ")      
elif (ti==20):
    print("Movie WILD MEN(ACTION). ")      
elif (ti==21):
    print("Movie JONH WICK(ACTION). ")      
elif (ti==22):
    print("Movie SERENITY(HORROR).")      
elif (ti==23):
    print("Movie STEALTH(HORROR). ")      
elif (ti==24):
    print("Movie SAMARITAN(ADVANTURE).")      
elif (ti==25):
    print("Movie TURBO KID(ACTION). ")      
elif (ti==26):
    print("Movie FAST X(ACTION). ")      
elif (ti==27):
    print("Movie THE NUN II(HORROR). ")      
elif (ti==28):
    print("Movie NOWHERE(hORROR). ")      
elif (ti==29):
    print("Movie THE MEG(HORROR). ")      
elif (ti==30):
    print("Movie COBWEB(HORROR). ")
if 1<=ti<=30:
    n=int(input("How many tickets do you want to booking?: ",))
    ch=int(input("Please chose  chair(Enter 5=5$,4=4$,3=3$):",))
    total=n*ch
    if ch==5:
        print("Your chair is 5$")
    elif ch==4:
         print("Your chair is 4$ ")
    elif ch==3:
         print("Your chair is 3$ ")
    else:
        print("Please you enter number chair again. Note you can enter number 5 or 4 or 3 !")
    if 1<=n<=400:
        
        print("You Pay Total is : ",total," $")
        
        print("                                                                                                  ")       
        class BankAccount:
            def __init__(self):
                self.balance = 0
                print("Hello! Welcome to the Deposit!! ")

            def deposit(self):
                amount = float(input("Enter amount to be deposited Number Accoount ABA: (123456789): "))
                self.balance += amount
                print("\nAmount Deposited : ", amount,"$")

        s = BankAccount()
        s.deposit()  
        
        print("------------------------------------------------------------------------------------------------")  
        print("                                                                                                       ")
        print("                     Maflix Cinema                                 ")
        print("                                                                                                       ")
        print("            Cinema at AEON MALL 4 in Phnom Penh                    ")
        print("                                                                                                       ")
        print("                    Your about!                                    ")
        print("                 ____________________                                                                  ")
        print("                                                                                                       ")
        print("  Your Name          :                              ",name,".")   
        print("                                                                                                       ")
        print("  Your age           :                              ",age,"years old.")
        print("                                                                                                       ")
        print("  You are            :                              ",sex,".")
        print("                                                                                                       ")
        print("  Your phone number  :                              ",num,".")
        print("                                                                                                ")
        print("  Your Gmail         :                              ",gmail,".")
        print("                                                                                                ")
        print("  Date you booking   :                              ",date,".")
        print("                                                                                                ")
        print("  Your Booking Movie  :                             ",ti,".")
        print("                                                                                                ")
        print("  Your booking Ticket :                             ",n,"Ticket.")
        print("                                                                                                ")
        print("  Your total pay      :                             ",total,"$.")
        print("                                                                                                ")
        print("  Your Theatre        :                             ",theatre,".")
        print("                                                                                                ")
        print("  Your chair          :                             ",ch,"$.")
        print("________________________________________________________________________________________________")
        print("      The all Movie start at 12/11/2023. ")
        print("      You can pay to ABA: 123456789 ")
        print("      Please keep the invoices you paid in ABA and Reciept to be able to enter the cinema.!!")
        print("      Thank you for booking Movie Tickets from Maflix!!!")
        print("      you not Cancel the tickets                                 ")
        print("-------------------------------------------------------------------------------------------------")
         
    else:
         print("Error system",n)
else:
    print("Error system")
if (ti==1):
    print("Verify You are booking the Movie FREE BIRDS(ACTION).")
elif (ti==2):
    print("Verify You are booking the Movie MARIO BROS(ADVANTURE).")
elif (ti==3):
    print("Verify You are booking the Movie KUNG FU PANDA(ACTION).")
elif (ti==4):
    print("Verify You are booking the Movie TITANIC(HORROR). ")
elif (ti==5):
    print("Verify You are booking the Movie FIST FIGHT COMEDY(ACTION). ")
elif (ti==6):
    print("Verify You are booking the Movie THE BFG(Advanture). ")    
elif (ti==7):
    print("Verify You are booking the Movie KING KONG(ADVANTURE). ")    
elif (ti==8):
    print("Verify You are booking the Movie AVATAR(ADVANTURE).")
elif (ti==9):
    print("Verify You are booking the Movie SPAYDER MAN(ACTION).")    
elif (ti==10):
    print("Verify You are booking the Movie CITY OF EMBER(HORROR).")    
elif (ti==11):
    print("Verify You are booking the Movie WEDNESDAY(HORROR).")  
elif (ti==12):
    print("Verify You are booking the Movie THE LAST OF US(HORROR).")
elif (ti==13):
    print("Verify You are booking the Movie I AM GROOT(ADVANTURE).")    
elif (ti==14):
    print("Verify You are booking the Movie SUPERMAN(ACTION). ")      
elif (ti==15):
    print("Verify You are booking the Movie WATER WORLD(HORROR). ")    
elif (ti==16):
    print("Verify You are booking the Movie JIM BUTTON AND LUKE THE EBGINE(ADVANTURE).")    
elif (ti==17):
    print("Verify You are booking the Movie JURASSIC WORLD(ADVANTURE). ")    
elif (ti==18):
    print("Verify You are booking the Movie BEAST(ACTION). ")        
elif (ti==19):
    print("Verify You are booking the Movie HELLBOY(ACTION).")      
elif (ti==20):
    print("Verify You are booking the Movie WILD MEN(ACTION).")      
elif (ti==21):
    print("Verify You are booking the Movie JONH WICK(ACTION).")      
elif (ti==22):
    print("Verify You are booking the Movie SERENITY(HORROR). ")      
elif (ti==23):
    print("Verify You are booking the Movie STEALTH(HORROR). ")      
elif (ti==24):
    print("Verify You are booking the Movie SAMARITAN(ADVANTURE). ")      
elif (ti==25):
    print("Verify You are booking the Movie TURBO KID(ACTION). ")      
elif (ti==26):
    print("Verify You are booking the Movie FAST X(ACTION). ")      
elif (ti==27):
    print("Verify You are booking the Movie THE NUN II(HORROR). ")      
elif (ti==28):
    print("Verify You are booking the Movie NOWHERE(hORROR). ")      
elif (ti==29):
    print("Verify You are booking the Movie THE MEG(HORROR). ")      
elif (ti==30):
    print("Verify You are booking the Movie COBWEB(HORROR).")
print("---------------------------------------------------------------------------------------------")