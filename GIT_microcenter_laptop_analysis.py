import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time
import random
import undetected_chromedriver as uc


    
class laptop:
    def __init__(self):
        self.laptops_dict = {} # this is where I will store all of the laptop data
        
    def initialize_driver(self,url,chrome_driver_path):
        def regular_chrome_driver(url,chrome_driver_path):# this is for the regular selenium chrome
            s = Service(chrome_driver_path) # Change with your path
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            #options.add_argument('--headless') #cannot use this, as the bot detection detects when the browser is headless
            driver = webdriver.Chrome(service=s, options=options)
            return driver
            
        def undetected_chromedriver(url,chrome_driver_path): # this is the undetected_chromedriver, which is used to simulate a human
            uc_options = uc.ChromeOptions()
            uc_options.add_argument("--start-maximized")
            driver = uc.Chrome(headless=False,use_subprocess=True,options=uc_options)
            return driver
        
        #call whichever chromedriver you would like.  
        self.driver = regular_chrome_driver(url,chrome_driver_path)
        self.driver.implicitly_wait(7)
        self.driver.get(url)
        time.sleep(1)
       
    def get_elements(self):
        self.laptops = self.driver.find_elements(By.XPATH,"//div[@class='normal']")  #Find all elements that match the class "normal".  All of the laptop entries have this class within them.  We are using this to create a list of all the laptop entries on the page 
        return self.laptops
        
    def get_data(self):
        for p in range(len(self.laptops)): #The self.laptops is a list of selenium elements.  We need to extract the data within each element
            rating =self.laptops[p].find_elements(By.XPATH,"//div[@class='bv_averageRating_component_container']") #Within each laptop in self.laptops, we pull out the rating (out of 5) that is listed
            price = self.laptops[p].find_elements(By.XPATH,"//div[@class='price']") #Within each laptop in self.laptops, we pull out the Price that is listed
            
            name, a, b, c, d = self.laptops[p].text.split(";") #We pull the text from the laptop element, which will be the title of each laptop entry and split it by ";" to each each component of the laptop
            try:# we have to filter out the entries that don't have a rating
                self.laptops_dict[name] = (a,b,c,d,price[p].text,rating[p].text) #Store the laptop components, rating, and price in a dictionary
            except:# the no ratings entries will filter into here (index error)
                rating_text = "no ratings"
                self.laptops_dict[name] = (a,b,c,d,price[p].text,rating_text) #Store the laptop components, rating, and price in a dictionary
        print("Page successfully scraped")
        print(f"Number of entries scraped: {len(self.laptops_dict.keys())}")
        
    def assign_variable(self, a,b,c,d): # This function is used to split the specs into the right variable
        variable_list = [a,b,c,d]
        
        ### These are the keywords that are often used to define each spec component
        cpu_checker = ['Processor','CPU',"Chip"]
        gpu_checker = ['Graphics','GPU','GDDR6', 'GeForce', 'NVIDIA']
        ram_checker = ['RAM','Memory','memory']
        harddrive_checker = ['Solid State Drive', 'SSD','Storage']
        cpu = ""
        gpu = ""
        ram = ""
        hd = ""
        for spec in variable_list:
            placer = False
            for check in cpu_checker:
                if check in spec:
                    cpu = spec
                    placer = True
                    continue
            if placer == True:
                continue
            for check in gpu_checker:
                if check in spec:
                    gpu = spec
                    placer = True   
                    continue
            if placer == True:
                continue
            for check in ram_checker:
                if check in spec:
                    ram = spec
                    placer = True
                    continue
            if placer == True:
                continue
            for check in harddrive_checker:
                if check in spec:
                    hd = spec
                    placer = True
                    continue
        for variable in [cpu,gpu,ram,hd]:
            if variable == "":
                variable = 'NULL'
            
        return cpu,gpu,ram,hd
        
    def insert_into_df(self): #This is just used to test which laptops were included within the web scraping
        self.df = pd.DataFrame(columns=['name','cpu_processor','graphics_card','ram','harddrive','rating','original_price','current_price','money_saved','discount_percent']) # create a dataframe using these columns
        i = 0 # This is used to index in the dataframe.  We need to match each entry with this index
        for laptop,specs in self.laptops_dict.items(): # go through the dictionary and see the name of the laptop and its individual specs
            a,b,c,d,price,rating = specs #split the specs into their individual components
            price = price.split('\n') # there are two prices in the variable price, one for the original price and one for the current price.  We need to split them into separate variables
            if len(price) != 4: # if there are both the original price and the current price present, the len of the string split will be 4.  We look for the ones that does not have the len of 4, which means only the current price is available and there was no original price
                og_price = "No previous price" # since there is no original price, we make the og_price variable as "No previous price"
                now_price = price[1] # we keep the current price the same
            elif len(price) == 4: # these will be the entries with both original and current price.
                og_price = price[1]
                now_price = price[3]
                
            cpu, gpu, ram, hd= self.assign_variable(a,b,c,d) # we call the assign variable to assign the variables to the right spec component
            self.pandas_dataframe(i,laptop,cpu,gpu,ram,hd,og_price,now_price,rating) # input the name, specs, rating, and prices into the create dataframe function
            i+=1 
            
    def first_page(self,url,chrome_driver_path): # This is for the first page of the search query
        self.initialize_driver(url,chrome_driver_path) #Create the chrome driver using chrome_driver_path and having the driver launch the url
        time.sleep(4)
        laptops = self.get_elements() #Call the get_elements function within the class
        if len(laptops) > 0: # if the laptop elements are found, this will confirm it
            print("Page 1")
            print("\n")
            print("Laptop elements found")
            
        else: # if the laptop elements are not found, this will confirm it

            print("No laptop elements found")
            self.driver.quit()
            return False
        time.sleep(4)
        self.get_data() # call the get_data function
        time.sleep(2)
        self.insert_into_df()       
        
    def next_page(self, i,url, chrome_driver_path): #We want to scrape all of the pages within this query search on the site
        
        self.driver.quit() #close the browser to avoid getting bot detected
        time.sleep(2.5)

        self.initialize_driver(url,chrome_driver_path) # create another browser with the next page url
        time.sleep(4)
        laptops = self.get_elements()

        if len(laptops) == 0:# This is a check to see if the page has laptop entries on it
            return False # if not we return out of the function
        print('\n')
        print(f"Page {i}")
        print("\n")
        print("Laptop elements found")
        
        time.sleep(4)
        
        self.get_data()
        
        time.sleep(2)
        
        self.insert_into_df()
        

        
    def pandas_dataframe(self,i,name, cpu, gpu, ram,hd, og_price, now_price,rating): # this is where we clean up the data 
        try:
            og_price = og_price.replace(",","") # we replace the "," in the prices with a blank 
            og_price = float(og_price[1:])# convert to float
        except: # there are some entries without an original price, so we use this to check if it had a original price 
            pass
        
        now_price = now_price.replace(",","") 
        now_price = float(now_price[1:])
        
        try: 
            price_difference = og_price - now_price # we calculate the price difference 
        except:
            price_difference = "No previous price" # if there was no original price, we label the original price "No previous price"
        
        try:
            discount_percent =round((1- (now_price / og_price)) * 100),2  
        except:
            discount_percent = "No discount"
        self.df.loc[i] = [name,cpu,gpu,ram,hd,rating,og_price,now_price,price_difference,discount_percent] # we insert the data into the dataframe at index [i]

def main():
    url = r'https://www.microcenter.com/search/search_results.aspx?N=4294967288&NTK=all&sortby=match&rpp=96' # Microcenter website that the program is trying to scrape
    chrome_driver_path = #Change with your path 
    MC = laptop() #Initialize a new instance of the laptop class. (MC abbreviation for microcenter)
    first_page = MC.first_page(url, chrome_driver_path) # 
    if first_page == False:
        exit()
    i = 2
    while True: #place holder loop because we do not know how many pages there will be  
        try:
            next_page_link = fr'https://www.microcenter.com/search/search_results.aspx?N=4294967288&NTK=all&sortby=match&rpp=96&page={i}&cat=Laptops/Notebooks-:-MicroCenter'
            next_page = MC.next_page(i,next_page_link,chrome_driver_path) #Call the next page function.  We are looking to scrape all of the pages within this query search
            if next_page == False:
                print("Bot detected")
                break
            time.sleep(6)
        except:
            break
        i +=1
        
    print(MC.df)
    MC.df.to_csv('microcenter_laptop_analysis.csv') # we want to save the dataframe to a csv for easier access 

if __name__ == "__main__":
    main() #call the main function