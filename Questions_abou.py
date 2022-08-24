from datetime import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class  Questions_about: #Блок "Вопросы о важном" и ответы
    how_much = [By.XPATH, '/html/body/div/div/div/div[5]/div[2]/div/div[1]/div[1]']
    rubles_400=[By.XPATH, '//*[@id="accordion__panel-0"]']

    several_at_once = [By.XPATH, '/html/body/div/div/div/div[5]/div[2]/div/div[2]/div[1]']
    one_scooter = [By.XPATH, '//*[@id="accordion__panel-1"]']

    time_is_calculated = [By.XPATH, '/html/body/div/div/div/div[5]/div[2]/div/div[3]/div[1]']
    rental_period = [By.XPATH, '//*[@id="accordion__panel-2"]']

    as_of_today = [By.XPATH, '/html/body/div/div/div/div[5]/div[2]/div/div[4]/div[1]']
    tomorrow = [By.XPATH, '//*[@id="accordion__panel-3"]']

    renew_the_order = [By.XPATH, '/html/body/div/div/div/div[5]/div[2]/div/div[5]/div[1]']
    change_is_not_possible = [By.XPATH, '//*[@id="accordion__panel-4"]']

    exercises_with = [By.XPATH, '/html/body/div/div/div/div[5]/div[2]/div/div[6]/div[1]']
    without_charging = [By.XPATH, '//*[@id="accordion__panel-5"]']

    cancel_order = [By.XPATH, '/html/body/div/div/div/div[5]/div[2]/div/div[7]/div[1]']
    cancellation_of_order = [By.XPATH, '//*[@id="accordion__panel-6"]']

    live_far_away = [By.XPATH, '/html/body/div/div/div/div[5]/div[2]/div/div[8]/div[1]']
    bringing = [By.XPATH, '//*[@id="accordion__panel-7"]']



    def __init__(self, driver):
        self.driver = driver
    #
    # def click_sign_in_button(self):
    #     self.driver.find_element(*self.sign_in_button).click()
    @allure.step('Клик вопроса Сколько это стоит? И как оплатить?')
    def clik_how_much(self):
        self.driver.find_element(*self.how_much).click()

    def wait_clik_how_much(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.how_much))

    @allure.step('Ожидание ответа Сутки — 400 рублей. Оплата курьеру — наличными или картой.')
    def wait_rubles_400(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.rubles_400))

    @allure.step('Клик вопроса Хочу сразу несколько самокатов! Так можно?')
    def clik_several_at_once(self):
        self.driver.find_element(*self.several_at_once).click()

    def wait_several_at_once(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.several_at_once))

    @allure.step('Ожидание ответа  Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
    def wait_one_scooter(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.one_scooter))

    @allure.step('Клик вопроса Как рассчитывается время аренды?')
    def clik_time_is_calculated(self):
        self.driver.find_element(*self.time_is_calculated).click()

    def wait_time_is_calculated(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.time_is_calculated))

    @allure.step('Ожидание ответа Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    def wait_rental_period(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.rental_period))

    @allure.step('Клик вопроса Можно ли заказать самокат прямо на сегодня?')
    def clik_as_of_today(self):
        self.driver.find_element(*self.as_of_today).click()

    def wait_as_of_today(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.as_of_today))

    @allure.step('Ожидание ответа Только начиная с завтрашнего дня. Но скоро станем расторопнее.')
    def wait_tomorrow(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.tomorrow))

    @allure.step('Клик вопроса Можно ли продлить заказ или вернуть самокат раньше?')
    def clik_renew_the_order(self):
        self.driver.find_element(*self.renew_the_order).click()

    def wait_renew_the_order(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.renew_the_order))

    @allure.step('Ожидание ответа Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')
    def wait_change_is_not_possible(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.change_is_not_possible))

    @allure.step('Клик вопроса Вы привозите зарядку вместе с самокатом?')
    def clik_exercises_with(self):
        self.driver.find_element(*self.exercises_with).click()

    def wait_exercises_with(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.exercises_with))

    @allure.step('Ожидание ответа Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
    def wait_without_charging(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.without_charging))

    @allure.step('Клик вопроса Можно ли отменить заказ?')
    def clik_cancel_order(self):
        self.driver.find_element(*self.cancel_order).click()

    def wait_cancel_order(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.cancel_order))

    @allure.step('Ожидание ответа Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')
    def wait_cancellation_of_order(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.cancellation_of_order))

    @allure.step('Клик вопроса Я жизу за МКАДом, привезёте?')
    def clik_live_far_away(self):
        self.driver.find_element(*self.live_far_away).click()

    def wait_live_far_away(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.live_far_away))

    @allure.step(
        'Ожидание ответа Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    def wait_bringing(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.bringing))


    def test_check_text_rubles_400(self):  # Сутки — 400 рублей. Оплата курьеру — наличными или картой.
        return self.driver.find_element(*self.rubles_400).text

    def test_check_text_one_scooter(self):  # Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.
        return self.driver.find_element(*self.one_scooter).text

    def test_check_text_rental_period(self):  # Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.
        return self.driver.find_element(*self.rental_period).text

    def test_check_text_tomorrow(self):  # Только начиная с завтрашнего дня. Но скоро станем расторопнее.
        return self.driver.find_element(*self.tomorrow).text

    def test_check_text_change_is_not_possible(self):  # Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.
        return self.driver.find_element(*self.change_is_not_possible).text

    def test_check_text_without_charging(self):  # Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.
        return self.driver.find_element(*self.without_charging).text

    def test_check_text_cancellation_of_order(self):  # Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.
        return self.driver.find_element(*self.cancellation_of_order).text

    def test_check_text_bringing(self):  # Да, обязательно. Всем самокатов! И Москве, и Московской области.
        return self.driver.find_element(*self.bringing).text




