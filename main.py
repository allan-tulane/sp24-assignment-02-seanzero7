"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

#Was able to use the same function from lab 3 as I thoguht that was the original assignment 

def subquadratic_multiply(x, y):
  xvec = x.binary_vec
  yvec = y.binary_vec
  xvec, yvec = pad(xvec, yvec)
  if x.decimal_val <= 1 and y.decimal_val <= 1:
    return BinaryNumber(x.decimal_val*y.decimal_val)
  x_left, x_right = split_number(xvec)
  y_left, y_right = split_number(yvec)
  a = subquadratic_multiply(x_left, y_left)
  b = subquadratic_multiply(x_right, y_right)
  c1 = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
  c2 = BinaryNumber(y_left.decimal_val + y_right.decimal_val)
  c = BinaryNumber((subquadratic_multiply(c1, c2).decimal_val - a.decimal_val - b.decimal_val))
  a = bit_shift(a, len(xvec))
  c = bit_shift(c, len(xvec)//2)
  return BinaryNumber(a.decimal_val + c.decimal_val + b.decimal_val)


def time_multiply(x, y, f):
  start = time.time()
  result = f(x, y)
  end = time.time()
  print(result)
  return (end - start) * 1000

print(subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)))
    

