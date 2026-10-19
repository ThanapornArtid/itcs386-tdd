import pytest
from shipping import shipping_fee
@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),    # Rule 2: inside
    (3, 60),      # Rule 3: inside
    (1.01, 60),   # Rule 3: just above 1 kg
    (5, 60),      # Rule 3: upper edge
    (6, 70),      # Rule 4: exactly 1 kg above 5
    (6.5, 80),    # Rule 4: 1.5 kg above 5 -> 2 started kg
])
def test_shipping_fee(weight, expected_fee):
    assert shipping_fee(weight) == expected_fee

def test_exactly_one_kg_costs_40():
    assert shipping_fee(1) == 40

def test_started_kilogram_above_five_is_charged():
    assert shipping_fee(5.2) == 70

def test_zero_weight_is_rejected():
    with pytest.raises(ValueError):
        shipping_fee(0)

def test_negative_weight_is_rejected():
    with pytest.raises(ValueError):
        shipping_fee(-1)