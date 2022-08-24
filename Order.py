
import random

import allure
import driver
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class OrderLowerButton: #Блок Заказ через нижнюю кнопку Заказать
    lower_button_order= [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'] #Нижняя кнопка Заказать
    upper_button_order_= [By.XPATH, '/html/body/div/div/div/div[1]/div[2]/button[1]'] #Верхняя кнопка Заказать
    kyki=[By.XPATH, '//*[@id="rcc-confirm-button"]']
    order_form= [By.XPATH, '//div[@class="Order_Header__BZXOb"]'] #Для кого самокат
    input_name=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/input'] #Поле ввода имени
    input_last_name=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/input'] #Поле ввода фамилии
    input_address = [By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/input']  # Поле ввода адреса
    metro=[By.XPATH, '//input[@class="select-search__input"]']  # Поле метро
    cherkizovo= [By.XPATH, './/button/div[text()="Черкизовская"]']  # Метро Черкизовская
    paveleckaja=[By.XPATH, './/button/div[text()="Павелецкая"]']  # Метро Павелецкая
    phone=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[5]/input']  #Телефон
    button_next=[By.XPATH, '/html/body/div/div/div[2]/div[3]/button']  #Кнопка далее
    about_rent=[By.XPATH, '/html/body/div/div/div[2]/div[1]']  # Про аренду
    when_bring=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/input']  # Когда привезти
    rental_period=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/span']  # Срок аренды
    calendar = [By.XPATH, './/div[text()="сутки"]']
    color=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]']
    black_pearl=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/label[1]']
    grey_pearl=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/label[2]']
    сommentary=[By.XPATH, '/html/body/div/div/div[2]/div[2]/div[4]/input']
    total_order=[By.XPATH, '/html/body/div/div/div[2]/div[3]/button[2]']
    place_an_order=[By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button[2]']
    button_yes=[By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button[2]']
    see_status=[By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button']
    logo_scooter=[By.XPATH, '/html/body/div/div/div[1]/div[1]/a[2]/img']
    image=[By.XPATH, '/html/body/div/div/div/div[2]/div[4]']
    logo_yandex=[By.XPATH, '/html/body/div/div/div/div[1]/div[1]/a[1]/img']
    search_button=[By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/dqs/div/div/div/div[2]/form/div[2]/button']
    close=[By.XPATH, '/html/body/div[2]/div/div/div/div/div[5]']




    def __init__(self, driver):
        self.driver = driver

    def wait_search_lower_button_order(self):
        WebDriverWait(driver, 10).until(element_to_be_clickable(self.lower_button_order))

    @allure.step('Клик куков :)')
    def click_kyki(self):
        self.driver.find_element(*self.kyki).click()

    @allure.step('Клик по нижней кнопке Заказать')
    def click_lower_button_order(self):
        self.driver.find_element(*self.lower_button_order).click()

    @allure.step('Клик по нижней кнопке Заказать')
    def click_upper_button_order(self):
        self.driver.find_element(*self.lower_button_order).click()

    @allure.step('Ожидание появление элемента Для кого самокат')
    def wait_clik_how_much(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order_form))

    @allure.step('Заполняем поле имя, Нина')
    def text_input_name_Nina(self, list_name=None):
        self.driver.find_element(*self.input_name).send_keys('Нина')

    @allure.step('Заполняем поле имя, Вася')
    def text_input_name_Vasja(self, list_name=None):
        self.driver.find_element(*self.input_name).send_keys('Вася')

    @allure.step('Заполняем поле фамилия, Печуркина')
    def text_input_last_name_Pechurkina(self, list_last_name=None):
        self.driver.find_element(*self.input_last_name).send_keys('Печуркина')

    @allure.step('Заполняем поле фамилия, Иванов')
    def text_input_last_name_Ivanov(self, list_last_name=None):
        self.driver.find_element(*self.input_last_name).send_keys('Иванов')

    @allure.step('Заполняем поле адрес, Ленина, 5')
    def text_input_address_Lenina_5(self, list_address=None):
        self.driver.find_element(*self.input_address).send_keys('Ленина, 5')

    @allure.step('Заполняем поле адрес, Советская, 5')
    def text_input_address_Sovetskaja_5(self, list_address=None):
        self.driver.find_element(*self.input_address).send_keys('Советская, 5')

    @allure.step('Клик по полю Метро')
    def click_metro(self):
        self.driver.find_element(*self.metro).click()

    @allure.step('Выбор из выпадающего списка станции метро Черкизово')
    def click_cherkizovo(self):
        self.driver.find_element(*self.cherkizovo).click()

    @allure.step('Выбор из выпадающего списка станции метро Павелецкая')
    def click_paveleckaja(self):
        self.driver.find_element(*self.paveleckaja).click()

    @allure.step('Заполнение поля телефон')
    def text_phone_Nina(self):
        self.driver.find_element(*self.phone).send_keys(89995559966)

    @allure.step('Заполнение поля телефон')
    def text_phone_Vasja(self):
        self.driver.find_element(*self.phone).send_keys(88886665555)

    @allure.step('Клик кнопки Далее')
    def click_button_next(self):
        self.driver.find_element(*self.button_next).click()

    @allure.step('Ожидание появление элемента Про аренду')
    def wait_about_rent(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.about_rent))

    @allure.step('Заполнение поля дата заказа')
    def text_when_bring_Nina(self):
        self.driver.find_element(*self.when_bring).send_keys('25.08.2022')

    @allure.step('Заполнение поля дата заказа')
    def text_when_bring_Vasja(self):
        self.driver.find_element(*self.when_bring).send_keys('15.09.3333')

    @allure.step('Клик на поле срок аренды')
    def click_rental_period(self):
        self.driver.find_element(*self.rental_period).click()

    @allure.step('Выбор срока аренды')
    def click_calendar_day(self):
        self.driver.find_element(*self.calendar).click()

    @allure.step('Клик на поле выбора цвета самоката')
    def click_color(self):
        self.driver.find_element(*self.color).click()

    @allure.step('Выбор чёрного самоката')
    def click_black_pearl(self):
        self.driver.find_element(*self.black_pearl).click()

    @allure.step('Выбор серого самоката')
    def click_grey_pearl(self):
        self.driver.find_element(*self.grey_pearl).click()

    @allure.step('Заполнение поля Комментарии')
    def text_сommentary_Nina(self):
        self.driver.find_element(*self.сommentary).send_keys('Когда-нибудь я научусь прикручивать генераторы')

    @allure.step('Заполнение поля Комментарии')
    def text_сommentary_Vasja(self):
        self.driver.find_element(*self.сommentary).send_keys('И с ассёртами я подружусь')

    @allure.step('Клик кнопки Заказа')
    def click_total_order(self):
        self.driver.find_element(*self.total_order).click()

    def wait_place_an_order(self):
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
                self.place_an_order))

    @allure.step('Клик кнопки Да')
    def click_button_yes(self):
        self.driver.find_element(*self.button_yes).click()

    def test_check_order_placed(self):
        return self.driver.find_element(*self.order_placed).text

    def test_check_see_status(self):
        return self.driver.find_element(*self.see_status).text

    @allure.step('Клик кнопки Посмотреть статус заказа')
    def click_check_see_status(self):
        return self.driver.find_element(*self.see_status).click()

    @allure.step('Клик лого Самоката')
    def click_logo_scooter(self):
        return self.driver.find_element(*self.logo_scooter).click()

    def wait_image(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.image))

    @allure.step('Клик лого Яндекса')
    def click_logo_yandex(self):
        return self.driver.find_element(*self.logo_yandex).click()

    def wait_search_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.search_button))

    def wait_close(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.close))

    def click_close(self):
        return self.driver.find_element(*self.close).click()

    def send_keys(self, param):
        pass

