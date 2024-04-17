i = 0
while i < 3:
    gmail = input('Enter your gmail: ')
    password = input('Enter your password: ')

    if gmail == 'user' and password == '123':
        print('You have successfully logged in.')
        print("_________________Welcome to DELULU Personal Finance Tracker!__________________")
        print("______________________________________________________________________________\n")
        m=float(input("Enter your money : "))
        s = float(input("Enter your Salary : "))
        ex_h= float(input("Enter your expence on house : "))
        ex_f= float(input("Enter your expence on meals : "))
        ex_t= float(input("Enter your expence on transportation : "))
        ex_o= float(input("Enter your expence on others : "))
        ex= ex_h + ex_f + ex_t + ex_o
        inc = float(input("Enter your income : "))
        print("___________________________________________\n")
        def Total():
            y = m - ex + inc + t
            print("Your salary after tax money is : ",t,'$')
            print("Your total money : ",y,'$')
        if  0<=s<=375:
              t=s
              Total()
        elif 375<s<=500:
              t=s-s*5/100
              Total()
        elif 500<s<=2125:
              t=s-s*10/100
              Total()
        elif 2125<s<=3125:
              t=s-s*15/100
              Total()
        elif s>3125:
              t=s-s*20/100
              Total()
        else:
           print(" Please Enter your real salary")
        y = m - ex + inc + t
        print("____________________________________________\n")
         
        print("__________Rules of manage your money________\n")
        print("*Rule 1: 50%,30%,20%\n")
        print("Needs\t|\tWants\t|\tSavings\t|")
        print("_________________________________")
        print("50%\t\t|\t30%\t\t|\t20%\t\t|\n")
        print("*Rule 2: 40%,30%,20%,10%\n")
        print("Needs\t|\tWants\t|\tSavings\t|\tInvestment\t|")
        print("_________________________________________________")
        print("40%\t\t|\t30%\t\t|\t20%\t\t|\t10%\t\t\t|\n")
        print("*Rule 3: 40%,20%,40%\n")
        print("Needs\t|\tWants\t|\tSave&Investment\t|")
        print("_________________________________________")
        print("40%\t\t|\t20%\t\t|\t40%\t\t\t\t|\n")
        sav= t-ex
        a = t*(50/100)   
        b = t*(30/100)
        c = t*(20/100)
        d = t*(40/100)
        f = t*(10/100)
        e = sav-f
        def total_Rule1():
            print("Your Needs is : ",ex,'$')
            print("Your Wants is : ",ex_o,'$')
            print("Your Saving is : ",sav,'$')
            print("Your total money : ",y,'$')
        def total_Rule2_3():
            print("Your Needs is : ",ex,'$')
            print("Your Wants is : ",ex_o,'$')
            print("Your Saving is : ",sav)
            print("Your money for investment is : ",f,'$')
            print("Your total money : ",y,'$') 
        Ch=int(input("Choose one rule of manage your money : "))
        if Ch==1:
             if (ex<=a and ex_o<=b and sav>=c) :
                 total_Rule1()
             else:
                 total_Rule1()
        elif Ch==2:
             if (ex<=d and ex_o<=b and sav>=c ):
                 total_Rule2_3()
             else:
                 total_Rule2_3()
        elif Ch==3:
             if (ex<=d and ex_o<=c and sav>=d):
                 total_Rule2_3()
             else:
                 total_Rule2_3() 
        else: 
            print("___________Please choose 1,2,3___________")
        print("__________________Investment__________________")
        invest=['c.Certificates_of_deposit','b.Bonds','f.Funds','s.Stocks','r.Real_estate']
        print("c : Certificates_of_deposit\nA certificate of deposit, or CD, is a federally insured savings account that offers a fixed interest rate for a defined period of time.")
        print("b : Bonds\nBonds can offer a relatively safe form of fixed-income to their investors. Lower risk bonds tend to pay lower interest than higher risk bonds, including government or corporate bonds. ")
        print("f : Funds\nFunds pool money from shareholders to invest in a portfolio of assets like stocks or bonds. The investing term “funds” often refers to mutual funds.")
        print("s : Stocks\nA stocks represents a share of ownership in a company.")
        print("r : Real_estate\nInvestors who already have a healthy investment portfolio and are looking for further diversification, or are willing to take more risk for higher returns.")
        inv_ch = str(input("Choose your investment : "))
        def information_1(Bestfor):
            print("Best for: " + Bestfor)
        def information_2(wheretobuy):
            print("Where to buy: " + wheretobuy)
        if inv_ch=='c':
             print(invest[1])
             information_1(" A CD is for money you know you’ll need at a fixed date in the future (e.g., a home down payment or a wedding).")
             information_2("CDs are sold based on term length, and the best rates are generally found at online banks and credit unions.")
        elif inv_ch=='b':
             print(invest[2])
             bond_ch=['1.goverment_bonds','2.Corporate bonds']
             print("There are two type of Bonds :")
             for Type_Bonds in bond_ch:
                 print(Type_Bonds)
             bond_ch=int(input("Choose one of these Bonds : "))
             if bond_ch==1:
                 information_1("Conservative investors who would prefer to see less volatility in their portfolio.")
                 information_2("government bonds: You can buy individual bonds or bond funds, which hold a variety of bonds to provide diversification, from a broker or directly from the underwriting investment bank or the U.S. government.")
             elif bond_ch==2:
                 information_1("Investors looking for a fixed-income security with potentially higher yields than government bonds, and willing to take on a bit more risk in return.")
                 information_2("corporate bonds: Similar to government bonds, you can buy corporate bond funds or individual bonds through an investment broker.")
             else:
                 print("Please choose 1-2")
        elif inv_ch=="f":
             print(invest[2])
             fund_ch=['1.Money_market_funds','2.Mutual funds','3.Index funds','4.Exchange-traded funds']
             print("There are four types of Funds : ")
             for Type_Funds in fund_ch:
                 print(Type_Funds)
             fund_ch=int(input("Choose one of these Fonds : "))
             if fund_ch==1:
                 information_1("Money you may need soon that you’re willing to expose to a little more market risk. ")
                 information_2("Money market mutual funds can be purchased directly from a mutual fund provider or a bank(you’ll need to open a brokerage account).")
             elif fund_ch==2:
                 information_1("If you’re saving for retirement or another long-term goal, mutual funds are a convenient way to get exposure to the stock market’s superior investment returns without having to purchase and manage a portfolio of individual stocks.")
                 information_2("Mutual funds are available directly from the companies that manage them, as well as through discount brokerage firms.")
             elif fund_ch==3:
                 information_1("Index mutual funds are some of the best investments available for long-term savings goals.")
                 information_2("Index funds are available directly from fund providers or through a discount broker. See our post on how to invest in index funds.")  
             elif fund_ch==4:
                 information_1("Like index funds and mutual funds, ETFs are a good investment if you have a long time horizon.")
                 information_2("ETFs have ticker symbols like stocks and are available through brokerages. (See our roundup of best brokers for ETF investing.) Robo-advisors also use ETFs to construct client portfolios.")
             else:
                 print("Please choose 1-2-3-4")
        elif inv_ch=='s':
             print(invest[3])
             stock_ch=['1.Individual_stocks','2.Dividend stocks']
             print("There two types of Stocks :")
             for Type_Stock in stock_ch:
                 print(Type_Stock)
             stock_ch=int(input("Choose one of these Stocks : "))
             if stock_ch==1:
                 information_1("Investors with a well-diversified portfolio who are willing to take on a little more risk.")
                 information_2("An easy way to buy stocks is through an online broker. ")
             elif stock_ch==2:
                 information_1("Any investor, from first-timer to retiree, though there are specific types of dividend stocks that may be better depending on where you are in your investing journe")
                 information_2("Similar to others on this list, the easiest way to buy dividend stocks is through an online broker. See our piece on high-dividend stocks and how to invest in them for more information.")
             else:
                 print("Please choose 1-2")
        elif inv_ch=='r':
             print(invest[4])
             information_1("Investors who already have a healthy investment portfolio and are looking for further diversification, or are willing to take more risk for higher returns. Real estate investments are highly illiquid, so investors shouldn’t put into an investment any money they may need to access quickly.")
             information_2("Some REITs can be purchased on the public stock market through an online stockbroker")
        else:
             print("Please write \nc for Certificates_of_deposit \nb for Bonds \nf for Funds \ns for Stocks \nr for Real_estate") 
        print("____________________________________________________\n")
        print("Thank you for using DELULU Personal Finance Tracker ")    
            
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        i += 1
        continue     
            
            
            
