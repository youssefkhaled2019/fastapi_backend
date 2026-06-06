from core.config import settings

def get_tokens(client):
    client.post("/auth/register", json={
        "username": "user1",
        "email": "user1@example.com",
        "password": "12345678"
    })

    login = client.post("/auth/login", json={
        "email": "user1@example.com",
        "password": "12345678"
    })

    return login.json()


# =========================
def test_get_me(client):
    tokens = get_tokens(client)

    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {tokens['access_token']}"}
    )

    assert response.status_code == 200
    assert response.json()["email"] == "user1@example.com"


# =========================
def test_create_user(client):
    response = client.post("/users/", json={
        "username": "newuser",
        "email": "new@example.com",
        "password": "12345678"
    })

    assert response.status_code == 200
# =========================

def test_update_user(client):

    # create user
    create = client.post(
        "/auth/register",
        json={
            "username": "youssef",
            "email": "youssef@test.com",
            "password": "12345678"
        }
    )

    user_id = create.json()["id"]

    # update
    response = client.put(
        f"/users/{user_id}",
        json={
            "username": "newname",
            "email": "new@test.com",
            "password": "87654321"
        }
    )

    assert response.status_code == 200
    assert response.json()["username"] == "newname"
    assert response.json()["email"] == "new@test.com"
# =========================
def test_patch_user(client):

    create = client.post(
        "/auth/register",
        json={
            "username": "patchuser",
            "email": "patch@test.com",
            "password": "12345678"
        }
    )

    user_id = create.json()["id"]

    response = client.patch(
        f"/users/{user_id}",
        json={
            "username": "patched"
        }
    )

    assert response.status_code == 200
    assert response.json()["username"] == "patched"

# =========================
def get_admin_token(client):

    login = client.post(
        "/auth/login",
        json={
            "email": f"{settings.TEST_ADMIN_EMAIL}",
            "password":f"{settings.TEST_ADMIN_PASSWORD}"
        }
    )

    return login.json()["access_token"]

def test_delete_user(client):

    create = client.post(
        "/auth/register",
        json={
            "username": "deleteuser",
            "email": "delete@test.com",
            "password": "12345678"
        }
    )

    user_id = create.json()["id"]

    token = get_admin_token(client)

    response = client.delete(
        f"/users/{user_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "User deleted successfully"
    }    
# =========================

def test_delete_user_not_found(client):

    token = get_admin_token(client)

    response = client.delete(
        "/users/99999",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404    
# =========================
def test_get_users_admin(client):

    login = client.post(
        "/auth/login",
        json={
            "email": f"{settings.TEST_ADMIN_EMAIL}",
            "password":  f"{settings.TEST_ADMIN_PASSWORD}"
        }
    )

    token = login.json()["access_token"]

    response = client.get(
        "/users/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

# =========================
def test_register_duplicate_email(client):

    data = {
        "username": "user1",
        "email": "user1@test.com",
        "password": "password123"
    }

    client.post("/auth/register", json=data)

    response = client.post("/auth/register", json=data)

    assert response.status_code == 400

# =========================
def test_login_wrong_password(client):

    client.post("/auth/register", json={
        "username": "user2",
        "email": "user2@test.com",
        "password": "password123"
    })

    response = client.post("/auth/login", json={
        "email": "user2@test.com",
        "password": "wrong"
    })

    assert response.status_code == 400    

# =========================
def test_get_user_not_found(client):

    response = client.get("/users/9999")

    assert response.status_code == 404    
# =========================

def test_update_user_not_found(client):

    response = client.put(
        "/users/9999",
        json={
            "username":"x",
            "email":"x@test.com",
            "password":"password123"
        }
    )

    assert response.status_code == 400    
# =========================
def test_me_without_token(client):

    response = client.get("/users/me")

    assert response.status_code == 401    