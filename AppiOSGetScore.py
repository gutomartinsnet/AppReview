#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
import requests
import pandas as pd
import numpy as np

#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#s = Service('C:\\webdrivers\\chromedriver.exe')
#driver = webdriver.Chrome(service=s, options=options)

url_score = 'https://apps.apple.com/br/app/poupatempo-digital/id1480051058'

res =  requests.get(url_score)
#res = requests.get(url)
html_source = res.text
soup=BeautifulSoup(html_source, "html.parser")

review_iosscore_src = soup.find('span', {'class','we-customer-ratings__averages__display'})
review_score_list = []
#print(review_score_src)

for val in review_iosscore_src:
    try:
        review_score_list.append(val.get_text())
    except:
        pass
review_score_list[:0]    


g_df2 = pd.DataFrame(np.array(review_score_list),columns=['review_iosscore_src'])
#g_df2 = g_df.join(pd.DataFrame(g_df.pop('review_iosscore_src').tolist()))
#g_df2.head()
print(g_df2)
g_df2.to_csv('pptdigital-apple-reviews-score.csv',encoding='utf-8-sig')
#g_df.to_excel('pptdigital-appgoogle-reviews.xlsx', sheet_name='google play',encoding='utf-8-sig')
