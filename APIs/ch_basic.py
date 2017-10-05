'''
    Example code using the Companies House API
'''

import requests

api_key = '''---'''
url = '''https://api.companieshouse.gov.uk/search?q=abc&items_per_page=20'''

r = requests.get(url, auth=(api_key,''))

# Print company name and postcode, note sometimes post code is listed as country

print "CompanyName,PostCode"
for i in r.json()['items']:
    if 'postal_code' in i[u'address']:
        print i[u'title']+','+i[u'address'][u'postal_code']
    else:
        print i[u'title']+','+i[u'address'][u'country']

