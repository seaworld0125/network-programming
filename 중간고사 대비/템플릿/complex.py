var_comp = 3+2j
print(var_comp, type(var_comp))

print(var_comp.real, var_comp.imag)
print(var_comp.conjugate())

class MyComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

if __name__ == '__main__':
    print('example')