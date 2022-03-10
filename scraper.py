from warnings import catch_warnings
import requests
from bs4 import BeautifulSoup
import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # server login credentials hidden

    subject = 'An item is on sale on Sephora.com!'
    body = 'The following item is on sale at Sephora!\n%s\n%s\nSale price: $%.2f\nRegular price: $%.2f\nSavings: $%.2f' % (detail1,detail2,spToFloat,float(ns[1:10]),diff)
    link = 'Click to shop: https://www.sephora.com/ca/en/product/pro-filt-r-hydrating-longwear-foundation-P448702?skuId=2268316&icid2=skugrid:p448702:product'

    msg = f"Subject: {subject}\n\n{body}\n\n{link}"
    server.sendmail(
        'lolm3ky@gmail.com',
        'meekybritanico96m@gmail.com',
        msg
    )
    print('Notification sent!')
    server.quit()


# URL = 'https://en.wikipedia.org/wiki/Main_Page'
URL = 'https://www.sephora.com/ca/en/product/pro-filt-r-hydrating-longwear-foundation-P448702?skuId=2268316&icid2=skugrid:p448702:product'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")


brandName = soup.find_all('a', {'class': 'css-1gyh3op e65zztl0'})
detail1 = brandName[0].get_text()
# print(brandName[0].get_text())

product = soup.find_all('span', {'class': "css-1pgnl76 e65zztl0"})
detail2 = product[0].get_text()
# print(product[0].get_text())

# check if id for sale items exists on page. if yes notify by email 
# ----- if item on sale -----
try:
    salePrice = soup.find_all('b', {'class':"css-5fq4jh"})
    sp = salePrice[0].get_text()
    spToFloat = float(sp[1:10])
    noSale = soup.find_all('b', {'class': "css-vc9b2"})
    ns = noSale[0].get_text()
    diff = float(ns[1:10])-spToFloat
    # print('The following item is on sale at Sephora!\n%s \nSale price: $%.2f\nRegular price: $%.2f\nSavings: $%.2f' % (detail1,spToFloat,float(ns[1:10]),diff))
    send_mail()

# ------ regular priced item ------
except:
    regPrice = soup.find_all('b', {'class': "css-0"})
    rp = regPrice[0].get_text()
    rpToFloat = float(rp[1:10])
    # print(rpToFloat)
    print('This item is regular price for $' + str(rpToFloat))
