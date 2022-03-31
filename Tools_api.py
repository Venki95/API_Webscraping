from bs4 import BeautifulSoup
import requests
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

apiPages = []
f = csv.writer(open('API.CSV', 'w'))
f.writerow(['API Name', 'API Url', 'API Description', 'API Category'])

for i in range(0,65):
    url = 'https://www.programmableweb.com/category/tools/api' + '?pw_view_display_id=apis_all&page=' +  str(i)
    apiPages.append(url)

for apis in apiPages:
    request = requests.get(apis,headers=headers)
    content = request.text
    soup = BeautifulSoup(content, "html.parser")
    for api in soup.select('[class="odd views-row-first"],[class="even"],[class="odd"],[class="odd views-row-last"]'):
        apiName = api.find("td",{"class":"views-field views-field-title"}).text
        urls = api.find("td",{"class":"views-field views-field-title"})
        apiUrl = urls.find("a").get("href")
        apiDescription = api.find("td",{"class":"views-field views-field-field-api-description"}).text
        apiCategory = api.find("td",{"class":"views-field views-field-field-article-primary-category"}).text
        f.writerow([apiName,apiUrl,apiDescription,apiCategory])