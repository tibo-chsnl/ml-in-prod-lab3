import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app import is_integer

def test_is_integer():
    assert is_integer("10") == True
    assert is_integer("-5") == True
    assert is_integer("0") == True
    assert is_integer("3.14") == False
    assert is_integer("abc") == False
    assert is_integer("") == False