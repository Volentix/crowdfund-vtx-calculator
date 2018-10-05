def compute_vtx(data):

    total_vtx_pre_bonus = data['satoshi_purchase_amount'] / data['price']

    bonus_vtx = total_vtx_pre_bonus* data['bonus'] / 100
    total_vtx = total_vtx_pre_bonus + bonus_vtx

    return {
        'total_vtx_pre_bonus': total_vtx_pre_bonus, 
        'bonus_vtx': bonus_vtx,
        'total_vtx': total_vtx,
    }