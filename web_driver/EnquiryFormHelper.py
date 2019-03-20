from Web import Web
import time

class EnquiryFormHelper():

    #__url = "http://blazedemo.com/"
    __url = "https://5shoesonloose.com"

    def Open(self):
        self._web.open(self.__url)

    def __init__(self, browser):
        self._web = Web(browser)

    def click_customize_button(self):
        self._web.get_web_element_by_xpath("(//*[contains(text(),'Customize Your Trip')])[1]").click()
        time.sleep(3)

    def enter_name(self, name):
        self._web.get_web_element_by_xpath("//*[@name='name']").send_keys(name)

    def enter_phone(self, phone):
        self._web.get_web_element_by_xpath("//*[@name='phone']").send_keys(phone)

    def enter_email(self, email):
        self._web.get_web_element_by_xpath("//*[@name='email']").send_keys(email)
        time.sleep  

    def select_no_of_people(self, noOfPeople):
        try:
            self._web.get_web_element_by_xpath("//input[@value='No. of People']").click()
            time.sleep(3)
            self._web.get_web_element_by_xpath("//div[contains(@class,'NoOfAdults')]//li/span[contains(text(),'{}')]".format(noOfPeople)).click()
            time.sleep(2)
        except Exception as e:
            print(e)

    def select_trip_begin(self, trip_begin):
        try:
            self._web.get_web_element_by_xpath("//input[@value='I will book']").click()
            time.sleep(3)
            self._web.get_web_element_by_xpath("//div[contains(@class,'duration')]//li/span[contains(text(),'{}')]".format(trip_begin)).click()
            time.sleep(2)
        except Exception as e:
            print(e)

    def select_trip_location(self,location):    
        self._web.get_web_element_by_xpath("//input[@value='Trip Location*']").click()
        time.sleep(2)
        self._web.get_web_element_by_xpath("//div[contains(@class,'location1')]//li/span[contains(text(),'{}')]".format(location)).click()
        time.sleep(2)

    def select_random_date(self):
        self._web.selectDate()    

    def Close(self):
        self._web.close_all()