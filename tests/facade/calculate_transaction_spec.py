import pytest
from mock import Mock
from decimal import *

from business.bonus_calculator import compute_bonus
from business.satoshi_calculator import compute_satoshi
from business.vtx_calculator import compute_vtx
from facade.calculate_transaction import TransactionCalculator

@pytest.fixture
def mock_compute():
    return {
        'bonus': Mock(spec=compute_bonus),
        'satoshi': Mock(spec=compute_satoshi),
        'vtx': Mock(spec=compute_vtx)
    }

@pytest.mark.parametrize('ask, answered', [
    (
        {
            'tokencount': 0, 
            'bonus_return': 20,
            'satoshi_per_vtx': 2590,
            'satoshi_amount_for_puchase': 2590,
            'vtx_request': {
                'bonus': 20, 
                'price': 2590, 
                'satoshi_amount_for_puchase': 2590
            },
            'vtx_return':{ 
                'vtx_pre_bonus': Decimal(100), 
                'bonus_vtx': Decimal(20),
                'total_vtx': Decimal(120),
            }
        },
        {
            'silly': 2610
        }
    ),
])
def test_calculate_transaction(mock_compute, ask, answered):
    mock_compute['bonus'].return_value = ask['bonus_return']
    mock_compute['satoshi'].return_value = ask['satoshi_per_vtx']
    mock_compute['vtx'].return_value = ask['vtx_return']

    tc = TransactionCalculator(mock_compute['bonus'], mock_compute['satoshi'],mock_compute['vtx'])
    assert tc.calculate(ask['tokencount'],ask['satoshi_amount_for_puchase']) == answered['silly']

    mock_compute['bonus'].assert_called_with(ask['tokencount'])
    mock_compute['satoshi'].assert_called_with(ask['tokencount'])
    mock_compute['vtx'].assert_called_with(ask['vtx_request'])