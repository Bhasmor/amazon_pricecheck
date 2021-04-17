import requests
from bs4 import BeautifulSoup
import smtplib
import time

bot_email = input("Bot Emaili: ")
bot_sifre = input("Bot Sifresi: ")
URL = input("Url giriniz: ")
price_holder = float(input("Fiyatı kaça düşerse haber vereyim: "))
e_mail = input("Hangi email e göndereyim: ")
second_holder = int(input("Kaç saniyede bir kontrol edilsin: "))
boolplace_holder = True

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52"
}

def price_check(URL, max_price):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    price = soup.find(id="priceblock_ourprice").getText().strip()

    pricedot_check = price[1:-1].replace(".","")
    new_price = float(pricedot_check[0:-1].replace(",","."))

    print(new_price)

    if(new_price <= max_price):
        send_email("TO_EMAIL",URL)
    else: 
        print("urun fiyati dusmedi!")



def send_email(toMail, url):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(bot_email,bot_sifre)


    body = 'Urun linki: ' + url
    body = body.encode('utf-8')
    msg = f'Subject:\n\n{body}'

    server.sendmail(
        bot_email,
        e_mail,
        msg
    )
    print("mesaj gonderildi")  
    server.quit() 



while(boolplace_holder):
    price_check(URL,price_holder)
    time.sleep(second_holder)
