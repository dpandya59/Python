import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n= ToastNotifier()

def getdata (url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://weather.com/en-IN/weather/today/l/2dc216a1b519028193aeef24008f270371e2fa792823856039d3ba3aba4c3c64")#https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/") 
  
soup = BeautifulSoup(htmldata,'html.parser')
current_temp=soup.find_all(class_="CurrentConditions--tempValue--MHmYY")
# print(current_temp)
temp =''
for i in current_temp:
    temp+=i.get_text()
    # print(i.get_text())
# temp =str(current_temp.get_text())
print(temp)
result = "current_temp " + temp 
print(result)

n.show_toast("live Weather update",  
     result, duration = 10) 