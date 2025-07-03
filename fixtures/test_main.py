import pytest
from main import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.addUser("emily","emily@gmail.com")
    assert user_manager.addUser("priya","priya@apple.com")

def test_duplicate_add_user(user_manager):
    user_manager.addUser("emily","em@gmail.com")
    with pytest.raises(ValueError):
        user_manager.addUser("emily","em@gmail.com")
def test_get_users(user_manager):
    user_manager.addUser("emily","em@gmail.com")
    print(f"users are {user_manager.getUser('emily')}")
    assert user_manager.getUser('emily')=="em@gmail.com"

