from decimal import *
import math

class Calculator:
    
    def bonus(self, tokens_sold):
        bonus = 0
        if 0 <= tokens_sold <= 99000000:
            bonus = 20
        if 99000000 < tokens_sold <= 171900000:
            bonus = 15
        if 171900000 < tokens_sold <= 226020000:
            bonus = 10
        if 226020000 < tokens_sold <= 281520000:
            bonus = 5
        return bonus
    
    def satoshi_per_vtx(self, tokens_sold):
        # TODO: Remove hardcoded value
        increment = 112161
        addition = math.floor(tokens_sold/increment)

        # TODO: Remove hardcoded value
        start_price = 2590
        return start_price + addition

    def vtx_amount_purchased(self, data):

        # 0.00000001
        # 100 Million V = 1 VTX

        vtx_pre_bonus = data['satoshi_amount_for_puchase'] / data['price']

        bonus_vtx = 0
        if (data['bonus'] > 0):
            bonus_vtx = vtx_pre_bonus* data['bonus'] / 100

        return {
            'vtx_pre_bonus': round(Decimal(vtx_pre_bonus), 8), 
            'bonus_vtx': round(Decimal(bonus_vtx), 8),
            'total_vtx': round(Decimal(vtx_pre_bonus + bonus_vtx), 8),
        }