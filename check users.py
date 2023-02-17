import requests,random,pyfiglet,os,threading
logo = pyfiglet.figlet_format("Insta\n Users",font = "slant"  ) 
print(logo)
print(' < 1️⃣ > Check Users Like This u.h.k \n < 2️⃣ > Check Users Like This o_t_d \n < 3️⃣ > Check Users Like This k_f.a or p.7_w')
choose = input(' < 0️⃣ > Choose : ')
def k():
    os.system('clear')
    print(logo)
    h = 0
    token = input(' Enter Your Bot Token : ')
    id = input(' Enter Telegram ID : ')
    os.system('clear')
    print(logo)
    while True:
        iis = 'qwertyuiopasdfghjklzxcvbnm'
        u1 = 'qwertyuiopasdfghjklzxcvbnm'
        u2 = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        us = ''.join(random.choice(iis)for i in range(1))
        us2 = ''.join(random.choice(u2)for i in range(1))
        u3 = ''.join(random.choice(u2)for i in range(1))
        user = us+'_'+us2+'_'+u3
        r = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',headers = {
'accept':'*/*',
'accept-encoding':'gzip, deflate',
'accept-language':'en-US,en;q=0.9',
'content-length':'97',
'content-type':'application/x-www-form-urlencoded',
'cookie':'csrftoken=8Z3dGB1AnriMwTvXTDceYJyP9lV04vGD; ds_user_id=6998232734; mid=Y7r7HQALAAFWD-afPi8pcdWQJPf8; ig_did=FDCB076A-295C-421C-890F-8F551406FC73',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'sec-ch-prefers-color-scheme':'light',
'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'viewport-width':'818',
'x-asbd-id':'198387',
'x-csrftoken':'8Z3dGB1AnriMwTvXTDceYJyP9lV04vGD',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'x-instagram-ajax':'1006796888',
'x-requested-with':'XMLHttpRequest'},data = f"email=kskwkssjsajauaujsjkw%40gmail.com&username={user}&first_name=skwnajajkn&opt_into_one_tap=false").text
        
        if '"username"' in r:
            h+=1
            print(r)
            print(f'[ {h} ]'+'User Is Unavailable ==> '+user)
        elif '"username"' not in r:
            h+=1
            print(f'[ {h} ]'+' User Is Available ==> '+user)
            ik = "حب جبتلك يوزر جديد😂❤️"
            hit = requests.post(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={id}&text={ik}  \n User : @{user}\n by@h_8_k")
            with open('good users.txt',"a") as usk:
                usk.write(f'{user}\n')
def n():
    os.system('clear')
    print(logo)
    h = 0
    token = input(' Enter Your Bot Token : ')
    id = input(' Enter Telegram ID : ')
    os.system('clear')
    print(logo)
    while True:
        iis = 'qwertyuiopasdfghjklzxcvbnm'
        u1 = 'qwertyuiopasdfghjklzxcvbnm'
        u2 = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        us = ''.join(random.choice(iis)for i in range(1))
        us2 = ''.join(random.choice(u2)for i in range(1))
        u3 = ''.join(random.choice(u2)for i in range(1))
        user = us+'.'+us2+'.'+u3
        r = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',headers = {
'accept':'*/*',
'accept-encoding':'gzip, deflate',
'accept-language':'en-US,en;q=0.9',
'content-length':'97',
'content-type':'application/x-www-form-urlencoded',
'cookie':'csrftoken=8Z3dGB1AnriMwTvXTDceYJyP9lV04vGD; ds_user_id=6998232734; mid=Y7r7HQALAAFWD-afPi8pcdWQJPf8; ig_did=FDCB076A-295C-421C-890F-8F551406FC73',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'sec-ch-prefers-color-scheme':'light',
'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'viewport-width':'818',
'x-asbd-id':'198387',
'x-csrftoken':'8Z3dGB1AnriMwTvXTDceYJyP9lV04vGD',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'x-instagram-ajax':'1006796888',
'x-requested-with':'XMLHttpRequest'},data = f"email=kskwkssjsajauaujsjkw%40gmail.com&username={user}&first_name=skwnajajkn&opt_into_one_tap=false").text
        if '"username"' in r:
            h+=1
            print(f'[ {h} ]'+'User Is Unavailable ==> '+user)
        elif '"username"' not in r:
            h+=1
            print(f'[ {h} ]'+' User Is Available ==> '+user)
            ik = "حب جبتلك يوزر جديد😂❤️"
            hit = requests.post(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={id}&text={ik}  \n User : @{user}\n by @h_8_k")
            with open('good users.txt',"a") as usk:
                usk.write(f'{user}\n')
def nn():
    os.system('clear')
    print(logo)
    h = 0
    token = input(' Enter Your Bot Token : ')
    id = input(' Enter Telegram ID : ')
    os.system('clear')
    print(logo)
    while True:
        iis = 'qwertyuiopasdfghjklzxcvbnm'
        u1 = 'qwertyuiopasdfghjklzxcvbnm'
        u2 = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        us = ''.join(random.choice(iis)for i in range(1))
        us2 = ''.join(random.choice(u2)for i in range(1))
        u3 = ''.join(random.choice(u2)for i in range(1))
        dot = ''.join(random.choice('._')for i in range(1))
        dot2 = ''.join(random.choice('._')for i in range(1))
        user = us+dot2+us2+dot+u3
        r = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',headers = {
'accept':'*/*',
'accept-encoding':'gzip, deflate',
'accept-language':'en-US,en;q=0.9',
'content-length':'97',
'content-type':'application/x-www-form-urlencoded',
'cookie':'csrftoken=8Z3dGB1AnriMwTvXTDceYJyP9lV04vGD; ds_user_id=6998232734; mid=Y7r7HQALAAFWD-afPi8pcdWQJPf8; ig_did=FDCB076A-295C-421C-890F-8F551406FC73',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'sec-ch-prefers-color-scheme':'light',
'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'viewport-width':'818',
'x-asbd-id':'198387',
'x-csrftoken':'8Z3dGB1AnriMwTvXTDceYJyP9lV04vGD',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'x-instagram-ajax':'1006796888',
'x-requested-with':'XMLHttpRequest'},data = f"email=kskwkssjsajauaujsjkw%40gmail.com&username={user}&first_name=skwnajajkn&opt_into_one_tap=false").text
        if '"username"' in r:
            h+=1
            print(f'[ {h} ]'+'User Is Unavailable ==> '+user)
        elif '"username"' not in r:
            h+=1
            print(f'[ {h} ]'+' User Is Available ==> '+user)
            ik = "حب جبتلك يوزر جديد😂❤️"
            hit = requests.post(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={id}&text={ik}  \n User : @{user}\n by @h_8_k")
            with open('good users.txt',"a") as usk:
                usk.write(f'{user}\n')           
if choose =="1":
    thread1 = threading.Thread(target= n)
    thread1.start() 
if choose =="2":
    thread2 = threading.Thread(target= k)
    thread2.start()
if choose =="3":
    nn()