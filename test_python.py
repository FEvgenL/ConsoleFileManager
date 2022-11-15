def test_filter():
    numbers_lst = [1, 2, 3, 4, 1, 5, 6, 7, 8, 9, 0, 1]
    assert list(filter(lambda x: x == 1, numbers_lst)) == [1, 1, 1]


def test_map():
    numbers_lst = [1, 2, 3, 4, 5]
    assert list(map(lambda x: x * 2, numbers_lst)) == [2, 4, 6, 8, 10]
