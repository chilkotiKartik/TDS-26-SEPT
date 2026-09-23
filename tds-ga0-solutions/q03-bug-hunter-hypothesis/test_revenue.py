from hypothesis import given, settings, strategies as st

# --- paste ONLY the part below into the portal; the function is here for local testing ---


def compute_subscription_revenue(price, quantity):  # buggy version from the question
    raw = int(price) * int(quantity)
    if raw > 2147483647:
        raw = raw - 4294967296
    return raw


@settings(max_examples=1000, deadline=None)
@given(
    price=st.integers(min_value=0, max_value=10**7),
    quantity=st.integers(min_value=0, max_value=10**7),
)
def test_revenue_is_exact_product(price, quantity):
    result = compute_subscription_revenue(price, quantity)
    assert result == price * quantity
    assert result >= 0
