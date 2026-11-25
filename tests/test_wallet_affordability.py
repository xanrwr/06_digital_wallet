import pytest
from wallet_affordability import can_afford


# --- Valid inputs: must return the real bool True/False (not 1/0) ---
# All 6 FAIL (D2: code returns int(...), so it gives 1 or 0 and `1 is True` is False)
@pytest.mark.parametrize(
    "tc_id, balance, price, expected",
    [
        ("A01", 1000, 500, True),    # typical: affordable                 -> FAIL (returns 1)
        ("A02", 1000, 1000, True),   # boundary: balance == price          -> FAIL (returns 1)
        ("A03", 999, 1000, False),   # boundary: one cent short            -> FAIL (returns 0)
        ("A04", 0, 0, True),         # boundary: zero balance, zero price  -> FAIL (returns 1)
        ("A05", 0, 1, False),        # boundary: zero balance, price > 0   -> FAIL (returns 0)
        ("A06", 1000, 0, True),      # zero price is always affordable     -> FAIL (returns 1)
    ],
)
def test_affordability_returns_bool(tc_id, balance, price, expected):
    result = can_afford(balance, price)
    assert result is expected  # `is` rejects 1 and 0


# --- Correct type but negative -> ValueError ---
@pytest.mark.parametrize(
    "tc_id, balance, price",
    [
        ("A07", -1, 100),   # negative balance -> PASS
        ("A08", 100, -1),   # negative price   -> PASS
    ],
)
def test_negative_raises_value_error(tc_id, balance, price):
    with pytest.raises(ValueError):
        can_afford(balance, price)


# --- Invalid data type -> TypeError ---
@pytest.mark.parametrize(
    "tc_id, balance, price",
    [
        ("A09", "1000", 500),   # str balance   -> PASS
        ("A10", 100, "50"),     # str price     -> PASS
        ("A11", 100.0, 50),     # float balance -> PASS
        ("A12", True, 1),       # bool balance  -> PASS
        ("A13", 100, False),    # bool price    -> PASS
    ],
)
def test_invalid_type_raises_type_error(tc_id, balance, price):
    with pytest.raises(TypeError):
        can_afford(balance, price)
