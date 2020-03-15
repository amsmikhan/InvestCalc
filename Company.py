class Company:

    def __init__(self):
        self.company_data = {}

    def add_data(self, company_data):
        self.company_data = company_data

    def get_company_data(self):
        return self.company_data

    def calculate_pe(self):
        pe = self.company_data['price'] / self.company_data['earnings']
        return pe

    def calculate_ps(self):
        ps = self.company_data['price'] / self.company_data['sales']
        return ps

    def calculate_pbv(self):
        pbv = self.company_data['price'] / self.company_data['book_value']
        return pbv

    def calculate_ev(self):
        ev = self.company_data['price'] + self.company_data['debt'] - self.company_data['available_budget']
        return ev

    def calculate_ebitda(self):
        ebitda = self.company_data['earnings_before_taxes'] + self.company_data['amortization'] + self.company_data[
            'percents']
        return ebitda

    def calculate_evebitda(self):
        evebitda = self.company_data['ev'] / self.company_data['ebitda']
        return evebitda

    def calculate_debtebitda(self):
        debtebitda = self.company_data['debt'] / self.company_data['ebitda']
        return debtebitda

    def calculate_eps(self):
        eps = self.company_data['earnings'] / self.company_data['shares']
        return eps

    def calculate_roe(self):
        roe = self.company_data['earnings'] / self.company_data['book_value'] * 100
        return roe

    def calculate_price(self):
        price = self.company_data['shares'] * self.company_data['price_per_share'] / 1000000
        return price
