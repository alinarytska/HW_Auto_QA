import requests


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_token(self, user, password):
        creds = {
            "username": user,
            "password": password
        }

        resp = requests.post(
            self.url + "/auth/login",
            json=creds
        )

        assert resp.status_code == 200, f"Ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]

    def create_employee(self, employee_data):
        resp = requests.post(
            self.url + "/employee/create",
            json=employee_data
        )

        assert resp.status_code == 200, f"Ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_employee_info(self, employee_id):
        resp = requests.get(
            self.url + f"/employee/info/{employee_id}"
        )

        assert resp.status_code == 200, f"Ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def change_employee_info(self, employee_id, employee_data, user, password):
        client_token = self.get_token(user, password)

        resp = requests.patch(
            self.url + f"/employee/change/{employee_id}?client_token={client_token}",
            json=employee_data
        )

        assert resp.status_code == 200, f"Ожидался статус 200, получен {resp.status_code}"
        return resp.json()
