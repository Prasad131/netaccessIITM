import requests, bs4

name, passw = 'userName', 'userPassword'        # Provide your LDAP details 

s = requests.Session()

res = s.get('https://netaccess.iitm.ac.in/account/login')

soup = bs4.BeautifulSoup(res.text, "lxml")

formdata = {
        'submit' : True, 
        'userLogin' : name,
        'userPassword' : passw
    }

r = s.post('https://netaccess.iitm.ac.in/account/login', data=formdata)

res = s.get('https://netaccess.iitm.ac.in/account/approve')

formdata = {
        'approveBtn' : True,
        'duration' : 2            # duration = 2 is for 1 day. Change the duration to 1 if you want 60 minutes access.
    }
r = s.post('https://netaccess.iitm.ac.in/account/approve', data=formdata)

