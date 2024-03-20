from test import *
from palindrome import is_palindrome

is_false(is_palindrome(["plop"]), 'is not str')
is_false(is_palindrome(""), 'is empty')
is_false(is_palindrome("a"), 'is not even sized')
is_true(is_palindrome("elle"), 'is a palindrome')
is_false(is_palindrome("Elle"), 'is different characters')
