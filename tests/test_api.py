def test_create_employee(client):
    payload = {
        "name": "Alice Smith",
        "age": 30,
        "department": "IT",
        "designation": "Cloud Architect",
        "salary": 110000,
    }
    response = client.post("/employees", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Alice Smith"
    assert data["age"] == 30
    assert data["department"] == "IT"


def test_list_employees(client):
    client.post(
        "/employees",
        json={
            "name": "John Doe",
            "age": 28,
            "department": "HR",
            "designation": "Manager",
            "salary": 70000,
        },
    )
    client.post(
        "/employees",
        json={
            "name": "Jane Smith",
            "age": 32,
            "department": "IT",
            "designation": "Developer",
            "salary": 85000,
        },
    )

    response = client.get("/employees")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert [employee["name"] for employee in data] == ["John Doe", "Jane Smith"]


def test_get_employee_by_id(client):
    payload = {
        "name": "Alice Smith",
        "age": 30,
        "department": "IT",
        "designation": "Cloud Architect",
        "salary": 110000,
    }
    create_response = client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == employee_id
    assert data["name"] == "Alice Smith"
    assert data["designation"] == "Cloud Architect"


def test_update_employee(client):
    create_response = client.post(
        "/employees",
        json={
            "name": "Alice Smith",
            "age": 30,
            "department": "IT",
            "designation": "Cloud Architect",
            "salary": 110000,
        },
    )
    employee_id = create_response.json()["id"]

    response = client.put(
        f"/employees/{employee_id}",
        json={
            "designation": "Senior Cloud Architect",
            "salary": 125000,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["designation"] == "Senior Cloud Architect"
    assert data["salary"] == 125000


def test_delete_employee(client):
    create_response = client.post(
        "/employees",
        json={
            "name": "Alice Smith",
            "age": 30,
            "department": "IT",
            "designation": "Cloud Architect",
            "salary": 110000,
        },
    )
    employee_id = create_response.json()["id"]

    delete_response = client.delete(f"/employees/{employee_id}")
    assert delete_response.status_code == 204
    assert delete_response.content == b""

    get_response = client.get(f"/employees/{employee_id}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Employee not found"


def test_employee_age_validation(client):
    response = client.post(
        "/employees",
        json={
            "name": "Too Young",
            "age": 17,
            "department": "IT",
            "designation": "Intern",
            "salary": 30000,
        },
    )
    assert response.status_code == 422


def test_get_employee_not_found(client):
    response = client.get("/employees/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"