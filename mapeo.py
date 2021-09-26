import gspread
import time
from datetime import datetime
import re
from selenium import webdriver
import pyautogui
import random

credentials = {
  #AQui va las credenciales de tu cuenta de servicio
}


class ScrapearGMaps:
    
     
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe") 
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        gc = gspread.service_account_from_dict(credentials)
        # Abrir por titulo
        sh = gc.open("Trabajo")
        self.worksheet = sh.get_worksheet(1)
        
    def get_name(self):
        try:
            return self.driver.find_element_by_xpath("//h1[contains(@class,'header-title')]").text
        except:
            return ""
        
    def get_address(self):
        try:
            return self.driver.find_element_by_css_selector("[data-item-id='address']").text
        except:
            return ""
        
    def get_phone(self):
        try:
            return self.driver.find_element_by_xpath("//button[contains(@data-item-id,'phone')]").text
        except:
            return ""
        
    def get_website(self):
        try:
            return self.driver.find_element_by_css_selector("[data-item-id='authority']").text
        except:
            return ""
    #precio Básico de 1 a 2 personas por Habitacion
    def get_price(self):
        try:   
                   
            return self.driver.find_element_by_xpath("//div[contains(@class,'Cbys4b')]").text           
        except:
            return ""
    #Valoracion por parte de la ubicacion
    def get_score(self):#puntuacion de la ubicacion, mas no de las personas
        try:   
                    
            return self.driver.find_element_by_xpath("//div[contains(@class,'headline')]").text           
        except:
            return ""
    #Valoracion por parte de las reseñas
    def get_valoration(self):
        try:
            return self.driver.find_element_by_xpath("//div[contains(@class,'gm2-display-2')]").text
        except :
            return ""

    def get_wifi(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Wi-Fi gratis disponible')]").text
            if dato == "Wi-Fi gratis":
                return 1
            else:
                return 0
        except :
            return 0

    def get_piscina(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Piscina disponible')]").text
            if dato == "Piscina":
                return 1
            else:
                return 0
        except :
            return 0

    def get_desayuno(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Desayuno disponible')]").text
            if dato == "Desayuno":
                return 1
            else:
                return 0
        except :
            return 0

    def get_estacionamiento(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Estacionamiento gratuito disponible')]").text
            if dato == "Estacionamiento gratuito":
                return 1
            else:
                return 0
        except :
            return 0

    def get_accesible(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Accesible disponible')]").text
            if dato == "Accesible":
                return 1
            else:
                return 0
        except :
            return 0
    
    def get_aire(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Aire acondicionado disponible')]").text
            if dato == "Aire acondicionado":
                return 1
            else:
                return 0
        except :
            return 0

    def get_lavanderia(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Servicio de lavandería disponible')]").text
            if dato == "Servicio de lavandería":
                return 1
            else:
                return 0
        except :
            return 0

    def get_mascotas(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Se permiten mascotas disponible')]").text
            if dato == "Se permiten mascotas":
                return 1
            else:
                return 0
        except :
            return 0

    def get_habitacion(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Servicio en la habitación disponible')]").text
            if dato == "Servicio en la habitación":
                return 1
            else:
                return 0
        except :
            return 0


    def get_ninos(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Apto para niños disponible')]").text
            if dato == "Apto para niños":
                return 1
            else:
                return 0
        except :
            return 0


    def get_restaurante(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Restaurante disponible')]").text
            if dato == "Restaurante":
                return 1
            else:
                return 0
        except :
            return 0

    def get_spa(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Spa disponible')]").text
            if dato == "Spa":
                return 1
            else:
                return 0
        except :
            return 0

    def get_gimnasio(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Gimnasio disponible')]").text
            if dato == "Gimnasio":
                return 1
            else:
                return 0
        except :
            return 0

    def get_bar(self):
        try:
            dato = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Bar disponible')]").text
            if dato == "Bar":
                return 1
            else:
                return 0
        except :
            return 0

    def zoom_ajust(self):
        time.sleep(3)
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl') 
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')  
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')        
                
    
    def scrape(self, url):
        try:      
            self.driver.get(url)  
            self.zoom_ajust()        
            self.driver.refresh()
            print(url)
            time.sleep(random.randint(3,20))       
            time.sleep(3)
            for j in range(0,3):
                print('nueva iteracion')                                    
                boton = self.driver.find_element_by_id("ppdPk-Ej1Yeb-LgbsSe-tJiF1e")
                self.driver.execute_script("arguments[0].click();", boton)
                for i in range(0,20):    
                    time.sleep(random.randint(3,20))     
                    place = self.driver.find_elements_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")[i]
                    self.driver.execute_script("arguments[0].click();", place)                  
                    time.sleep(random.randint(3,20))          
                    print(len(self.driver.find_elements_by_class_name("M77dve")))
                    if len(self.driver.find_elements_by_class_name("M77dve"))>1:#Condicional para que no surja error al no detectar dicho elemento
                        element = self.driver.find_elements_by_class_name("M77dve")[1]#Condicional que toma el segundo boton del panel
                        time.sleep(3)               
                        self.driver.execute_script("arguments[0].click();", element)   
                    name = self.get_name()
                    time.sleep(random.randint(1,3)) 
                    address = self.get_address()
                    time.sleep(random.randint(1,3)) 
                    phone_number = self.get_phone()
                    website = self.get_website()
                    time.sleep(random.randint(1,3)) 
                    price = self.get_price()
                    time.sleep(random.randint(1,3)) 
                    score = self.get_score()
                    time.sleep(random.randint(1,3)) 
                    valoration = self.get_valoration()   
                    time.sleep(random.randint(1,3))               
                    wifi = self.get_wifi()
                    time.sleep(random.randint(1,3)) 
                    piscina = self.get_piscina()
                    time.sleep(random.randint(1,3)) 
                    desayuno = self.get_desayuno()
                    time.sleep(random.randint(1,3)) 
                    estacionamiento = self.get_estacionamiento()
                    time.sleep(random.randint(1,3)) 
                    accesible = self.get_accesible()
                    time.sleep(random.randint(1,3)) 
                    aire = self.get_aire()
                    time.sleep(random.randint(1,3)) 
                    lavanderia = self.get_lavanderia()
                    time.sleep(random.randint(1,3)) 
                    mascotas = self.get_mascotas()
                    time.sleep(random.randint(1,8)) 
                    habitacion = self.get_habitacion()
                    time.sleep(random.randint(1,3)) 
                    ninos = self.get_ninos()
                    time.sleep(random.randint(1,8)) 
                    restaurante = self.get_restaurante()
                    time.sleep(random.randint(1,3)) 
                    spa = self.get_spa()
                    time.sleep(random.randint(1,8)) 
                    gimnasio = self.get_gimnasio()
                    time.sleep(random.randint(1,8)) 
                    bar = self.get_bar()
                    print(wifi)
                    
                    email = ""                    
                    print([name, address, phone_number, website, price, score, valoration,wifi,piscina,desayuno,estacionamiento,accesible,aire,lavanderia,mascotas,habitacion,ninos,restaurante,spa,gimnasio,bar])                    
                    time.sleep(random.randint(3,20))
                    row_index = len(self.worksheet.col_values(1)) + 1
                    self.worksheet.update_acell('A'+str(row_index), name)
                    self.worksheet.update_acell('B'+str(row_index), address)
                    self.worksheet.update_acell('C'+str(row_index), phone_number) 
                    self.worksheet.update_acell('D'+str(row_index), website)
                    self.worksheet.update_acell('E'+str(row_index), price)
                    self.worksheet.update_acell('F'+str(row_index), email)
                    self.worksheet.update_acell('G'+str(row_index), score)
                    self.worksheet.update_acell('H'+str(row_index), valoration)
                    self.worksheet.update_acell('I'+str(row_index), wifi)
                    self.worksheet.update_acell('J'+str(row_index), piscina)
                    self.worksheet.update_acell('K'+str(row_index), desayuno)
                    self.worksheet.update_acell('L'+str(row_index), estacionamiento)
                    self.worksheet.update_acell('M'+str(row_index), accesible)
                    self.worksheet.update_acell('N'+str(row_index), aire)
                    self.worksheet.update_acell('O'+str(row_index), lavanderia)
                    self.worksheet.update_acell('P'+str(row_index), mascotas)
                    self.worksheet.update_acell('Q'+str(row_index), habitacion)
                    self.worksheet.update_acell('R'+str(row_index), ninos)
                    self.worksheet.update_acell('S'+str(row_index), restaurante)
                    self.worksheet.update_acell('T'+str(row_index), spa)
                    self.worksheet.update_acell('U'+str(row_index), gimnasio)
                    self.worksheet.update_acell('V'+str(row_index), bar)
                    time.sleep(random.randint(3,20)) 
                    element = self.driver.find_element_by_xpath("//button[contains(@class,'searchbox-button')]")
                    time.sleep(3)            
                    self.driver.execute_script("arguments[0].click();", element)                
                time.sleep(random.randint(3,15))
                #boton = self.driver.find_element_by_id("ppdPk-Ej1Yeb-LgbsSe-tJiF1e")
                #self.driver.execute_script("arguments[0].click();", boton)
                time.sleep(3) 
        except Exception as e:
            print(e)
        
        time.sleep(10)
        self.driver.quit()

query = "Hoteles Tacna"
url = "https://www.google.com/maps?q="+query.replace(" ", "+")+"&hl=pe"

gmaps = ScrapearGMaps()
print(gmaps.scrape(url))
