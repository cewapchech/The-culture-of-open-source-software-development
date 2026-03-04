import sys
sys.path.append("../src")
#TODO make it with 'pip install -e'

from math_demo import(add, 
                      add_with_bug, 
                      calculate_tax_with_bug,
                      calculate_tax)

def test_addition ():
    assert add(2,2) ==4,"function did not return 4"
    print("Test BASIC ADDITION PASSED")

def test_addition_with_bug ():
    assert add_with_bug(2,2) ==4,"function did not return 4"
    assert add_with_bug(0,0) ==0
    print("Test BASIC ADDITION PASSED (does it mesn cod ok&))")

def test_addition_duplicated():
    assert add(2,3)==2+3

def test_addition_overcomplicsted():
    for i in range(0,2**320):
        for j in range(0,2**32):
            assert add(i,j)==sum([i,j])
            assert add(-i,j)==sum([-i,j])
            assert add(i,-j)==sum([i,-j])
            assert add(-i,-j)==sum([-i,-j])

def test_addition_reasonable():
    assert add(2,2)==4
    assert add(0,0)==0
    assert add(6,7)==13
    assert add(-6,-7)==-13
    assert add(6,-7)==-1
    assert add(7,0)==7
    assert add(-7,0)==-7
    print("Test BASIC ADDITION PASSED")

def test_tax_calucation_pesticised():
    assert calculate_tax_with_bug(1000)==150.0
    assert calculate_tax_with_bug(100)==15.0
    assert calculate_tax_with_bug(10)==1.5
    assert calculate_tax_with_bug(1)==0.15
    assert calculate_tax_with_bug(-200)==-30.0
    assert calculate_tax_with_bug(0)==0.0
    print("Test TAX PASSED")

def test_tax_calucation():
    assert calculate_tax(0)==0

if __name__=="__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    test_addition_overcomplicsted()
    test_tax_calucation()
    test_tax_calucation_pesticised()