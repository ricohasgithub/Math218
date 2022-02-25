
from sympy import *

# Helper methods to return new matrix instances
def get_inverse(A):
    return Inverse(A)

def get_transpose(A):
    return A.transpose()

def get_rref(A, pivots=False):
    return A.rref(pivots=pivots)

def make_augment(A, b):
    return A.row_join(b)

def mat_mult(A, b):
    return A * b

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

def get_bv(A, b):

    x_hat = get_x_hat(A, b)

    # Get the number of columns
    n = shape(x_hat)[1]
    # A is transposed, so get cols dim as rows and rows dim as cols
    m_aug = shape(A)[1]
    n_aug = shape(b)[0]

    # Get the augment b from x_hat
    b_aug = x_hat[:, (shape(x_hat)[1] - n_aug):]

    return mat_mult(A, b_aug)

def get_pv(A):
    
    # Returns projection matrix Pv for a given matrix A
    # Formula: Pv = A * (A_t * A)^-1 * A_t

    AT = get_transpose(A)
    ATA = AT * A

    ATA_1 = get_inverse(ATA)        
    Pv = A * ATA_1 * AT

    return Pv

def get_AtA(A):
    return A.transpose() * A

def get_Atb(A, b):
    return A.transpose() * b