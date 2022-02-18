
from sympy import *

# Matrix reader class for easy inputting and computation
class Mat_Reader():

    def __init__(self, pref="entry"):
        # Num of rows
        self.m = 0
        # Num of cols
        self.n = 0
        # Sympy matrix -- TODO: Add Pytorch/Numpy/Pandas equivalents
        self.A = None
        self.pref = pref

    def input_mat(self):

        # Method to instantiate fields
        self.m = int(input("# of rows (m): "))
        self.n = int(input("# of cols (n): "))
        
        # Populate matrix
        self.A_list = []
        
        if self.pref == "entry":
            for r in range(self.m):
                row = []
                for c in range(self.n):
                    row.append(int(input("entry: ")))
                self.A_list.append(row)
                print(",")
            self.A = Matrix(self.A_list)
            pprint(self.A)

A = Mat_Reader()
A.input_mat()