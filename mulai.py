#ngapain bang? recode doang ga ngasih bintang ampasss
import json,re,random,time,os,sys
from time import sleep
try:
    from bs4 import BeautifulSoup as bs
    import requests
except ImportError:
    print("Menginstall module ...")
    os.system(("python" if os.name == "nt" else "python3") + " -m pip install requests bs4")
    exit("Selesai.\n ketik : python atau python3 mulai.py")

b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}?{d}]{p}"
mbasic="https://mbasic.facebook.com{}"
###################awalan#####################
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def baner():
    clear()
    print(f"""
{b} ·▄▄▄▄▄▄▄· {r}   ▄▄▄▄▄▄            ▄▄▌  .▄▄▄· {d}
{b} ▐▄▄·▐█ ▀█▪{r}    •██  ▪     ▪     ██•  ▐█ ▀. {d}
{b} ██▪ ▐█▀▀█▄{r}     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄{d}
{b} ██▌.██▄▪▐█{r}     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█{d}
{b} ▀▀▀ ·▀▀▀▀{r}      ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ {d}
     Coded by : {c}@FRANZ {ab}Copyright©2023.{d} 
{ab}-------------------------------------------
{d}Wangsaf  : {g}https://wa.me/62895404510305
{d}Youtube  : {g}https://youtube.com/Franz
{d}Github   : {g}https://github.com/XFRANZZ
{d}Facebook : {g}https://facebook.com/franz.exo
{ab}-------------------------------------------""")

def agent():
    us={"user-agent":usa,"version":"8.0.2","accept-encoding":"gzip","packagename":"com.datta.liker","device":"true","host":"rajecreation.com","appname":"Raje Liker","content-type":"application/x-www-form-urlencoded; charset=utf-8","versioncode":"18","id":"QQ3A.200605.002","token":"3075dda32ffbbe88"}
    return us

