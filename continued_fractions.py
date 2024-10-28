from itertools import islice
from sympy.core import pi
from sympy.ntheory.continued_fraction import continued_fraction_iterator

print(list(islice(continued_fraction_iterator(pi), 15)))