import numpy as np
import matplotlib.pyplot as plt


class poly:
    coeff = np.array([])
    zeros = np.array([])

    def __init__(self, coeff): 
        self.coeff = coeff

    #overload input
    @classmethod
    def from_input(cls):
        return cls(
            np.array([int(i) for i in input("enter coeff with spaces ").split()])
        )

    #add zeros to check
    def add_zeros(self, zeros):
        self.zeros = zeros
    #add zeros to check
    def input_zeros(self):
        self.zeros = np.array([int(i) for i in input("enter zeros with spaces ").split()])
    
    #calc value using gorner method
    def gorner(self, x):
        p = self.coeff[0]
        for a in self.coeff[1:]:
            p = p * x + a
        return p
    #calc value using factorization
    def calc_by_factor(self, x):
        p = 1
        for zero in self.zeros:
            p *= (x - zero)
        return p


def check_accuracy(polynom, interaval):
    difference = np.array([])
    for x in interaval:
        difference = np.append(difference, polynom.gorner(x) - polynom.calc_by_factor(x))
    return difference

def main():
    polynom = poly([1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512])
    polynom.add_zeros([2, 2, 2, 2, 2, 2, 2, 2, 2])
    interaval = np.arange(1.92, 2.08, 10**(-5))

    plt.plot(interaval,check_accuracy(polynom, interaval))
    plt.ylabel('difference')
    plt.xlabel('x value')
    plt.show()

if (__name__ == "__main__"):
    main()