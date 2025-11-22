import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from app import is_integer

def test_is_integer():
    assert is_integer("10")
    assert is_integer("-5")
    assert is_integer("0")
    assert not is_integer("3.14")
    assert not is_integer("abc")
    assert not is_integer("")