
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from selenium import webdriver



import time
import os

class WppBot:

    def __init__(self):

        self.nombre_contacto = "Contacto"

        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-es")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

self.ultimo_texto = ''

def whatsapp(self):    
    self.driver.get('https://web.whatsapp.com/')    
    time.sleep(20)
    target = self.driver.find_element_by_xpath(f"//span[@title='{self.nombre_contacto}']")    
    time.sleep(3)    
    target.click()

    def escucha(self):
        post = self.driver.find_elements_by_class_name('z_tTQ')
        ultimo = len(post) - 1
        texto = post[ultimo].find_elements_by_css_selector('span.selectable-text')
        self.texto = texto[len(texto)-1].text
        return self.texto

    def bot(self):
        chatbot = ChatBot("Tob")
        trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.spanish.conversations')

    while True:
        texto = self.escucha()
        texto = str(texto)
        if texto != self.ultimo_texto and texto[0] != ':':
            self.ultimo_texto = texto
            user_input = texto
            self.bot_response = chatbot.get_response(user_input)
            chatBox = self.driver.find_element_by_class_name("_3uMse")
            time.sleep(3)
            chatBox.click()
            chatBox.send_keys(":" + str(self.bot_response))
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)   
 
            botao_enviar.click()
            time.sleep(5)


bot = WppBot()
bot.whatsapp()
time.sleep(30)
bot.bot()