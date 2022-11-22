import math

numbers_lst = [1, 9, 64, 25, 4]
words_lst = ['раз', 'два', 'три']


def test_filter():
    assert list(filter(lambda x: x == 9, numbers_lst)) == [9]
    assert list(filter(lambda x: x == 'два', words_lst)) == ['два']


def test_map():
    assert list(map(lambda x: x * 2, numbers_lst)) == [2, 18, 128, 50, 8]
    assert list(map(lambda x: x * 2, words_lst)) == ['разраз', 'двадва', 'тритри']


def test_sorted():
    assert sorted(numbers_lst) == [1, 4, 9, 25, 64]
    assert sorted(numbers_lst, reverse=True) == [64, 25, 9, 4, 1]
    assert sorted(numbers_lst, key=lambda x: x % 2) == [64, 4, 1, 9, 25]
    assert sorted(words_lst) == ['два', 'раз', 'три']
    assert sorted(words_lst, reverse=True) == ['три', 'раз', 'два']


def test_pi():
    assert round(math.pi, 10) == 3.1415926536


def test_sqrt():
    assert math.sqrt(numbers_lst[2]) == 8


def test_pow():
    assert math.pow(numbers_lst[4], 2) == 16
    assert math.pow(numbers_lst[1], 3) == 729


def test_hypot():
    x = 2
    y = 5
    assert math.hypot(x, y) == math.sqrt(x ** 2 + y ** 2)
