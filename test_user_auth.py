import requests
import pytest


class TestAuthUser:

    def test_auth_user(self):
        data = {"email": "vinkotov@example.com",
                "password": "1234"}

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies
        assert "x-csrf-token" in response1.headers
        assert "user_id" in response1.json()

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]

        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})

        assert "user_id" in response2.json()
        user_id_from_check_method = response2.json()["user_id"]
        assert user_id_from_auth_method == user_id_from_check_method

    exclude_params = [
        "no_cookie",
        "no_token"
    ]

    @pytest.mark.parametrize("condition", exclude_params)
    def negative_auth_check(self, condition):
        data = {"email": "vinkotov@example.com",
                "password": "1234"}

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies
        assert "x-csrf-token" in response1.headers
        assert "user_id" in response1.json()

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")

        if condition == "no_cookie":
            response2 = requests.post("https://playground.learnqa.ru/api/user/login", headers=token)
        else:
            response2 = requests.post("https://playground.learnqa.ru/api/user/login", cookies=auth_sid)

        assert "user_id" in response2.json()
        user_id_from_check_method = response2.json()["user_id"]
        assert user_id_from_check_method == 0
