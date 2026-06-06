def test_register(client):
    response = client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "12345678"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login(client):
    # لازم نسجل الأول
    client.post("/auth/register", json={
        "username": "loginuser",
        "email": "login@example.com",
        "password": "12345678"
    })

    response = client.post("/auth/login", json={
        "email": "login@example.com",
        "password": "12345678"
    })

    assert response.status_code == 200
    data = response.json()

    assert "access_token" in data
    assert "refresh_token" in data


def test_refresh_token(client):
    # register + login
    client.post("/auth/register", json={
        "username": "refreshuser",
        "email": "refresh@example.com",
        "password": "12345678"
    })

    login_res = client.post("/auth/login", json={
        "email": "refresh@example.com",
        "password": "12345678"
    })

    refresh_token = login_res.json()["refresh_token"]

    response = client.post("/auth/refresh", json={
        "refresh_token": refresh_token
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
    


def test_refresh_with_access_token(client):

    client.post("/auth/register", json={
        "username": "user3",
        "email": "user3@test.com",
        "password": "password123"
    })

    login = client.post("/auth/login", json={
        "email": "user3@test.com",
        "password": "password123"
    })

    access_token = login.json()["access_token"]

    response = client.post(
        "/auth/refresh",
        json={"refresh_token": access_token}
    )

    assert response.status_code == 401    