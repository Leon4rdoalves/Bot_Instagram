from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint, choice


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cont = 0
        self.driver = webdriver.Firefox(executable_path=r"/usr/local/bin/geckodriver")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        sleep(randint(4, 7))

        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        sleep(randint(4, 6))

        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        sleep(randint(3, 5))

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        sleep(randint(3, 6))

        password_element.send_keys(Keys.RETURN)
        sleep(randint(2, 5))

        self.coment("caricaturaspersonalizadas")  # wacom, wacomcintiq

    @staticmethod
    def digitando(frase, caixa):
        for letra in frase:
            caixa.send_keys(letra)
            sleep(randint(1, 5) / 30)

    def coment(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(randint(7, 10))

        for i in range(1, 4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(randint(3, 6))

        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " Fotos carregadas: " + str(len(pic_hrefs)))
        print(f'Quantidade de fotos comentadas: {self.cont}')
        print('\n')

        while True:
            for pic_href in pic_hrefs:
                try:
                    pic_href.index("https://www.instagram.com/p")
                except ValueError as err:
                    print("pulando link inválido")
                    continue
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(randint(4, 7))

                try:
                    comentarios = ['Muito legal seu trabalho!', 'Parabéns, muito legal seu trabalho.',
                                   'Caricaturas digitais com preço promocional! Solicite seu orçamento.',
                                   'Veja meu perfil e solicite seu orçamento!', 'Top!', 'Muito legal :)',
                                   'Curte caricaturas? Da uma olhada no meu perfil, estamos em promoção!',
                                   'Legal!!!', 'Que maneiro!!!', 'Putz, muito maneiro rs!', ':)', ':o', ':D',
                                   'Ta rolando sorteio para meus seguidores, so vem!', 'Show', 'Q top',
                                   'Aí galera, minhas caricaturas estão em promoção, solicite seu orçamento',
                                   'Gostei, bons traços!', ':D', 'Curti (y)', 'Caraca, muito bom', 'Maneiro',
                                   'Dá uma olhada na minha galeria, tenho uns desenhos legais tbm!', 'Show!!!',
                                   'Bem feito', 'Bem legal!', 'Legal, eu tbm faço algumas e estamos em promoção!']

                    driver.find_element_by_class_name('Ypffh').click()
                    sleep(randint(5, 8))
                    campo_comentario = driver.find_element_by_class_name('Ypffh')
                    sleep(randint(8, 13))
                    self.digitando(choice(comentarios), campo_comentario)
                    sleep(randint(30, 40))
                    driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                    sleep(randint(10, 15))
                    self.cont += 1

                except Exception as e:
                    print(e)
                    sleep(randint(5, 7))


ebony_coment_bot = InstaBot('seu usuário', 'sua senha')
ebony_coment_bot.login()
