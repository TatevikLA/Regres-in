import pytest
import requests
import allure


@allure.feature("User API")
@allure.suite("Get User List")
@allure.title("Get the list of users from page 2")
@allure.description("Test to get the list of users from page 2 and validate the response structure and content.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_list_users():
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        'https://reqres.in/api/users?page=2',
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "page", "per_page", "total", and "total_pages" fields'):
        assert 'page' in response_data, "The response does not contain 'page'"
        assert 'per_page' in response_data, "The response does not contain 'per_page'"
        assert 'total' in response_data, "The response does not contain 'total'"
        assert 'total_pages' in response_data, "The response does not contain 'total_pages'"

    with allure.step('Verify "page" is 2'):
        assert response_data['page'] == 2, f'Expected page 2 but got {response_data["page"]}'

    with allure.step('Verify "data" field is a list and contains 6 users'):
        assert isinstance(response_data['data'], list), "'data' should be a list"
        assert len(response_data['data']) == 6, f'Expected 6 users but got {len(response_data["data"])}'

    with allure.step('Verify each user has required fields: id, email, first_name, last_name, avatar'):
        for user in response_data['data']:
            assert 'id' in user, "User does not contain 'id'"
            assert 'email' in user, "User does not contain 'email'"
            assert 'first_name' in user, "User does not contain 'first_name'"
            assert 'last_name' in user, "User does not contain 'last_name'"
            assert 'avatar' in user, "User does not contain 'avatar'"

    with allure.step('Verify the response contains "support" field'):
        assert 'support' in response_data, "The response does not contain 'support'"

    with allure.step('Verify "support" field contains "url" and "text"'):
        assert 'url' in response_data['support'], "'Support' does not contain 'url'"
        assert 'text' in response_data['support'], "'Support' does not contain 'text'"
