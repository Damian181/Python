from exchangeCurrency import currency_sell, currency_buy, wrong_input, currency_sell_euro, currency_sell_usdollar, currency_sell_swisfranc, currency_sell_britishpound, currency_buy_euro, currency_buy_usdollar, currency_buy_swisfranc, currency_buy_britishpound

"""
pytest test_project.py -s
for every currency 3 times
=================SELL================
"""
#Euro
def test_currency_sell1():
    try:
        assert currency_sell(-1) == wrong_input()
    except AssertionError:
        assert currency_sell(2) == 9.1934
        assert currency_sell(100) == 459.67

#U.S Dolar
def test_currency_sell2():
    try:
        assert currency_sell(-1) == wrong_input()
    except AssertionError:
        assert currency_sell(2) == 8.3606
        assert currency_sell(100) == 418.03
#Swis Franc
def test_currency_sell3():
    try:
        assert currency_sell(-1) == wrong_input()
    except AssertionError:
        assert currency_sell(2) == 9.374
        assert currency_sell(100) == 468.70000000000005

#British pound
def test_currency_sell4():
    try:
        assert currency_sell(-1) == wrong_input()
    except AssertionError:
        assert currency_sell(2) == 10.4634
        assert currency_sell(100) == 523.17

"""
=====================BUY=======================
Euro
"""
def test_currency_buy1():
    try:
        assert currency_buy(-1) == wrong_input()
    except AssertionError:
        assert currency_buy(2) == 9.2912
        assert currency_buy(100) == 464.56

#U.S Dolar
def test_currency_buy2():
    try:
        assert currency_buy(-1) == wrong_input()
    except AssertionError:
        assert currency_buy(2) == 8.377
        assert currency_buy(100) == 418.85

#Swis Franc
def test_currency_buy3():
    try:
        assert currency_buy(-1) == wrong_input()
    except AssertionError:
        assert currency_buy(2) == 9.3914
        assert currency_buy(100) == 469.57000000000005

#British pound
def test_currency_buy4():
    try:
        assert currency_buy(-1) == wrong_input()
    except AssertionError:
        assert currency_buy(2) == 10.494
        assert currency_buy(100) == 524.7





# test other currency=========================
# SELL==================Euro==================SELL
# ================================================
        #Us Dollar
def test_sell_other_euro1():
    try:
        assert currency_sell_euro(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_euro(2) == 2.1848
        assert currency_sell_euro(100) == 109.24000000000001

        #Swiss Franc
def test_sell_other_euro2():
    try:
        assert currency_sell_euro(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_euro(2) == 1.9532
        assert currency_sell_euro(100) == 97.66

        #British Pound
def test_sell_other_euro3():
    try:
        assert currency_sell_euro(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_euro(2) == 1.736
        assert currency_sell_euro(100) == 86.8

#sell================U.S Dolar================
        #Euro
def test_sell_other_dollar1():
    try:
        assert currency_sell_usdollar(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_usdollar(2) == 1.8304
        assert currency_sell_usdollar(100) == 91.52

        #Swiss Franc
def test_sell_other_dollar2():
    try:
        assert currency_sell_usdollar(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_usdollar(2) == 1.7856
        assert currency_sell_usdollar(100) == 89.28

        #British Pound
def test_sell_other_dollar3():
    try:
        assert currency_sell_usdollar(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_usdollar(2) == 1.5962
        assert currency_sell_usdollar(100) == 79.81

# sell================Swiss Franc================
        #Euro
def test_sell_other_swisfranc1():
    try:
        assert currency_sell_swisfranc(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_swisfranc(2) == 2.0464
        assert currency_sell_swisfranc(100) == 102.32000000000001

        #Us Dollar
def test_sell_other_swisfranc2():
    try:
        assert currency_sell_swisfranc(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_swisfranc(2) == 2.2388
        assert currency_sell_swisfranc(100) == 111.94

        #British Pound
def test_sell_other_swisfranc3():
    try:
        assert currency_sell_swisfranc(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_swisfranc(2) == 2.238
        assert currency_sell_swisfranc(100) == 111.9

#sell================British Pound================
        #Euro
def test_sell_other_britishpound1():
    try:
        assert currency_sell_britishpound(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_britishpound(2) == 2.303
        assert currency_sell_britishpound(100) == 115.14999999999999

        #Swiss Franc
def test_sell_other_swisfranc2():
    try:
        assert currency_sell_britishpound(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_britishpound(2) == 2.238
        assert currency_sell_britishpound(100) == 111.9

        #U.S Dollar
def test_sell_other_swisfranc3():
    try:
        assert currency_sell_britishpound(-1) == wrong_input()
    except AssertionError:
        assert currency_sell_britishpound(2) == 2.506
        assert currency_sell_britishpound(100) == 125.29999999999998


# test other currency=========================
# BUY==================Euro==================BUY
# ================================================
        # Us Dollar
def test_buy_other_euro1():
    try:
        assert currency_buy_euro(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_euro(2) == 2.1856
        assert currency_buy_euro(100) == 109.28

        #Swiss Franc
def test_buy_other_euro2():
    try:
        assert currency_buy_euro(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_euro(2) == 1.9548
        assert currency_buy_euro(100) == 97.74000000000001

        #British Pound
def test_buy_other_euro3():
    try:
        assert currency_buy_euro(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_euro(2) == 1.737
        assert currency_buy_euro(100) == 86.85000000000001

#buy================U.S Dolar================
        #Euro
def test_buy_other_dollar1():
    try:
        assert currency_buy_usdollar(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_usdollar(2) == 1.8304
        assert currency_buy_usdollar(100) == 91.52

        #Swiss Franc
def test_buy_other_dollar2():
    try:
        assert currency_buy_usdollar(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_usdollar(2) == 1.7864
        assert currency_buy_usdollar(100) == 89.32

        #British Pound
def test_buy_other_dollar3():
    try:
        assert currency_buy_usdollar(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_usdollar(2) == 1.5962
        assert currency_buy_usdollar(100) == 79.81

# buy================Swiss Franc================
        #Euro
def test_buy_other_swisfranc1():
    try:
        assert currency_buy_swisfranc(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_swisfranc(2) == 2.0482
        assert currency_buy_swisfranc(100) == 102.41

        #Us Dollar
def test_buy_other_swisfranc2():
    try:
        assert currency_buy_swisfranc(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_swisfranc(2) == 2.2398
        assert currency_buy_swisfranc(100) == 111.99

        #British Pound
def test_buy_other_swisfranc3():
    try:
        assert currency_buy_swisfranc(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_swisfranc(2) == 2.239
        assert currency_buy_swisfranc(100) == 111.94999999999999

#sell================British Pound================
        #Euro
def test_buy_other_britishpound1():
    try:
        assert currency_buy_britishpound(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_britishpound(2) == 2.3042
        assert currency_buy_britishpound(100) == 115.21

        #Swiss Franc
def test_buy_other_britishpound2():
    try:
        assert currency_buy_britishpound(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_britishpound(2) == 2.239
        assert currency_buy_britishpound(100) == 111.94999999999999

        #U.S Dollar
def test_buy_other_britishpound3():
    try:
        assert currency_buy_britishpound(-1) == wrong_input()
    except AssertionError:
        assert currency_buy_britishpound(2) == 2.5068
        assert currency_buy_britishpound(100) == 125.34
