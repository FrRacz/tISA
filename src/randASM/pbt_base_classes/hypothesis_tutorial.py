from hypothesis import given, strategies as st

def selection_sort(lst):
    result = []
    while lst:
        smallest = min(lst)
        result.append(smallest)
        lst.remove(smallest)
    return result

@given(st.lists(st.integers()))
def test_sort_correct(lst):
    print(f"called with {lst}")
    assert selection_sort(lst.copy()) == sorted(lst)

test_sort_correct()
