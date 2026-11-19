import pytest
from wallet_withdrawal import withdraw


# --- Valid withdrawals (return the remaining balance) ---
@pytest.mark.parametrize(
    "tc_id, balance, amount, expected",
    [
        ("W01", 1000, 300, 700),   # typical
        ("W02", 1000, 1000, 0),    # boundary: exact balance -> 0
        ("W03", 1000, 999, 1),     # boundary: just below balance
        ("W04", 1000, 1, 999),     # boundary: smallest valid amount
    ],
)
def test_valid_withdrawal(tc_id, balance, amount, expected):
    result = withdraw(balance, amount)
    assert result == expected
    assert type(result) is int


# --- Correct type but outside permitted range -> ValueError ---
@pytest.mark.parametrize(
    "tc_id, balance, amount",
    [
        ("W05", 1000, 1001),  # above balance
        ("W06", 1000, 0),     # zero amount
        ("W07", 1000, -1),    # negative amount
        ("W08", -1, 1),       # negative balance
        ("W09", 0, 1),        # zero balance, any amount exceeds it
    ],
)
def test_out_of_range_raises_value_error(tc_id, balance, amount):
    with pytest.raises(ValueError):
        withdraw(balance, amount)


# --- Invalid data type -> TypeError ---
@pytest.mark.parametrize(
    "tc_id, balance, amount",
    [
        ("W10", "1000", 300),   # str balance
        ("W11", 1000, "300"),   # str amount
        ("W12", 10.5, 300),     # float balance
        ("W13", True, 1),       # bool balance
        ("W14", 1000, True),    # bool amount
        ("W15", None, 300),     # None balance
    ],
)
def test_invalid_type_raises_type_error(tc_id, balance, amount):
    with pytest.raises(TypeError):
        withdraw(balance, amount)
