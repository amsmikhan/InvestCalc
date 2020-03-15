# ©Moscow, 2020, Mikhail Sergeev
# The project is open source, feel free to use it
# the author is not responsible for possible financial losses resulting from investments based on data calculated by the
# program

import calculators
import os

version = "1.0"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    print("Moscow, 2020, Mikhail Sergeev")
    print("The project is open source, feel free to use it")
    print("the author is not responsible for possible financial losses resulting")
    print("from investments based on data calculated by the program")
    print("Version " + version)
    print("=====================================================================")


def main():
    clear()
    main_menu()

    print("Read readme before start!!!")

    price_per_share = float(input("Input current price per share of the company: "))
    earnings = float(input("Input earnings of the company: "))
    sales = float(input("Input sales of the company: "))
    book_value = float(input("Input book value of the company: "))
    debt = float(input("Input debt of the company: "))
    available_budget = float(input("Input available budget of the company: "))
    earnings_before_taxes = float(input("Input earnings before taxes of the company: "))
    amortization = float(input("Input amortization of the company: "))
    percents = float(input("Input interest expenses of the company: "))
    shares = int(input("Input number of shares of the company: "))

    input("Press Enter to continue")

    clear()
    main_menu()

    print("All data is saved, starting calculations")

    price = calculators.calculate_price(shares, price_per_share)
    pe = calculators.calculate_pe(price, earnings)
    ps = calculators.calculate_ps(price, sales)
    pbv = calculators.calculate_pbv(price, book_value)
    ev = calculators.calculate_ev(price, debt, available_budget)
    ebitda = calculators.calculate_ebitda(earnings_before_taxes, amortization, percents)
    evebitda = calculators.calculate_evebitda(ev, ebitda)
    debtebitda = calculators.calculate_debtebitda(debt, ebitda)
    eps = calculators.calculate_eps(earnings, shares)
    roe = calculators.calculate_roe(earnings, book_value)

    input("Calculations are done, press Enter to go to analysis")

    clear()
    main_menu()

    print("Capitalization(total price) of the company = " + str(price) + ".")
    print("P/E = " + str(pe) + ". It has to be more than 0, the less - the better.")
    print("P/S = " + str(ps) + ". It has to be more than 0 but less than 1.")
    print("P/BV = " + str(pbv) + ". It has to be less than 1.")
    print("EV = " + str(ev) + ". This is real enterprise value.")
    print("EBITDA = " + str(ebitda) + ". This are earnings before interest, taxes, depreciation and amortization.")
    print("EV/EBITDA = " + str(evebitda) + ". It has to be more than 0, the less - the better.")
    print("DEBT/EBITDA = " + str(debtebitda) + ". The less - the better.")
    print("EPS = " + str(eps) + ". This are earnings per share. If it grows - it is good.")
    print("ROE = " + str(roe) + ". This is return on equity. The more - the better.")

    input("Press Enter to quit.")

    return 0


main()
