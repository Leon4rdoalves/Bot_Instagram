from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"/usr/local/bin/geckodriver")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        sleep(5)

        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        sleep(4)

        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        sleep(3)
        user_element.send_keys(self.username)
        sleep(2)

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        sleep(2)

        password_element.send_keys(Keys.RETURN)
        sleep(3)

        self.like("desenho")  # Hashtag a ser procurada

    def like(self, hashtag):
        # total = subtotal = 0
        cont = 0
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(7)

        for i in range(1, 4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)

        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        print('\n')
        # print(f'Total de fotos curtidas: {total}')
        # print(f'Fotos curtidas neste sprint: {subtotal}\n')

        while True:
            for pic_href in pic_hrefs:
                try:
                    pic_href.index("https://www.instagram.com/p")
                except ValueError as err:
                    print("pulando link inválido")
                    continue
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)

                try:
                    sleep(5)
                    driver.find_element_by_xpath('//button[@class="wpO6b "]').click()
                    sleep(25)
                    cont += 1
                    print(cont)

                except Exception as e:
                    print(e)
                    sleep(5)


ebony = InstaBot('usuário', 'senha')
ebony.login()
