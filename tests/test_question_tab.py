import allure
import pytest
from locators.tabs_questions_locator import QaScooterQuestions as QSQ
from pages.base_page import BasePage



class TestClickQuestion:

    @allure.step('Проверка раздела "Вопросы о важном"')
    @pytest.mark.parametrize('answer, tab', zip(QSQ.questions, QSQ.tab_answer))
    def test_tab_question(self,driver,tab,answer):
        tabs_page = BasePage(driver)
        tabs_page.scroll_element(answer)
        tabs_page.click_element(answer)
        assert tabs_page.display_locator(tab)

