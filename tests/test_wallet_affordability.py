import pytest
from wallet_affordability import can_afford


# --- Valid inputs: must return the real bool True/False (not 1/0) ---
@pytest.mark.parametrize(
    "tc_id, balance, price, expected",
    [
        ("A01", 1000, 500, True),    # typical: affordable
        ("A02", 1000, 1000, True),   # boundary: balance == price
        ("A03", 999, 1000, False),   # boundary: one cent short
        ("A04", 0, 0, True),         # boundary: zero balance, zero price
        ("A05", 0, 1, False),        # boundary: zero balance, price > 0
        ("A06", 1000, 0, True),      # zero price is always affordable
    ],
)
def test_affordability_returns_bool(tc_id, balance, price, expected):
    result = can_afford(balance, price)
    assert result is expected  # `is` rejects 1 and 0


# --- Correct type but negative -> ValueError ---
@pytest.mark.parametrize(
    "tc_id, balance, price",
    [
        ("A07", -1, 100),
        ("A08", 100, -1),
    ],
)
def test_negative_raises_value_error(tc_id, balance, price):
    with pytest.raises(ValueError):
        can_afford(balance, price)


# --- Invalid data type -> TypeError ---
@pytest.mark.parametrize(
    "tc_id, balance, price",
    [
        ("A09", "1000", 500),   # str balance
        ("A10", 100, "50"),     # str price
        ("A11", 100.0, 50),     # float balance
        ("A12", True, 1),       # bool balance
        ("A13", 100, False),    # bool price
    ],
)
def test_invalid_type_raises_type_error(tc_id, balance, price):
    with pytest.raises(TypeError):
        can_afford(balance, price)
