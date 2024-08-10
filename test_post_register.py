import pytest
import requests
import allure


@allure.feature("User Management")
@allure.suite("User Registration")
@allure.title("Register a new user and verify the response")
@allure.description(
    "This test case registers a new user using the ReqRes API and verifies the response for successful registration.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_register_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/register',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "id" and "token" fields'):
        assert 'id' in response_data, "The response does not contain 'id'"
        assert 'token' in response_data, "The response does not contain 'token'"

    with allure.step('Verify that "id" is not empty'):
        assert response_data['id'], "The 'id' field is empty"

    with allure.step('Verify that "token" is not empty'):
        assert response_data['token'], "The 'token' field is empty"

    with allure.step('Attach the response payload to the Allure report'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)
