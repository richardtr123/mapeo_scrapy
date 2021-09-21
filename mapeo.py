import gspread
import time
from datetime import datetime
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import random

credentials = {
  #Colocar tus credenciales aqui, ejemplo de como obtenerlo
  #https://www.youtube.com/watch?v=A1URtaaA-v0&t=0s&ab_channel=NicolasMarinTorres
  #el archivo con extension .json, copiar su contenido aquí
}


class ScrapearGMaps:
    
    data = {}
    worksheet = {}
    
    def __init__(self):
        # Ruta de ChromeDriver
        #self.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe") 
        self.driver = webdriver.Chrome(executable_path="ruta del chromedriver.exe") 
        # self.driver.get('chrome://settings/')
        # self.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.5);')   
        # self.driver.get(url)
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        gc = gspread.service_account_from_dict(credentials)
        # Abrir por titulo
        sh = gc.open("Trabajo")
        # Seleccionar primera hoja
        self.worksheet = sh.get_worksheet(0)
        
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
            # print(self.driver.find_element_by_xpath("//div[contains(@class,'Cbys4b')]").text)         
            return self.driver.find_element_by_xpath("//div[contains(@class,'Cbys4b')]").text           
        except:
            return ""
    #Valoracion por parte de la ubicacion
    def get_score(self):#puntuacion de la ubicacion, mas no de las personas
        try:   
            # print(self.driver.find_element_by_xpath("//div[contains(@class,'Cbys4b')]").text)         
            return self.driver.find_element_by_xpath("//div[contains(@class,'headline')]").text           
        except:
            return ""
    #Valoracion por parte de las reseñas
    def get_valoration(self):
        try:
            return self.driver.find_element_by_xpath("//div[contains(@class,'gm2-display-2')]").text
        except :
            return ""

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
            #print(self.driver.page_source)
            time.sleep(random.randint(3,20))       
            time.sleep(3)
            for j in range(0,3):
                element = self.driver.find_element_by_id("ppdPk-Ej1Yeb-LgbsSe-tJiF1e")
                self.driver.execute_script("arguments[0].click();", element)
                print('nueva iteracion')
                time.sleep(random.randint(3,20))        
                for i in range(0,20):    
                    time.sleep(random.randint(3,20))     
                    place = self.driver.find_elements_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")[i]
                    #place = self.driver.find_element_by_xpath("(//a[contains(@class,'a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')])")
                    self.driver.execute_script("arguments[0].click();", place)
                    #place.click()                    
                    time.sleep(random.randint(3,20))                    
                    name = self.get_name()
                    time.sleep(random.randint(1,3)) 
                    address = self.get_address()
                    phone_number = self.get_phone()
                    website = self.get_website()
                    time.sleep(random.randint(1,3)) 
                    price = self.get_price()
                    score = self.get_score()
                    time.sleep(random.randint(1,3)) 
                    valoration = self.get_valoration()
                    email = ""
                    #if website != "":
                    #    email = self.get_email('http://'+website)
                    
                    print([name, address, phone_number, website, email, price, score, valoration])
                    
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
                    time.sleep(random.randint(3,20)) 
                    element = self.driver.find_element_by_xpath("//button[contains(@class,'searchbox-button')]")
                    time.sleep(3)               
                    self.driver.execute_script("arguments[0].click();", element)
                    

                time.sleep(random.randint(3,20))  
                
            
        except Exception as e:
            print(e)
        
        time.sleep(10)
        self.driver.quit()

query = "Veterinanias Tacna"
url = "https://www.google.com/maps?q="+query.replace(" ", "+")+"&hl=pe"

gmaps = ScrapearGMaps()
print(gmaps.scrape(url))
