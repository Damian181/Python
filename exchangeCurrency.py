import os
from termcolor import colored
"""
PROJECT: Exchange Currency
NAME: Damian Niechoda
FROM: Poland,Ostrów Lubelski
https://www.linkedin.com/in/damian-niechoda-a93805260/
https://github.com/Damian181
"""



def main():

    print(colored("welcome to Polish PLN exchange office\n", "green"))

    while True:

        print("====currency actual offer====")
        print("============Buy==============")
        print(colored("1 Euro = 4.6456 PLN", "green"))
        print(colored("1 U.S Dolar = 4.1885 PLN", "green"))
        print(colored("1 Swis Franc = 4.6957 PLN", "green"))
        print(colored("1 British Pound = 5.2470 PLN\n", "green"))
        print("============Sell===============")
        print(colored("1 Euro = 4.5967 PLN", "green"))
        print(colored("1 U.S Dolar = 4.1803 PLN", "green"))
        print(colored("1 Swis Franc = 4.6870 PLN", "green"))
        print(colored("1 British Pound = 5.2317 PLN\n", "green"))

        try:
            ask = int(input("type 1 to buy, 2 to sale, 3 to exchange other currency: "))
            clear_terminal()
            if ask == 1:
                print("===============================")
                buy = int(input("How many do you buy? "))
                print("===============================")
                if buy < 0:
                      wrong_input()
                      print("===============================")
                elif buy > 0:
                      print(currency_buy(buy))

            elif ask == 2:
                print("===============================")
                sell = int(input("How many do you sell? "))
                print("===============================")
                if sell < 0:
                      wrong_input()
                      print("===============================")
                elif sell > 0:
                    print(currency_sell(sell))
            elif ask == 3:
                other_currency()
            else:
                wrong_input()
        except ValueError:
                clear_terminal()
                wrong_input()




def clear_terminal():
     os.system('cls||clear')

def wrong_input():
     print("===============================")
     print(colored("wrong input", "red"))
     print("===============================")

#BUY

def currency_buy(n):

    print(colored("Euro type 1", "green"))
    print(colored("U.S Dolar type 2", "green"))
    print(colored("Swis Franc type 3", "green"))
    print(colored("British Pound type 4", "green"))
    print("===============================")


    buy = int(input("What currency do you want to buy?: "))
    if buy == 1:
            clear_terminal()
            print("===============================")
            final = n * 4.6456
            print(colored(f"You buy {n} Euro for {final:.2f} PLN", "green"))
            return final

    elif buy == 2:
            clear_terminal()
            print("===============================")
            final = n * 4.1885
            print(colored(f"You buy {n} U.S Dolar for {final:.2f} PLN", "green"))
            return final


    elif buy == 3:
            clear_terminal()
            print("===============================")
            final = n * 4.6957
            print(colored(f"You buy {n} Swis Franc for {final:.2f} PLN", "green"))
            return final

    elif buy == 4:
            clear_terminal()
            print("===============================")
            final = n * 5.2470
            print(colored(f"You buy {n} British Pound for {final:.2f} PLN", "green"))
            return final

    else:
        wrong_input()


#SELL

def currency_sell(n):

    print(colored("Euro type 1", "green"))
    print(colored("U.S Dolar type 2", "green"))
    print(colored("Swis Franc type 3", "green"))
    print(colored("British Pound type 4", "green"))
    print("===============================")

    sell = int(input("What currency do you want to sell?: "))
    if sell == 1:
        clear_terminal()
        print("===============================")
        final = n * 4.5967
        print(colored(f"You sell {n} Euro for {final:.2f} PLN", "green"))
        return final

    elif sell == 2:
        clear_terminal()
        print("===============================")
        final = n * 4.1803
        print(colored(f"You sell {n} U.S Dolar for {final:.2f} PLN", "green"))
        return final

    elif sell == 3:
        clear_terminal()
        print("===============================")
        final = n * 4.6870
        print(colored(f"You sell {n} Swis Franc for {final:.2f} PLN", "green"))
        return final

    elif sell == 4:
        clear_terminal()
        print("===============================")
        final = n * 5.2317
        print(colored(f"You sell {n} British Pound for {final:.2f} PLN", "green"))
        return final

    else:
        wrong_input()



def other_currency():#===============================================================================


    print(colored("1 - Sell", "green"))
    print(colored("2 - Buy", "green"))
    chose = int(input("What you gona do?: "))
    if chose == 1:
        clear_terminal()
        sell_sell()
    elif chose == 2:
        clear_terminal()
        buy_buy()
    else:
        wrong_input()