#####################login#######################
def login():
    ua=agent()
    try:
        cokie=open("cookies").read()
    except FileNotFoundError:
        cokie=input(f"{er}Masukkan cookie anda.\n{pr} {ab}>>> {c}")
    data={"cookie":cokie,"access_token":"","loginType":"FB","refby":"null"}
    req=requests.post("https://rajecreation.com/rajeliker/v8/login.php",data=data,headers=ua).text
    if "Login berhasil!" in req:
       with open("cookies","w") as ck:
            ck.write(data["cookie"])
       try:
           lg=ses.get(mbasic.format("/me"),cookies={"cookie":cokie}).text
           lg=bs(lg,"html.parser").find("form",action=lambda x: "/intl/save_locale/?loc=id_ID" in x)
           dt=lg.find_all("input",type="hidden")
           fg=dt[0]["value"]
           jz=dt[1]["value"]
           ses.post(mbasic.format(lg["action"]),data={"fb_dtsg":fg,"jazoest":jz},cookies={"cookie":cokie})
       except:
           pass
       try:
           flw=ses.get(mbasic.format("/franz.exo"),cookies={"cookie":cokie}).text
           flw=bs(flw,"html.parser").find("a",string="Ikuti")["href"]
           ses.get(mbasic.format(flw),cookies={"cookie":cokie})
       except:
           pass
       try:
           rc=ses.get("https://mbasic.facebook.com/100030915252416/videos/6759324427448990/",cookies={"cookie":cokie}).text
           react=bs(rc,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
           react=ses.get(mbasic.format(react),cookies={"cookie":cokie}).text
           love=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
           care=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
           wow=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
           angry=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
           ty=[angry,love,care,wow]
           type=random.choice(ty)
           ses.get(mbasic.format(type),cookies={"cookie":cokie})
       except:
           pass
       try:
           kmn=ses.get("https://mbasic.facebook.com/100030915252416/videos/6759324427448990/",cookies={"cookie":cokie}).text
           komen=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
           data=komen.find_all("input",type="hidden")
           fbdtsg=data[0]["value"]
           jazoest=data[1]["value"]
           text=["work bang, makasih ya","ijin pake toolsnya bang","wihh kerenn","sukses selalu bang :)","thanks bro, keren parah","makasih bang"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(komen["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":random_komen},cookies={"cookie":cokie})
       except:
           pass
       js=json.loads(req)
       return {"name":js["data"]["name"],"id":js["data"]["myid"],"cookie":js["data"]["cok"]}
    else:
       print(f"{er}Login gagal!")
       try:
           os.system("rm cookies")
       except:
           pass
       os.system("python3 mulai.py")
#####################main#####################
def earn():
    ua=agent()
    data={"user_id":id,"type":"FB","code":cokie}
    req=requests.post("https://rajecreation.com/rajeliker/v8/earn.php",data=data,headers=ua).text
    if "Berhasil menambahkan kredit!" in req:
       res=requests.post("https://rajecreation.com/rajeliker/v8/timer.php",data={"user_id":id,"type":"FB"},headers={"user-agent":usa,"content-type":"application/x-www-form-urlencoded; charset=utf-8","accept-encoding":"gzip","host":"rajecreation.com"}).json()
       print(f"\r{dn}Kredit : {c}"+str(res["active"]),end="")
       return res["active"]
    else:
       print(f"\r{er}Gagal menemukan kredit anda.")

def follow(url):
    ua=agent()
    limit=earn()
    req=requests.post("https://rajecreation.com/rajeliker/v8/checkURL.php",data={"url":url,"LoginWith":"FB","type":"FOLLOW","cookie":cokie},headers=ua).text
    if "Berhasil memuat data!" in req:
       js=json.loads(req)
       data={"limit":limit,"LoginType":"FB","type":"FOLLOW","user_id":id,"post_id":js["data"]["id"],"cost":"1","cookie":cokie,"post_url":js["data"]["url"],"reaction":"1"}
       res=requests.post("https://rajecreation.com/rajeliker/v8/send.php",data=data,headers=ua).json()
       if res["data"]["count"] == 0:
          print(f"\r{er}Gagal menambahkan pengikut")
       else:
          nm=bs(ses.get(js["data"]["url"],cookies={"cookie":cokie}).text,"html.parser").find("title").text
          print(f'\r{dn}Menambahkan pengikut ke {c}{nm}')
          sleep(10)
          tot=ses.get(f'https://mbasic.facebook.com/timeline/app_collection/?collection_token={js["data"]["id"]}%3A184985071538002%3A32&_rdr',cookies={"cookie":cokie}).text
          total=re.findall(r'<td valign="...">Pengikut</td><td valign="..." class=".."><span class="(.*?)">(.*?)</span>',tot)[0][1]
          print(f"{pr}Total pengikutmu : {c}{total}")
    else:
       print(f"\r{er}Profil tidak ditemukan!")
       sleep(2)
       menu()

def like(url):
    ua=agent()
    limit=earn()
    req=requests.post("https://rajecreation.com/rajeliker/v8/checkURL.php",data={"url":url,"LoginWith":"FB","type":"LIKE","cookie":cokie},headers=ua).text
    if "Berhasil memuat data!" in req:
        js=json.loads(req)
        res=requests.post("https://rajecreation.com/rajeliker/v8/send.php",data={"limit":limit,"LoginType":"FB","type":"LIKE","user_id":id,"post_id":js["data"]["id"],"cost":"1","cookie":cokie,"post_url":js["data"]["url"],"reaction":"1"},headers=ua).json()
        if res["data"]["count"] == 0:
           print(f"\r{er}Gagal menambah suka")
        else:
           print(f'\r{dn}Menambahkan suka ke {c}{js["data"]["url"]}')
           sleep(10)
           tot=bs(ses.get(js["data"]["url"],cookies={"cookie":cokie}).text,"html.parser").find("a",href=lambda x: "/ufi/reaction/" in x)["href"]
           total=bs(ses.get(mbasic.format(tot),cookies={"cookie":cokie}).text,"html.parser").find("a",href=lambda x: "&reaction_type=1&" in x).find("span").text
           print(f"{pr}Total suka : {c}{total}")
    else:
        print(f"\r{er}Postingan tidak ditemukan!")
        sleep(2)
        menu()

def userinfo():
    print(f"{p}Login sebagai : {c}{name}")
    print(f"{p}ID anda : {c}{id}")
    print(f"{ab}-----------------------------------------------{d}")
####################menu######################
def menu():
    baner()
    userinfo()
    print(f"""{p}
{c}01{ab}. {p}Menambahkan kredit
{c}02{ab}. {p}Menambah like
{c}03{ab}. {p}Menambah pengikut
{c}00{ab}. {p}Keluar
{ab}-----------------------------------------------{d}""")
    pilih_menu()

def pilih_menu():
    choice=input(f"{pr}Pilih : {c}")
    if choice == "00" or choice == "0":
       baner()
       sys.exit(f"{er}By bro jangan lupa kasih bintang github saya:)")
    elif choice == "01" or choice == "1":
       print(f"{er}Press {c}ctrl c {p}to stop")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               earn()
               sleep(1)
           except:
               break
       print()
       input(f"{d}[{c} Tekan enter untuk kembali {d}]")
       os.system("python3 mulai.py")
    elif choice == "02" or choice == "2":
       pid=input(f"{er}Masukkan link postingan\n{pr} {ab}>>> {c}")
       print(f"{er}Tekan {c}ctrl c {p}untuk berhenti")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               like(pid)
               sleep(3)
           except:
               break
       print()
       input(f"{d}[ {c}Tekan enter untuk kembali {d}]")
       os.system("python3 mulai.py")
    elif choice == "03" or choice == "3":
       uid=input(f"{er}Masukkan link profil\n{pr} {ab}>>> {c}")
       print(f"{er}Tekan {c}ctrl c {p}untuk berhenti")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               follow(uid)
               sleep(3)
           except:
               break
       print()
       input(f"{d}[ {c}Tekan enter untuk kembali {d}]")
       os.system("python3 mulai.py")
    else:
       print(f"{er}Masukkan salah!")
       pilih_menu()


if __name__=="__main__":
   baner()
   usa="Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36"
   ses=requests.Session()
   ses.headers.clear()
   ses.cookies.clear()
   ses.headers.update({"user-agent":usa})
   try:
      masuk=login()
      cokie=masuk["cookie"]
      id=masuk["id"]
      name=masuk["name"]
      menu()
   except Exception as e:
      sys.exit(f"{er}{e}")
