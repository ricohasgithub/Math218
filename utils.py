
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

# Algorithms useful for quick reference
def get_x_hat(A, b):

    # Returns x_hat such that bV (orthogonal decomp of b onto V) = A * x_hat
    # Formula: x_hat = A_t * A * x_hat = A_t * b

    AT = get_transpose(A)

    ATA = AT * A
    ATb = AT * b

    x = make_augment(ATA, ATb)

    # Solve for x_hat from new system of equations
    return get_rref(x)