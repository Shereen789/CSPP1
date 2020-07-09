import os,sys
sys.path.append(os.getcwd())
from solution import add
import pytest

@pytest.mark.parametrize('x,y,result',[
    (10,10,20),(1,5,6),(6,6,12)
])
def test_add(x,y,result):
    assert add(x,y) == result