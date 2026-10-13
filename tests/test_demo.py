
import pytest

def test_login_success():
    assert 1 + 1 == 2

def test_login_failure():
    # 故意让测试失败
    assert 1 == 2

def test_add():
    assert 10 + 20 == 30
