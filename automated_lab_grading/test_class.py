import os

from student_notebook import encrypt as student_encrypt
from student_notebook import text_to_digit as student_text_to_digit

class TestClass:
    def test_encrypt_CASE_ONE(self):
        assert student_encrypt('abcde') == 'abcde'
    def test_encrypt_CASE_TWO(self):
        assert student_encrypt('hellllohha') == 'hel4oh2a'
    def test_encrypt_CASE_THREE(self):
        assert student_encrypt('xiinchaooo') == 'xi2nchao3'
    def test_encrypt_CASE_FOUR(self):
        assert student_encrypt('aaabbc') == 'a3b2c'

    def test_text_to_digt_CASE_ONE(self):
        assert student_text_to_digit('six two five five') == 6255
    def test_text_to_digt_CASE_TWO(self):
        assert student_text_to_digit('nine nine four two') == 9942
    def test_text_to_digt_CASE_THREE(self):
        assert student_text_to_digit('five') == 5
    def test_text_to_digt_CASE_FOUR(self):
        assert student_text_to_digit('four zero three') == 403
