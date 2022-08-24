import time


import driver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


from Order import OrderLowerButton
from Questions_abou import Questions_about

import allure

class TestQuestionsAbout:
    driver=None

    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Firefox()

    @allure.title(
        'проверяем ответ на вопрос Сколько это стоит? И как оплатить?')
    def test_how_much(self): #Сколько это стоит? И как оплатить?
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions=Questions_about(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.wait_clik_how_much()
        questions.clik_how_much()
        questions.wait_rubles_400()
        text_answer=questions.test_check_text_rubles_400()

        assert text_answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.', 'Овет не верен'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title(
        'проверяем ответ на вопрос Хочу сразу несколько самокатов! Так можно?')
    def test_several_at_once(self): #Хочу сразу несколько самокатов! Так можно?
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions=Questions_about(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        questions.wait_several_at_once()
        questions.clik_several_at_once()
        questions.wait_one_scooter()
        text_answer=questions.test_check_text_one_scooter()

        assert text_answer == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.', 'Овет не верен'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title(
        'проверяем ответ на вопрос Как рассчитывается время аренды?')
    def test_time_is_calculated(self): #Как рассчитывается время аренды?
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions=Questions_about(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.wait_time_is_calculated()
        questions.clik_time_is_calculated()
        questions.wait_rental_period()
        text_answer=questions.test_check_text_rental_period()

        assert text_answer == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.', 'Овет не верен'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title(
        'проверяем ответ на вопрос Можно ли заказать самокат прямо на сегодня?')
    def test_as_of_today(self): #Можно ли заказать самокат прямо на сегодня?
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions=Questions_about(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.wait_as_of_today()
        questions.clik_as_of_today()
        questions.wait_tomorrow()
        text_answer=questions.test_check_text_tomorrow()

        assert text_answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.', 'Овет не верен'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title(
        'проверяем ответ на вопрос Можно ли продлить заказ или вернуть самокат раньше?')
    def test_renew_the_order(self): #Можно ли продлить заказ или вернуть самокат раньше?
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions=Questions_about(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.wait_renew_the_order()
        questions.clik_renew_the_order()
        questions.wait_change_is_not_possible()
        text_answer=questions.test_check_text_change_is_not_possible()

        assert text_answer == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.', 'Овет не верен'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title(
        'проверяем ответ на вопрос Вы привозите зарядку вместе с самокатом?')
    def test_exercises_with(self): #Вы привозите зарядку вместе с самокатом?
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions=Questions_about(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.wait_exercises_with()
        questions.clik_exercises_with()
        questions.wait_without_charging()
        text_answer=questions.test_check_text_without_charging()

        assert text_answer == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.', 'Овет не верен'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title(
        'проверяем ответ на вопрос Можно ли отменить заказ?')
    def test_cancel_order(self): #Можно ли отменить заказ?
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions=Questions_about(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.wait_cancel_order()
        questions.clik_cancel_order()
        questions.wait_cancellation_of_order()
        text_answer=questions.test_check_text_cancellation_of_order()

        assert text_answer == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.', 'Овет не верен'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title(
        'проверяем ответ на вопрос Я жизу за МКАДом, привезёте?')
    def test_live_far_away(self): #Я жизу за МКАДом, привезёте?
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions=Questions_about(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.wait_live_far_away()
        questions.clik_live_far_away()
        questions.wait_bringing()
        text_answer=questions.test_check_text_bringing()

        assert text_answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.', 'Овет не верен'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()




def assertTrue(param):
    pass


def assertMultiLineEqual(param, text_order):
    pass


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Заказ через нижнюю кнопку Заказать')
    def test_lower_button_order(self): #Заказ через нижнюю кнопку Заказать
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        lower_button=OrderLowerButton(self.driver)
        elementToFocus = self.driver.find_element(By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
        self.driver.execute_script("arguments[0].focus();", elementToFocus)
        lower_button.click_kyki()
        lower_button.click_lower_button_order()
        lower_button.wait_clik_how_much()
        lower_button.text_input_name_Nina()
        lower_button.text_input_last_name_Pechurkina()
        lower_button.text_input_address_Lenina_5()
        lower_button.click_metro()
        lower_button.click_cherkizovo()
        lower_button.text_phone_Nina()
        lower_button.click_button_next()
        lower_button.wait_about_rent()
        lower_button.text_when_bring_Nina()
        lower_button.click_rental_period()
        lower_button.click_calendar_day()
        lower_button.click_color()
        lower_button.click_black_pearl()
        lower_button.text_сommentary_Nina()
        lower_button.click_total_order()
        lower_button.wait_place_an_order()
        lower_button.click_button_yes()
        text=lower_button.test_check_see_status()

        assert text== 'Посмотреть статус'

        lower_button.click_check_see_status()
        lower_button.click_logo_scooter()
        lower_button.wait_image()

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        lower_button.click_logo_yandex()
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)

        assert self.driver.current_url == 'https://yandex.ru/'

    @allure.title('Заказ через верхнюю кнопку Заказать')
    def test_upper_button_order(self): #Заказ через верхнюю кнопку Заказать

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        lower_button = OrderLowerButton(self.driver)

        # lower_button.click_kyki()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollDown);")
        lower_button.click_upper_button_order()
        lower_button.text_input_name_Vasja()
        lower_button.text_input_last_name_Ivanov()
        lower_button.text_input_address_Sovetskaja_5()
        lower_button.click_metro()
        lower_button.click_paveleckaja()
        lower_button.text_phone_Vasja()
        lower_button.click_button_next()
        lower_button.wait_about_rent()
        lower_button.text_when_bring_Vasja()
        lower_button.click_rental_period()
        lower_button.click_calendar_day()
        lower_button.click_color()
        lower_button.click_grey_pearl()
        lower_button.text_сommentary_Vasja()
        lower_button.click_total_order()
        lower_button.wait_place_an_order()
        lower_button.click_button_yes()
        text=lower_button.test_check_see_status()

        assert text== 'Посмотреть статус'


        lower_button.click_check_see_status()
        lower_button.click_logo_scooter()
        lower_button.wait_image()

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        lower_button.click_logo_yandex()
        time.sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)

        assert self.driver.current_url == 'https://yandex.ru/'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()







