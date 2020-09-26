from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Teste de bot, nada demais"
        self.grupos = ["teste", "Emanuel"]  # Nome do grupo
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # Faz a repetição com os grupos indicados
        # Caso ele faça muito rapidamente ele vai trava, por isso o tempo de espera
        self.driver.get('https://web.whatsapp.com/')
        # Tempo para que ele consiga escanear o HTML
        time.sleep(50)

        for grupo in self.grupos:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
