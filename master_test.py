import random
from dummy_solution import dummy_solution
from largest_odd import largest_odd

class TestClass:

    def test_dummy_test1(self):
        assert dummy_solution([5,5,5]) == 5

    def test_dummy_test2(self):
        assert dummy_solution(random.sample([7,12,12], 3)) == 7

    def test_dummy_test3(self):
        assert dummy_solution(random.sample([12,4,4], 3)) == -1

    def test_dummy_random(self):
        args = [random.randint(0,1000) for i in range(3)]
        assert dummy_solution(args) == largest_odd(*args)