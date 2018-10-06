
class TransactionCalculator:

    def __init__(self, calculator):
        self.calculator = calculator

    def calculate(self,tokens_sold, satoshi_amount_for_puchase):
        request = {
            'bonus':self.calculator.bonus(tokens_sold), 
            'price': self.calculator.satoshi_per_vtx(tokens_sold), 
            'satoshi_amount_for_puchase': satoshi_amount_for_puchase
        }
        rvalues = {
            'request': request,
            'response': self.calculator.vtx_amount_purchased(request)
        }
        print(rvalues)
        return rvalues