import pytest
from decimal import Decimal
try:
    from mock import Mock
except ModuleNotFoundError:
    from unittest.mock import Mock

from ...business.calculator import Calculator
from ...facade.calculate_transaction import TransactionCalculator


@pytest.fixture
def mock_calculator():
    return Mock(spec=Calculator)


@pytest.mark.parametrize('ask, answered', [
    (
        {
            'tokencount': 0,
            'bonus_return': 20,
            'satoshi_per_vtx': 2590,
            'satoshi_amount_for_puchase': 2590
        },
        {
            'vtx_return': { 
                'request': {
                    'bonus': 20,
                    'price': 2590, 
                    'satoshi_amount_for_puchase': 2590
                },
                'response': {
                    'vtx_pre_bonus': Decimal(100),
                    'bonus_vtx': Decimal(20),
                    'total_vtx': Decimal(120),
                }
            }
        }
    ),
])
def test_calculate_transaction(mock_calculator, ask, answered):
    mock_calculator.bonus.return_value = ask['bonus_return']
    mock_calculator.satoshi_per_vtx.return_value = ask['satoshi_per_vtx']
    mock_calculator.vtx_amount_purchased.return_value = answered['vtx_return']['response']

    tc = TransactionCalculator()
    tc.calculator = mock_calculator
    assert tc.calculate(ask['tokencount'], ask['satoshi_amount_for_puchase']) == answered['vtx_return']

    mock_calculator.bonus.assert_called_with(ask['tokencount'])
    mock_calculator.satoshi_per_vtx.assert_called_with(ask['tokencount'])
    mock_calculator.vtx_amount_purchased.assert_called_with(answered['vtx_return']['request'])
