import test_first
def test_testing():
    output=test_first.findarea(12,12)
    assert output==144
    # assert output==142
    
def test():
    output=test_first.findname()
    assert output=="aswanth"   
    
# def test1():
#     output=test_first.findname()
#     assert output=="aswanh"      