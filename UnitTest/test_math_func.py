from UnitTest.math_func import StudentDB
import pytest

@pytest.fixture(scope='module')
def db():
    print('----------setup Method----------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('----------teardown Method----------------')
    db.close()

def test_kiran1_data(db):
    kiran1_data = db.get_data('kiran1')
    assert kiran1_data['id'] == 5
    assert kiran1_data['name'] == 'kiran1'
    assert kiran1_data['result'] == 'pass'

def test_kiran2_data(db):
    kiran2_data = db.get_data('kiran2')
    assert kiran2_data['id'] == 10
    assert kiran2_data['name'] == 'kiran2'
    assert kiran2_data['result'] == 'fail'