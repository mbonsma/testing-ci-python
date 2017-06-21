
import function

def test_add_nums():
  added = function.add_nums(2, 2)
  assert added == 4
  string_add = function.add_nums('a','b')
  assert string_add == 'ab'
  neg = function.add_nums(-1,-2)
  assert neg == 3
