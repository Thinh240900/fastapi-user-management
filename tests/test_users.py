def test_me_endpoint(client):
    res = client.post("/login", data={"username": "test@example.com", "password": "test123"})
    token = res.json()["access_token"]
    res = client.get("/me", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert res.json()["email"] == "test@example.com"