def sell_sell():
    print(colored("1 = Euro", "green"))
    print(colored("2 = U.S Dollar", "green"))
    print(colored("3 = Swiss Franc", "green"))
    print(colored("4 = British Pound", "green"))

    sell1 = int(input("What currency do you want to sell?: "))
    if sell1 == 1:
        print("===============================")
        clear_terminal()
        sell = int(input("How many do you sell?: "))
        if sell > 0:
            print(currency_sell_euro(sell))
        elif sell <= 0:
            wrong_input()

    elif sell1 == 2:
        print("===============================")
        clear_terminal()
        sell = int(input("How many do you sell?: "))
        if sell > 0:
            print(currency_sell_usdollar(sell))
        elif sell <= 0:
            wrong_input()

    elif sell1 == 3:
        print("===============================")
        clear_terminal()
        sell = int(input("How many do you sell?: "))
        if sell > 0:
            print(currency_sell_swisfranc(sell))
        elif sell <= 0:
            wrong_input()

    elif sell1 == 4:
        print("===============================")
        clear_terminal()
        sell = int(input("How many do you sell?: "))
        if sell > 0:
            print(currency_sell_britishpound(sell))
        elif sell <= 0:
            wrong_input()

    else:
        wrong_input()



def buy_buy():
    print(colored("1 = Euro", "green"))
    print(colored("2 = U.S Dollar", "green"))
    print(colored("3 = Swiss Franc", "green"))
    print(colored("4 = British Pound", "green"))

    buy1 = int(input("What currency do you want to buy?: "))
    if buy1 == 1:
        print("===============================")
        clear_terminal()
        buy = int(input("How many do you buy?: "))
        if buy > 0:
            print(currency_buy_euro(buy))
        elif buy <= 0:
            wrong_input()

    elif buy1 == 2:
        print("===============================")
        clear_terminal()
        buy = int(input("How many do you buy?: "))
        if buy > 0:
            print(currency_buy_usdollar(buy))
        elif buy <= 0:
            wrong_input()

    elif buy1 == 3:
        print("===============================")
        clear_terminal()
        buy = int(input("How many do you buy?: "))
        if buy > 0:
            print(currency_buy_swisfranc(buy))
        elif buy <= 0:
            wrong_input()

    elif buy1 == 4:
        print("===============================")
        clear_terminal()
        buy = int(input("How many do you buy?: "))
        if buy > 0:
            print(currency_buy_britishpound(buy))
        elif buy <= 0:
            wrong_input()

    else:
        wrong_input()




#SELL============================================================================================
def currency_sell_euro(n):
    print(colored("1 = U.S Dollar", "green"))
    print(colored("2 = Swiss Franc", "green"))
    print(colored("3 = British Pound", "green"))
    currency = int(input("For What currency do you want to sell?: "))

    #1 euro = 1.0924 us dolar
    if currency == 1:
        print("===============================")
        clear_terminal()
        final = 1.0924 * n
        print(colored(f"You sell {n} Euro for {final:.2f} U.S Dolar", "green"))
        return final

    #1 euro = 0.9774 swis franc
    elif currency == 2:
        print("===============================")
        clear_terminal()
        final = 0.9766 * n
        print(colored(f"You sell {n} Euro for {final:.2f} Swiss Franc", "green"))
        return final

    #1 euro = 0.8685 british pound
    elif currency == 3:
        print("===============================")
        clear_terminal()
        final = 0.8680 * n
        print(colored(f"You sell {n} Euro for {final:.2f} British Pound", "green"))
        return final

    else:
        wrong_input()



def currency_sell_usdollar(n):
    print(colored("1 = Euro", "green"))
    print(colored("2 = Swiss Franc", "green"))
    print(colored("3 = British Pound", "green"))
    currency = int(input("For What currency do you want to sell?: "))

    #1 us dolar = 0.9152 euro
    if currency == 1:
        print("===============================")
        clear_terminal()
        final = 0.9152 * n
        print(colored(f"You sell {n} U.S Dollar for {final:.2f} Euro", "green"))
        return final

    #1 us dolar = 0.8928 swis franc
    elif currency == 2:
        print("===============================")
        clear_terminal()
        final = 0.8928 * n
        print(colored(f"You sell {n} U.S Dollar for {final:.2f} Swiss Franc", "green"))
        return final

    #1 us dolar = 0.7981 british pound
    elif currency == 3:
        print("===============================")
        clear_terminal()
        final = 0.7981 * n
        print(colored(f"You sell {n} U.S Dollar for {final:.2f} British Pound", "green"))
        return final

    else:
        wrong_input()



def currency_sell_swisfranc(n):
    print(colored("1 = Euro", "green"))
    print(colored("2 = U.S Dollar", "green"))
    print(colored("3 = British Pound", "green"))
    currency = int(input("For What currency do you want to sell?: "))

    #1 swis franc = 1.0232 euro
    if currency == 1:
        print("===============================")
        clear_terminal()
        final = 1.0232 * n
        print(colored(f"You sell {n} Swiss Franc for {final:.2f} Euro", "green"))
        return final

    #1 swis franc = 1.1194 us dollar
    elif currency == 2:
        print("===============================")
        clear_terminal()
        final = 1.1194 * n
        print(colored(f"You sell {n} Swiss Franc for {final:.2f} U.S Dollar", "green"))
        return final

    #1 swis franc = 1.1190 british pound
    elif currency == 3:
        print("===============================")
        clear_terminal()
        final = 1.1190 * n
        print(colored(f"You sell {n} Swiss Franc for {final:.2f} British Pound", "green"))
        return final

    else:
        wrong_input()



