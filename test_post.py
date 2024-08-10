import pytest
import requests
import allure


@allure.feature("User Management")
@allure.suite("Create Single User")
@allure.title("Create a new user and verify response")
@allure.description("This test case creates a new user using the ReqRes API and verifies the response.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_create_a_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/users',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 201'):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response_data has required fields: name, job, id, createdAt'):
        assert 'name' in response_data, "The response does not contain 'name'"
        assert 'job' in response_data, "The response does not contain 'job'"
        assert 'id' in response_data, "The response does not contain 'id'"
        assert 'createdAt' in response_data, "The response does not contain 'createdAt'"

    with allure.step('Verify the name and job fields match the input data'):
        assert response_data['name'] == data['name'], f"Expected name {data['name']} but got {response_data['name']}"
        assert response_data['job'] == data['job'], f"Expected job {data['job']} but got {response_data['job']}"

    with allure.step('Attach the response payload to the Allure report'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)
