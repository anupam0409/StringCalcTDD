import str_calc
import pytest

def test_empty_string():
	assert str_calc.add('') == 0 #example1

def test_add_two_CSVs():
	assert str_calc.add('1') == 1 #example2

def test_add_multiple_CSVs():
	assert str_calc.add('1,5') == 6 #example3

def test_new_line_as_delimiter():
	assert str_calc.add('1\n2,3') == 6 #point3 text case

def test_different_delimiters():
	assert str_calc.add('//;\n1;2') == 3 #point4 test case

def test_negative_numbers_exception():
	with pytest.raises(Exception, match = r'Negatives not allowed'): #point5 test case
		str_calc.add('-1, -2, -3, 7, 8')

