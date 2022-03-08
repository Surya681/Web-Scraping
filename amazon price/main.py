import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.in/dp/B097MG6HVP/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=f053b5835866dcaa2028eaeda8f9cda5&hsa_cr_id=5359662720402&pd_rd_plhdr=t&pd_rd_r=b780b6b2-1705-41f2-b2e0-88e876a36998&pd_rd_w=7Yrsk&pd_rd_wg=EhpF3&ref_=sbx_be_s_sparkle_mcd_asin_1_img"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()

price_without_currency = price.split(".")[0]
price_without_currency=price_without_currency.replace(',', '')
price_as_float = float(price_without_currency)
print(price_as_float)

import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 10500

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )