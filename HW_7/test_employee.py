from employee_api import EmployeeApi


base_url = "http://5.101.50.27:8000"


def test_create_employee():
    api = EmployeeApi(base_url)

    employee_data = {
        "first_name": "Tom",
        "last_name": "Hart",
        "middle_name": "Test",
        "company_id": 1,
        "email": "tom.hart.test@example.com",
        "phone": "+491111111111",
        "birthdate": "2000-01-01",
        "is_active": True
    }

    result = api.create_employee(employee_data)

    assert result["first_name"] == employee_data["first_name"]
    assert result["last_name"] == employee_data["last_name"]
    assert result["company_id"] == employee_data["company_id"]
    assert result["email"] == employee_data["email"]
    assert result["phone"] == employee_data["phone"]
    assert result["is_active"] is True


def test_get_employee_info():
    api = EmployeeApi(base_url)

    employee_id = 1

    employee = api.get_employee_info(employee_id)

    assert employee["first_name"] == "Иван"
    assert employee["last_name"] == "Иванов"
    assert employee["email"] == "ivan@example.com"


def test_change_employee_info():
    api = EmployeeApi(base_url)

    employee_id = 2

    new_employee_data = {
        "last_name": "Potter",
        "email": "harry@test.com",
        "phone": "+49111111111",
        "is_active": True
    }

    result = api.change_employee_info(
        employee_id,
        new_employee_data,
        "harrypotter",
        "expelliarmus"
    )

    assert result["last_name"] == new_employee_data["last_name"]
    assert result["email"] == new_employee_data["email"]
    assert result["phone"] == new_employee_data["phone"]
    assert result["is_active"] == new_employee_data["is_active"]
