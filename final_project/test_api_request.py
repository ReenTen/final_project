import allure

from final_project.api_request_page import *


@allure.feature('Testing "Pet store"')
class TestApiRequest:

    @allure.story('Add pet to store and than remove it')
    def test_add_and_delete_pet_from_store(self):
        with allure.step('Adding pet to store'):
            add_pet_to_store()
        with allure.step('Checking, that pet add to store'):
            check_add_pet_to_store()
        with allure.step('Deleting pet from store'):
            delete_pet_from_store()
        with allure.step('Checking, that pet delete from store'):
            check_delete_pet_from_store()

    @allure.story('Add user and than change his info')
    def test_add_user_and_change_his_first_name(self):
        with allure.step('Creating user'):
            create_user()
        with allure.step('Checking, that user add'):
            check_add_user()
        with allure.step('Changing user name and e-mail'):
            change_user_info()
        with allure.step('Checking, that new user info has changed'):
            check_change_user_first_name()
