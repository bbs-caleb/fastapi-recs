def test_recommendations(client, seed_data):
    r = client.get("/api/v1/post/recommendations/?id=1&limit=5")
    assert r.status_code == 200
    posts = r.json()
    assert posts[0]["id"] == 10  # у поста 10 больше всего лайков

