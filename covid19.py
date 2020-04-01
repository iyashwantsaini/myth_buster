import bs4 as bs
import requests

def request(url):
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"
	}
	return requests.get(url,headers=headers)

url = "https://www.worldometers.info/coronavirus/"

try:
	r = request(url)
except:
	print("Url not found")

r = request(url)

soup = bs.BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())

tb = soup.find('table',{'id':'main_table_countries_today'})

head = tb.thead.tr.findAll('th')

result = {}

for i in head:
	result[i.text] = []

#print(result)
'''
Country,Other
TotalCases
NewCases
TotalDeaths
NewDeaths
TotalRecovered
ActiveCases
Serious,Critical'''

tem_body = tb.tbody.findAll('tr')

for body in tem_body:
	row = body.findAll('td')
	try:
		result['Country,Other'].append(row[0].a.text)
	except:
		result['Country,Other'].append(row[0].text)
	result['TotalCases'].append(row[1].text)
	result['NewCases'].append(row[2].text)
	result['TotalDeaths'].append(row[3].text)
	result['NewDeaths'].append(row[4].text)
	result['TotalRecovered'].append(row[5].text)
	result['ActiveCases'].append(row[6].text)
	result['Serious,Critical'].append(row[7].text)

print(result['Serious,Critical'])
