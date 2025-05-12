def test_register_and_login(client):
    res = client.post("/register", json={"email": "test@example.com", "password": "test123"})
    assert res.status_code == 200
    res = client.post("/login", data={"username": "test@example.com", "password": "test123"})
    assert res.status_code == 200
    assert "access_token" in res.json()
