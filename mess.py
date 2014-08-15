from mechanize import Browser
from bs4 import BeautifulSoup
import urllib2

mess_priority=[
    'SGR (Normal Menu)',
    'SGR (Jain Food)',
    'SK',
    'Cauvery',
    'Mandakini'
]
br = Browser()
page = br.open('http://students2.iitm.ac.in:3000/boys')


br.select_form(nr=0)
soup = BeautifulSoup( page.read() )

a = set(soup.find_all('option'))
pri = []
print a
for p in mess_priority:
    for k in a:
        if p == k.get_text():
            pri.append(k.get('value'))
print pri

br.form["username"] = ""
br.form["password"] = ""

i=0
for pris in pri:
    print pris
    i += 1
    control = br.form.find_control("mess_registration[caterer_id_"+str(i)+"]")
    for item in control.items:
      if item.name == pris:
          item.selected = True

#submit form
response = br.submit()
print response.read()
