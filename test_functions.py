"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import sword

assert sword(3) == 'You can go challenge the Lady of Nothing!'
assert sword(1) == 'You are not strong enough to defeat the Lady of Nothing. To be continued....'
