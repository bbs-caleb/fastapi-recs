def test_get_post_ok(client, seed_data):
    r = client.get("/api/v1/post/10")
    assert r.status_code == 200
    assert r.json()["topic"] == "business"

def test_get_post_404(client):
    r = client.get("/api/v1/post/9999")
    assert r.status_code == 404

