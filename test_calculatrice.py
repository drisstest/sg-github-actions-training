from calculatrice import addition, division

def test_addition():
    assert addition(2, 3) == 5

def test_addition_negatif(): 
    assert addition(-1, -1) == -2
    
def test_division():
    assert division(6, 2) == 3
    
def test_division_zero():
    try:
        division(6, 0)
        assert False 
    except ValueError:
        assert True
    