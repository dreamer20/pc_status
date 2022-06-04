from pc_status import create_app

def test_app():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
