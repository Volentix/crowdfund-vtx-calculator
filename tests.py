from business.pricecalculator import compute_price
from business.bonuscalculator import compute_bonus
from business.vtxcalculator import compute_vtx

def test_price_calculations():
    """
    Tests the compute_price function
    """
    testdata = [
        {'tokencount': 0, 'price': 2590},
        {'tokencount': 112160, 'price': 2590},
        {'tokencount': 112161, 'price': 2591},
        {'tokencount': 224321, 'price': 2591},
        {'tokencount': 224322, 'price': 2592},
        {'tokencount': 281520000, 'price': 5099},
        {'tokencount': 281524109, 'price': 5099},
        {'tokencount': 281524110, 'price': 5100},
    ]

    for testme in testdata:
        price = compute_price(testme['tokencount'])
        assert price == testme['price']

def test_bonus_calculations():
    """
    Tests the compute_bonus function
    """

    testdata = [
        {'tokencount': 0, 'bonus':20},
        {'tokencount': 99000000, 'bonus':20},
        {'tokencount': 99000000.0001, 'bonus':15},
        {'tokencount': 171900000, 'bonus':15},
        {'tokencount': 171900000.001, 'bonus':10},
        {'tokencount': 226020000, 'bonus':10},
        {'tokencount': 226020000.00001, 'bonus':5},
        {'tokencount': 281520000, 'bonus':5},
        {'tokencount': 281520000.0001, 'bonus':0},
    ]

    for testme in testdata:
        bonus = compute_bonus(testme['tokencount'])
        print(bonus)
        assert bonus == testme['bonus']

def test_calculate_purchase():
    """
    Test to calculate the purchase of the tokens
    """
    testdata = [
        {
            'calcdata': {
                'bonus':20, 
                'price': 2590, 
                'satoshi_purchase_amount': 2590
            },
            'total_vtx_pre_bonus': 1.0,
            'bonus_vtx': 0.2,
            'total_vtx': 1.2
        },
        {
            'calcdata': {
                'bonus':20, 
                'price': 2590, 
                'satoshi_purchase_amount': 5180
            },
            'total_vtx_pre_bonus': 2.0,
            'bonus_vtx': 0.4,
            'total_vtx': 2.4
        }
    ]

    for testme in testdata:
        result = compute_vtx(testme['calcdata'])
        assert result['total_vtx_pre_bonus'] == testme['total_vtx_pre_bonus']
        assert result['bonus_vtx'] == testme['bonus_vtx']
        assert result['total_vtx'] == testme['total_vtx']



        # assert result['total_vtx'] == testme['total_vtx']
    