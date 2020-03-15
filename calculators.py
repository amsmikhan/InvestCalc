def calculate_pe(price, earnings):
    pe = price / earnings
    return pe


def calculate_ps(price, sales):
    ps = price / sales
    return ps


def calculate_pbv(price, book_value):
    pbv = price / book_value
    return pbv


def calculate_ev(price, debt, available_budget):
    ev = price + debt - available_budget
    return ev


def calculate_ebitda(earnings_before_taxes, amortization, percents):
    ebitda = earnings_before_taxes + amortization + percents
    return ebitda


def calculate_evebitda(ev, ebitda):
    evebitda = ev / ebitda
    return evebitda


def calculate_debtebitda(debt, ebitda):
    debtebitda = debt / ebitda
    return debtebitda


def calculate_eps(earnings, shares):
    eps = earnings / shares
    return eps


def calculate_roe(earnings, book_value):
    roe = earnings / book_value * 100
    return roe


def calculate_price(shares, price_per_share):
    price = shares * price_per_share / 1000000
    return price
