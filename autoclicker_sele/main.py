from selenium import webdriver
import time

chrome_driver_path="C:\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5   # 5 minutes from now

cookie = driver.find_element_by_id("cookie")

while True:

    cookie.click()

    if time.time() > timeout:

        store = driver.find_elements_by_css_selector("#store b")
        cost = []
        for value in store:
            value_text=value.text
            if value_text!="":
                price=int(value_text.split("-")[1].strip().replace(",", ""))
                cost.append(price)
        print(cost)
        score=driver.find_element_by_id("money").text
        if "," in score:
            score = score.replace(",", "")
        score=int(score)

        for c in cost:
            if score<c:
                position=cost.index(c)
                break
        pos=position-1
        if pos>=0:
            i=item_ids[pos]
            print(score)
            print(i)
            click=driver.find_element_by_id(i)
            click.click()

        timeout = time.time() + 3
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break