from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Explicit wait - waiting for a specific condition like an element is available. 
# Implicit wait - waiting for a specified time without any condition.

# Explicit wait should be used when there is an element that it takes more time to load it, 
# implicit wait is used when it takes time for all elements on page to load

class GreenKartShopper:

    def setUp(self):
        
        self.browser = webdriver.Chrome()

        #I'm using implicit wait here to give time for the whole page to load
        self.browser.implicitly_wait(10)

        self.browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        
    def finishShopping(self):
        
        self.browser.quit()    

    def goToCart(self):
        cart_icon = self.browser.find_element(By.CLASS_NAME, 'cart-icon')
        cart_icon.click()

        proceed_to_checkout = self.browser.find_element(By.CLASS_NAME, 'action-block')
        proceed_to_checkout.click()

    def applyDiscount(self, promoCode):

        promo_code = self.browser.find_element(By.CLASS_NAME, 'promoCode')
        promo_code.send_keys(promoCode)
                     
        promo_button = self.browser.find_element(By.CLASS_NAME, 'promoBtn')
        promo_button.click()

        #Explicit wait is used here - wait until string Code applied is shown meaning discount was applied successfully        
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))
    
    def searchAndAddToCart(self, name, number):
        products = self.browser.find_elements(By.CLASS_NAME, 'product')
        for product in products:

            product_name = product.text
            
            if name.lower() in product_name.lower():

                #set number of the items
                stepper_input = product.find_element(By.CLASS_NAME, 'stepper-input')
                stepper_input.find_element(By.CLASS_NAME, 'quantity').clear()
                stepper_input.find_element(By.CLASS_NAME, 'quantity').send_keys(number)

                #get the button and click
                add_button = product.find_element(By.CLASS_NAME, 'product-action')
                add_button.click()   

                return True    

        return False

    def shop(self, items, promoCode):

        for item in items:
            if not self.searchAndAddToCart(item, items[item]):
                return False
                    
        self.goToCart()
        self.applyDiscount(promoCode)


shopper = GreenKartShopper()
shopper.setUp()

shoppinglist = {"Cucumber" : 1, "Tomato" : 2, "Carrot" : 1}

shopper.shop(shoppinglist, "rahulshettyacademy")

shopper.finishShopping()

