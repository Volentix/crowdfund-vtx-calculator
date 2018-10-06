import pytest
from business.satoshi_calculator import compute_satoshi

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
def test_satoshi_calculation(tokencount, price):
    rprice = compute_satoshi(tokencount)
    assert rprice == price
