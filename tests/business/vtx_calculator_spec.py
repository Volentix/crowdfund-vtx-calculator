import pytest
from decimal import *
from business.vtx_calculator import compute_vtx

@pytest.mark.parametrize('calcdata, result', [
    (
        {'bonus':20, 'price': 2590, 'satoshi_purchase_amount': 2590}, 
        {'vtx_pre_bonus': 1.0, 'bonus_vtx': 0.2, 'total_vtx': 1.2 }
    ),(
        { 'bonus':20, 'price': 2590, 'satoshi_purchase_amount': 5180 }, 
        { 'vtx_pre_bonus': 2.0, 'bonus_vtx': 0.4, 'total_vtx': 2.4 }
    ),(
        { 'bonus':10, 'price': 2590, 'satoshi_purchase_amount': 5180 }, 
        { 'vtx_pre_bonus': 2.0, 'bonus_vtx': 0.2, 'total_vtx': 2.2 }
    ),(
        { 'bonus':0, 'price': 2590, 'satoshi_purchase_amount': 5180 }, 
        { 'vtx_pre_bonus': 2.0, 'bonus_vtx': 0.0, 'total_vtx': 2.0 }
    ),(
        { 'bonus':0, 'price': 2591, 'satoshi_purchase_amount': 5180 }, 
       { 'vtx_pre_bonus': 1.9992281, 'bonus_vtx': 0.0, 'total_vtx': 1.9992281 }
    ),(
        { 'bonus': 5, 'price': 2591, 'satoshi_purchase_amount': 5180 }, 
       { 'vtx_pre_bonus': 1.9992281, 'bonus_vtx': 0.09996140, 'total_vtx': 2.09918950 }
    ),
])
def test_bonus_calculator(calcdata, result):
    retresult = compute_vtx(calcdata)
    assert retresult['vtx_pre_bonus'] == round(Decimal(result['vtx_pre_bonus']),8)
    assert retresult['bonus_vtx'] == round(Decimal(result['bonus_vtx']), 8)
    assert retresult['total_vtx'] == round(Decimal(result['total_vtx']), 8)
