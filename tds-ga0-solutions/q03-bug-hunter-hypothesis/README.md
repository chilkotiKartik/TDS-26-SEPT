# Q3 · The Bug Hunter — Property-Based Testing (1 mark)

## Question
Write a **Hypothesis** `@given` test that *fails* on this buggy function but *passes* on the correct one:

```python
def compute_subscription_revenue(price, quantity):
    raw = int(price) * int(quantity)
    if raw > 2147483647:
        raw = raw - 4294967296
    return raw
```
Expected behaviour: exact `price * quantity`, no overflow artefacts.

## Answer — [`test_revenue.py`](test_revenue.py)
```python
from hypothesis import given, settings, strategies as st

@settings(max_examples=1000, deadline=None)
@given(
    price=st.integers(min_value=0, max_value=10**7),
    quantity=st.integers(min_value=0, max_value=10**7),
)
def test_revenue_is_exact_product(price, quantity):
    result = compute_subscription_revenue(price, quantity)
    assert result == price * quantity
    assert result >= 0
```

## Steps / reasoning
1. Spot the bug: it simulates **32-bit signed overflow** — once the product passes `2**31 - 1` (~2.1 billion) it wraps negative.
2. The given unit tests only use tiny numbers, so they never reach that region.
3. Let Hypothesis generate numbers up to 10⁷ each → products up to 10¹⁴, so most examples cross the overflow line.
4. The property is simply *"revenue equals price × quantity and is never negative"*.
5. Paste the code (imports + test) → **Check** → **Correct**.

## Run it yourself
```bash
pip install hypothesis pytest
pytest test_revenue.py   # fails against the buggy version (as it should)
```
