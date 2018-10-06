class TransactionCalculator:

    def __init__(self, compute_bonus, compute_satoshi, compute_vtx):
        self.compute_bonus = compute_bonus
        self.compute_satoshi = compute_satoshi
        self.compute_vtx = compute_vtx

    def calculate(self,tokens_sold, satoshi_amount_for_puchase):
        rvalue = self.compute_vtx(
            {
                'bonus':self.compute_bonus(tokens_sold), 
                'price': self.compute_satoshi(tokens_sold), 
                'satoshi_amount_for_puchase': satoshi_amount_for_puchase
            }
        )
        return  self.compute_satoshi(tokens_sold) + self.compute_bonus(tokens_sold)