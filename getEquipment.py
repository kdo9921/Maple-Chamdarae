import requests
from bs4 import BeautifulSoup
req = requests.get('https://maplestory.nexon.com/Common/Character/Detail/ApteryxChan/Equipment?p=mikO8qgdC4hElCwBGQ6GOx8CmO11EvduZkV0bRbPAhamMYDAebG0EnF1y5QYmH%2fMO6Jl%2fsaWPSdAN3Ti6mgeiQzlZIIB8GxvbNjkR0p0Q5HAFWaytgXB2JEweaZRvGlwC9Ic6Q3icuUwaRH%2bkHEYra8fSlQCDKVT9CKT7Qu7soB4C65UbUEkcuQsaA%2fL1hO3')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
itemLiHTML = soup.select('.item_pot li')

itemArr = []

for i in range(0,30):
    if len(itemLiHTML[i]) == 0:
        itemArr.append("")
        continue
    itemArr.append(itemLiHTML[i].select('img')[0])

print(itemArr)



