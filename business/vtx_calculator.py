from decimal import *

def compute_vtx(data):

    # 0.00000001
    # 100 Million V = 1 VTX

    vtx_pre_bonus = data['satoshi_purchase_amount'] / data['price']

    bonus_vtx = 0
    if (data['bonus'] > 0):
        bonus_vtx = vtx_pre_bonus* data['bonus'] / 100

    return {
        'vtx_pre_bonus': round(Decimal(vtx_pre_bonus), 8), 
        'bonus_vtx': round(Decimal(bonus_vtx), 8),
        'total_vtx': round(Decimal(vtx_pre_bonus + bonus_vtx), 8),
    }