
import main

def test_set_path():
    main.app.testing = True
    client = main.app.test_client()
    r = client.get('/set_path?base_path=https://domain.xyz/path/')
    assert r.status_code == 200

def test_get_file():
    main.app.testing = True
    client = main.app.test_client()
    r = client.get('/get_file/abcd.xyz')
    assert r.status_code == 200
    
