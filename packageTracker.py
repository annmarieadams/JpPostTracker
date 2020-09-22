import ezgmail, requests, bs4, sys, shelve
#Expected arguments: tracking number, (optional) phone number (only numbers), (optional) SMS email gateway (in @ format)
if len(sys.argv)>4:
    print('Invalid argument(s)--- Expected argument: Japanese Tracking Number, phone number, SMS email gateway (optional once program runs once)')
    sys.exit()
PackageReady=False
s=shelve.open('userInfo')
if len(sys.argv)==4:
    s['trackingNum']=sys.argv[1]
    s['phone']=sys.argv[2]
    s['gateway']=sys.argv[3]
res=requests.get('https://trackings.post.japanpost.jp/services/srv/search/direct?locale=en&reqCodeNo1='+sys.argv[1])
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, "lxml")
for items in soup.find_all('td', class_='w_150'):
    if 'Processing at delivery Post Office' in items:
        PackageReady=True
if PackageReady==True:
    ezgmail.init()
    ezgmail.send(s['phone']+s['gateway'],'--PACKAGE ALERT--','Your package ' + s['trackingNum'] + ' is coming! Be ready to sign for it. ')
s.close()