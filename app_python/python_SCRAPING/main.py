import requests
import json
from bs4 import BeautifulSoup

class CapturarNindo:
    def capturandoNindo(self):
        res = requests.get("https://steamcommunity.com/sharedfiles/filedetails/?l=hungarian&id=1548022827")
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, 'html.parser')
        info = soup.select('div.workshopItemTitle')

        if info != [] or info != None:
            descricao = info[0].text
        return descricao
