def test_get_user_ok(client, seed_data):
    r = client.get("/api/v1/user/1")
    assert r.status_code == 200
    assert r.json()["name"] == "John"

def test_get_user_404(client):
    r = client.get("/api/v1/user/9999")
    assert r.status_code == 404

