from pepallow.allow import Allow
from pepallow.peps.p231 import AssetBean as Bean

with Allow(211):
    s = [1, 2, 3]
    t = "abc"
    for i, j in s @ t:
        print(f"{i}{j}")
        
with Allow(231):
    b = Bean(3)
    assert b.foo == 3
    b.foo = 4
    assert b.foo == 4

with Allow(313):
    assert IV + I == V
    assert VI + M == 1006
    assert (M - D) + VI - X == (500) + 6 - 10
    
