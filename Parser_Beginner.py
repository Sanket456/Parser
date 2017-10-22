
# coding: utf-8

# In[ ]:




# In[ ]:




# In[42]:

import requests
from bs4 import *
data = requests.get("https://www.accuweather.com/en/in/delhi/202396/daily-weather-forecast/202396")
soup = BeautifulSoup(data.text,'html.parser')
data2 = soup.find('div',{'class':'info'})
data3 = soup.find('span',{'class':'large-temp'})
print(data3.contents)


# In[ ]:



