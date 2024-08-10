import pytest
import requests
import allure


@allure.feature("User Management")
@allure.suite("Update User")
@allure.title("Update an existing user's job and verify the response")
@allure.description(
    "This test case updates the job of an existing user using the ReqRes API and verifies the response for successful update.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.patch(
        'https://reqres.in/api/users/2',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "name", "job", and "updatedAt" fields'):
        assert 'name' in response_data, "The response does not contain 'name'"
        assert 'job' in response_data, "The response does not contain 'job'"
        assert 'updatedAt' in response_data, "The response does not contain 'updatedAt'"

    with allure.step('Verify the name and job fields match the input data'):
        assert response_data['name'] == data['name'], f"Expected name {data['name']} but got {response_data['name']}"
        assert response_data['job'] == data['job'], f"Expected job {data['job']} but got {response_data['job']}"

    with allure.step('Verify "updatedAt" is not empty'):
        assert response_data['updatedAt'], "The 'updatedAt' field is empty"

    with allure.step('Attach the response payload to the Allure report'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)
