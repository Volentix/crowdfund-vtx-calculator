import pytest
from decimal import Decimal
from ...business.calculator import Calculator


@pytest.mark.parametrize('tokencount, bonus', [
  (0, 20),
  (99000000, 20),
  (99000000.0000001, 15),
  (171900000, 15),
  (171900000.0000001, 10),
  (226020000, 15),
  (226020000.0000001, 5),
  (281520000, 5),
  (281520000.0001, 0),
])
def test_bonus_calculator_1(tokencount, bonus):
    calc = Calculator()
    bonus = calc.bonus(tokencount)
    assert bonus == bonus


@pytest.mark.parametrize('tokencount, price', [
  (0, 2590),
  (112160, 2590),
  (112161, 2591),
  (224321, 2591),
  (224322, 2592),
  (281520000, 5099),
  (281524109, 5099),
  (281524110, 5100),
])
def test_satoshi_calculation_2(tokencount, price):
    calc = Calculator()
    rprice = calc.satoshi_per_vtx(tokencount)
    assert rprice == price


@pytest.mark.parametrize('calcdata, result', [
    (
        {
            'bonus': 20,
            'price': 2590,
            'satoshi_amount_for_puchase': 2590
        },
        {
            'vtx_pre_bonus': 1.0,
            'bonus_vtx': 0.2,
            'total_vtx': 1.2
        }
    ),
    (
        {
            'bonus': 20,
            'price': 2590,
            'satoshi_amount_for_puchase': 5180
        },
        {
            'vtx_pre_bonus': 2.0,
            'bonus_vtx': 0.4,
            'total_vtx': 2.4
        }
    ),
    (
        {
            'bonus': 10,
            'price': 2590,
            'satoshi_amount_for_puchase': 5180
        },
        {
            'vtx_pre_bonus': 2.0,
            'bonus_vtx': 0.2,
            'total_vtx': 2.2
        }
    ),
    (
        {
            'bonus': 0,
            'price': 2590,
            'satoshi_amount_for_puchase': 5180
        },
        {
            'vtx_pre_bonus': 2.0,
            'bonus_vtx': 0.0,
            'total_vtx': 2.0
        }
    ),
    (
        {
            'bonus': 0,
            'price': 2591,
            'satoshi_amount_for_puchase': 5180
        },
        {
            'vtx_pre_bonus': 1.9992281,
            'bonus_vtx': 0.0,
            'total_vtx': 1.9992281
        }
    ),
    (
        {
            'bonus': 5,
            'price': 2591,
            'satoshi_amount_for_puchase': 5180
        },
        {
            'vtx_pre_bonus': 1.9992281,
            'bonus_vtx': 0.09996140,
            'total_vtx': 2.09918950
        }
    )
])
def test_bonus_calculator_3(calcdata, result):
    calc = Calculator()
    retresult = calc.vtx_amount_purchased(calcdata)
    assert retresult['vtx_pre_bonus'] == round(Decimal(result['vtx_pre_bonus']), 8)
    assert retresult['bonus_vtx'] == round(Decimal(result['bonus_vtx']), 8)
    assert retresult['total_vtx'] == round(Decimal(result['total_vtx']), 8)
