import pytest
import requests



class TestFirstAPI:
    names = [
        ("Valeriy"),
        ("Arseniy"),
        ("Terentiy"),
        ("")
    ]

    @pytest.mark.parametrize("name", names)
    def test_call_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, f"Response status code is {response.status_code}, not 200"

        response_dict = response.json()
        assert "answer" in response_dict, f"There is no field 'answer' in response"
        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, f"Actual response text is not correct"
