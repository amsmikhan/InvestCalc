# ©Moscow, 2020, Mikhail Sergeev
# The project is open source, feel free to use it
# the author is not responsible for possible financial losses resulting from investments based on data calculated by the
# program

import Company
import os
import sys

version = "1.1"

company = Company.Company()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    print("© Moscow, 2020, Mikhail Sergeev")
    print("The project is open source, feel free to use it")
    print("the author is not responsible for possible financial losses resulting")
    print("from investments based on data calculated by the program")
    print("Read readme before start!!!")
    print("Version " + version)
    print("=====================================================================")


def input_company_data(company_data):
    company_data['name'] = input("Input company name: ")
    company_data['ticker'] = input("Input company ticker: ")
    company_data['scope'] = input("Input company scope: ")
    company_data['price_per_share'] = float(input("Input current price per share of the company: "))
    company_data['earnings'] = float(input("Input earnings of the company: "))
    company_data['sales'] = float(input("Input sales of the company: "))
    company_data['book_value'] = float(input("Input book value of the company: "))
    company_data['debt'] = float(input("Input debt of the company: "))
    company_data['available_budget'] = float(input("Input available budget of the company: "))
    company_data['earnings_before_taxes'] = float(input("Input earnings before taxes of the company: "))
    company_data['amortization'] = float(input("Input amortization of the company: "))
    company_data['percents'] = float(input("Input interest expenses of the company: "))
    company_data['shares'] = int(input("Input number of shares of the company: "))
    return company_data


def calculate_company_fields(company_data):
    company_data['price'] = company.calculate_price()
    company_data['pe'] = company.calculate_pe()
    company_data['ps'] = company.calculate_ps()
    company_data['pbv'] = company.calculate_pbv()
    company_data['ev'] = company.calculate_ev()
    company_data['ebitda'] = company.calculate_ebitda()
    company_data['evebitda'] = company.calculate_evebitda()
    company_data['debtebitda'] = company.calculate_debtebitda()
    company_data['eps'] = company.calculate_eps()
    company_data['roe'] = company.calculate_roe()
    return company_data


def print_analysis(company_data):
    print("Capitalization(total price) of the company = " + str(company_data['price']) + ".")
    print("P/E = " + str(company_data['pe']) + ". It has to be more than 0, the less - the better.")
    print("P/S = " + str(company_data['ps']) + ". It has to be more than 0 but less than 1.")
    print("P/BV = " + str(company_data['pbv']) + ". It has to be less than 1.")
    print("EV = " + str(company_data['ev']) + ". This is real enterprise value.")
    print("EBITDA = " + str(
        company_data['ebitda']) + ". This are earnings before interest, taxes, depreciation and amortization.")
    print("EV/EBITDA = " + str(company_data['evebitda']) + ". It has to be more than 0, the less - the better.")
    print("DEBT/EBITDA = " + str(company_data['debtebitda']) + ". The less - the better.")
    print("EPS = " + str(company_data['eps']) + ". This are earnings per share. If it grows - it is good.")
    print("ROE = " + str(company_data['roe']) + ". This is return on equity. The more - the better.")


def main():
    clear()
    main_menu()

    company.company_data = input_company_data(company.company_data)
    company.company_data = calculate_company_fields(company.company_data)
    input("Press Enter to continue")

    clear()
    main_menu()

    print_analysis(company.company_data)

    input("Press Enter to quit.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
