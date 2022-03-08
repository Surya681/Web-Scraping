from selenium import webdriver

chrome_driver_path="C:\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")



fname=driver.find_element_by_name("fName")
fname.send_keys("Python")
lname=driver.find_element_by_name("lName")
lname.send_keys("Programmer")
email=driver.find_element_by_name("email")
email.send_keys("Pythonprogram@gmail.com")
btn=driver.find_element_by_class_name("btn")
# btn.send_keys(Keys.ENTER)
btn.click()