from __matrix import *

m1 = Matrix(3, 3)
m2 = Matrix(3, 3)

m1.setFromArray(
    [
        [1, 0, 0], 
        [5, 0, 8], 
        [0, 0, 0]
    ]
)

m2.setFromArray(
    [
        [1, 0, 0], 
        [1, 0, 0], 
        [1, 0, 0]
    ]
)

print('Matrix 1');
m1.print()
print('Matrix 2');
m2.print()
print('Adding those matrices results in');
m1.add(m2).print()