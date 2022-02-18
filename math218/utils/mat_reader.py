
from sympy import *

# Matrix reader class for easy inputting and computation
class Mat_Reader():

    def __init__(self, input_pref="entry"):
        # Num of rows
        self.m = 0
        # Num of cols
        self.n = 0
        # Sympy matrix -- TODO: Add Pytorch/Numpy/Pandas equivalents
        self.A = None
        # Preference as to how to input the matrix
        self.input_pref = input_pref

    def input_mat(self):

        # Method to instantiate fields
        self.m = int(input("# of rows (m): "))
        self.n = int(input("# of cols (n): "))
        
        # Populate matrix
        self.A_list = []
        
        if self.input_pref == "entry":

            # Input by ith, jth entry
            for r in range(self.m):

                row = []
                for c in range(self.n):
                    row.append(int(input("entry: ")))

                self.A_list.append(row)
                print(",")

        elif self.input_pref == "rows":

            # Input row by row
            for r in range(self.m):

                row_str = input("row: ")
                entries = row_str.split(" ")

                row = list(map(int, entries))
                self.A_list.append(row)
                print(",")

        elif self.input_pref == "cols":

            for i in range(self.m):
                self.A_list.append([])

            # Input col by col
            for c in range(self.n):

                col_str = input("col: ")
                entries = col_str.split(" ")

                col = list(map(int, entries))

                for r in range(len(col)):
                    self.A_list[r].append(col[r])

                print(",")

        self.A = Matrix(self.A_list)
        pprint(self.A)

    def get_A(self):
        return self.A

A = Mat_Reader(input_pref="cols")
A.input_mat()