import pytest
import requests
import allure

@allure.feature("User Management")
@allure.suite("Delete Single User")
@allure.title("Delete a user and verify response")
@allure.description("This test case deletes an existing user and verifies the response.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_delete_user():
    headers = {'Content-Type': 'application/json'}

    response = requests.delete(
        'https://reqres.in/api/users/2',
        headers= headers
    )

    with allure.step('Verify the response status code is 204'):
        assert response.status_code == 204, f"Expected status code 204 but got {response.status_code}"