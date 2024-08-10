import pytest
import requests
import allure


@allure.feature("User Management")
@allure.suite("User Login")
@allure.title("Login with valid credentials and verify the response")
@allure.description(
    "This test case logs in a user using the ReqRes API with valid credentials and verifies the response for successful authentication.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_login_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/login',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "token" field'):
        assert 'token' in response_data, "The response does not contain 'token'"

    with allure.step('Verify that "token" is not empty'):
        assert response_data['token'], "The 'token' field is empty"

    with allure.step('Attach the response payload to the Allure report'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)
