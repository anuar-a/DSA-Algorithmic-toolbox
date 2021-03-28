import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import xlrd
import lxml
import re

string = <a href="http://pvl.kgd.gov.kz/sites/default/files/u1365/o_vozb_dela_o_bankr_i_por_zayav_treb_kred_vrem_128.xlsx"><font face="Arial, Helvetica, sans-serif"><span style="box-sizing: border-box; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; cursor: pointer; line-height: 16px;">Объявления о возбуждении дела о банкротстве и порядке заявления </span></font><font face="Arial, Helvetica, sans-serif"><span style="box-sizing: border-box; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; cursor: pointer; line-height: 16px;">требований кредиторами временному управляющему</span></font></a>

soup = BeautifulSoup(string)
links = soup.find_all(links)
for link in links:
    print(link[text])