def currency_sell_britishpound(n):
    print(colored("1 = Euro", "green"))
    print(colored("2 = Swiss Franc", "green"))
    print(colored("3 = U.S Dollar", "green"))
    currency = int(input("For What currency do you want to sell?: "))

    #1 british pound = 1.1515 euro
    if currency == 1:
        print("===============================")
        clear_terminal()
        final = 1.1515 * n
        print(colored(f"You sell {n} British Pound for {final:.2f} Euro", "green"))
        return final

    #1 british pound = 1.1190 swis franc
    elif currency == 2:
        print("===============================")
        clear_terminal()
        final = 1.1190 * n
        print(colored(f"You sell {n} British Pound for {final:.2f} Swiss Franc", "green"))
        return final

    #1 british pound = 1.2534 us dollar
    elif currency == 3:
        print("===============================")
        clear_terminal()
        final = 1.2530 * n
        print(colored(f"You sell {n} British Pound for {final:.2f} U.S Dollar", "green"))
        return final

    else:
        wrong_input()



#BUY=============================================================================================
def currency_buy_euro(n):
    print(colored("1 = U.S Dollar", "green"))
    print(colored("2 = Swiss Franc", "green"))
    print(colored("3 = British Pound", "green"))
    currency = int(input("For What currency do you want to buy?: "))

    #1 euro = 1.0928 us dolar
    if currency == 1:
        print("===============================")
        clear_terminal()
        final = 1.0928 * n
        print(colored(f"You buy {n} Euro for {final:.2f} U.S Dollar", "green"))
        return final

    #1 euro = 0.9774 swis franc
    elif currency == 2:
        print("===============================")
        clear_terminal()
        final = 0.9774 * n
        print(colored(f"You buy {n} Euro for {final:.2f} Swiss franc", "green"))
        return final


    #1 euro = 0.8685 british pound
    elif currency == 3:
        print("===============================")
        clear_terminal()
        final = 0.8685 * n
        print(colored(f"You buy {n} Euro for {final:.2f} British Pound", "green"))
        return final

    else:
        wrong_input()



def currency_buy_usdollar(n):
    print(colored("1 = Euro", "green"))
    print(colored("2 = Swiss Franc", "green"))
    print(colored("3 = British Pound", "green"))
    currency = int(input("For What currency do you want to buy?: "))

    #1 us dolar = 0.9152 euro
    if currency == 1:
        print("===============================")
        clear_terminal()
        final = 0.9152 * n
        print(colored(f"You buy {n} U.S Dollar for {final:.2f} Euro", "green"))
        return final

    #1 us dolar = 0.8932 swis franc
    elif currency == 2:
        print("===============================")
        clear_terminal()
        final = 0.8932 * n
        print(colored(f"You buy {n} U.S Dollar for {final:.2f} Swiss franc", "green"))
        return final

    #1 us dolar = 0.7978 british pound
    elif currency == 3:
        print("===============================")
        clear_terminal()
        final = 0.7981 * n
        print(colored(f"You buy {n} U.S Dollar for {final:.2f} British Pound", "green"))
        return final

    else:
        wrong_input()



def currency_buy_swisfranc(n):
    print(colored("1 = Euro", "green"))
    print(colored("2 = U.S Dollar", "green"))
    print(colored("3 = British Pound", "green"))
    currency = int(input("For What currency do you want to buy?: "))

    #1 swis franc = 1.0241 euro
    if currency == 1:
        print("===============================")
        clear_terminal()
        final = 1.0241 * n
        print(colored(f"You buy {n} Swiss franc for {final:.2f} Euro", "green"))
        return final

    #1 swis franc = 1.1199 us dollar
    elif currency == 2:
        print("===============================")
        clear_terminal()
        final = 1.1199 * n
        print(colored(f"You buy {n} Swiss franc for {final:.2f} U.S Dollar", "green"))
        return final

    #1 swis franc = 1.1195 british pound
    elif currency == 3:
        print("===============================")
        clear_terminal()
        final = 1.1195 * n
        print(colored(f"You buy {n} Swiss franc for {final:.2f} British Pound", "green"))
        return final

    else:
        wrong_input()


def currency_buy_britishpound(n):
    print(colored("1 = Euro", "green"))
    print(colored("2 = Swiss Franc", "green"))
    print(colored("3 = U.S Dollar", "green"))
    currency = int(input("For What currency do you want to buy?: "))

    #1 british pound = 1.1521 euro
    if currency == 1:
        print("===============================")
        clear_terminal()
        final = 1.1521 * n
        print(colored(f"You buy {n} British Pound for {final:.2f} Euro", "green"))
        return final

    #1 british pound = 1.1195 swis franc
    elif currency == 2:
        print("===============================")
        clear_terminal()
        final = 1.1195 * n
        print(colored(f"You buy {n} British Pound for {final:.2f} Swiss franc", "green"))
        return final

    #1 british pound = 1.2534 us dollar
    elif currency == 3:
        print("===============================")
        clear_terminal()
        final = 1.2534 * n
        print(colored(f"You buy {n} British Pound for {final:.2f} U.S Dollar", "green"))
        return final

    else:
        wrong_input()



if __name__ == "__main__":
    main()
