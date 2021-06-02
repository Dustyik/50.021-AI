test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_yield(test_list):
    for state in test_list:
        if state % 2 == 0:
            yield state

results = test_yield(test_list)