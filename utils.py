
from sympy import *

# Helper methods to return new matrix instances
def get_inverse(A):
    return Inverse(A)

def get_transpose(A):
    return A.tranpose()

def get_rref(A, pivots=False):
    return A.rref(pivots=pivots)

def make_augment(A, b):
    return A.row_join(b)

