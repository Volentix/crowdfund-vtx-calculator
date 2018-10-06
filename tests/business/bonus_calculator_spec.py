import pytest
from business.bonus_calculator import compute_bonus

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
def test_bonus_calculator(tokencount, bonus):
    bonus = compute_bonus(tokencount)
    assert bonus == bonus