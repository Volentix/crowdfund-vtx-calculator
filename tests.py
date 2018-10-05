from calculator import compute_price, compute_bonus


def test_price_calculations():
    """
    Tests the compute_price function
    """

    # ---------------------------
    # At exactly zero tokens sold
    # ---------------------------

    price = compute_price(0)
    assert price == 2590

    # -------------------------------
    # At tokens sold equal to 112,161
    # -------------------------------

    price = compute_price(112161)
    assert price == 2591

    # -------------------------------
    # At tokens sold equal to 224,322
    # -------------------------------

    price = compute_price(224322)
    assert price == 2592

    # -------------------------------
    # At tokens sold equal to 336,483
    # -------------------------------

    price = compute_price(336483)
    assert price == 2593

    # -------------------------------
    # At tokens sold equal to 448,644
    # -------------------------------

    price = compute_price(448644)
    assert price == 2594

    # -------------------------------
    # At tokens sold equal to 560,805
    # -------------------------------

    price = compute_price(560805)
    assert price == 2595

    # -------------------------------
    # At tokens sold equal to 672,966
    # -------------------------------

    price = compute_price(672966)
    assert price == 2596

    # -------------------------------
    # At tokens sold equal to 785,127
    # -------------------------------

    price = compute_price(785127)
    assert price == 2597

    # -----------------------------------
    # At tokens sold equal to 281,520,000
    # -----------------------------------

    price = compute_price(281520000)
    assert price == 5100


def test_bonus_calculations():
    """
    Tests the compute_bonus function
    """

    # -------------------
    # Phase 1
    # At zero tokens sold
    # -------------------

    bonus = compute_bonus(100, 0)
    assert bonus == 20

    # ---------------------------------
    # Phase 1
    # At exactly 99,000,000 tokens sold
    # ---------------------------------

    bonus = compute_bonus(100, 99000000)
    assert bonus == 20

    # ---------------------------------
    # Phase 2
    # At exactly 99,000,001 tokens sold
    # ---------------------------------

    bonus = compute_bonus(100, 99000001)
    assert bonus == 15

    # ----------------------------------
    # Phase 2
    # At exactly 171,900,000 tokens sold
    # ----------------------------------

    bonus = compute_bonus(100, 171900000)
    assert bonus == 15

    # ----------------------------------
    # Phase 3
    # At exactly 171,900,001 tokens sold
    # ----------------------------------

    bonus = compute_bonus(100, 171900001)
    assert bonus == 10

    # ----------------------------------
    # Phase 3
    # At exactly 226,020,000 tokens sold
    # ----------------------------------

    bonus = compute_bonus(100, 226020000)
    assert bonus == 10

    # ----------------------------------
    # Phase 4
    # At exactly 226,020,001 tokens sold
    # ----------------------------------

    bonus = compute_bonus(100, 226020001)
    assert bonus == 5

    # ----------------------------------
    # Phase 4
    # At exactly 281,520,000 tokens sold
    # ----------------------------------

    bonus = compute_bonus(100, 281520000)
    assert bonus == 5
