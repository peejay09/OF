import pandas as pd
import emoji 
import requests


rentry = input("Enter rentry file number to read from : ")

char = input("Do you want to download rentry file from google? (y/n) : ")
if(char=='y' or char=='Y'):
    url = 'https://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=1dWeTZ4udRBdNsAzPAg7LJF-CQ4KIQnWoLEKnjmwRFUk&exportFormat=xlsx'
    r = requests.get(url, allow_redirects=True)
    open('rentry'+ str(rentry) + '.xlsx', 'wb').write(r.content)
# Excel File
df = pd.read_excel ('rentry'+rentry+'.xlsx')

# Data
name = df["Name"].tolist()
temp_username = df["Username"].tolist()
link = df["Link"].tolist()

#Text
headline_reddit = '''π DM FOR {0} {1} Onlyfans Mega Link Leak **LINK IN THE COMMENTS ALSO** π'''
headline_telegram = '''π {0} {1} Onlyfans Mega Link Leak π'''

telegram='''
        β Click for Onlyfans β - {0}
        |
        β How To Use Linksβ - https://reddit.com/r/howto/comments/k4gyr4/how_to_use_linkvertise/ 
        | 
        π² Follow on Telegram π² - https://t.me/nsfw_chick
        |
        π All Links Till Now π - https://docs.google.com/spreadsheets/d/1-E-1EPLt0XSxAjek-8ufV-rZ6ggKaqyIIHmgCvr_o6k/edit#gid=0
        |
        πΎ Join Backup Channel πΎ - https://t.me/nsfw_chick_2
        |
        πΎ Join Discord Server πΎ - https://discord.gg/wspe8KTsje
        |
        βοΈ Post Your Requests βοΈ - https://discord.gg/Me7mwRpd32
        |
        π©Έ Please Donate π©Έ - https://rentry.org/u3wvf
        '''
reddit = '''
β Click for Onlyfans β - https://rentry.org/vbrh3

β Click for Onlyfans β - {0}

β How To Use Linksβ - https://reddit.com/r/howto/comments/k4gyr4/how_to_use_linkvertise/

π² Follow on Telegram π² - https://t.me/nsfw_chick

πΎ Join Discord Server πΎ - https://discord.gg/wspe8KTsje

π Join our Reddit π - https://www.reddit.com/r/nsfw_chick_of/

π©Έ Please Donate π©Έ - https://rentry.org/u3wvf

πΎ For ALL Direct MEGA Links JOIN PREMIUM @ $10 (Paypal/Crypto). Direct Message on : πΎ

β‘οΈ Telegram : @error404

β‘οΈ Discord : @nswf_chick#2456

β‘οΈ Reddit : @Appropriate-Aerie-59

'''

try:
    username=[]
    for uname in temp_username:
        uname = uname.replace("_", r"\_")
        username.append(uname)
except:
    print("Some issue in rentry1 excel. Remove #findlinks etc. line if present")

def write_file_telegram(f):
    
    for index in range(0,len(name)):
        f.write("\n\n=============================="+ name[index] + "==============================\n\n")
        f.write("                Telegram_UNAME                \n\n")
        
        f.write(headline_telegram.format(name[index], username[index]))
        
        f.write("\n\n                Telegram                \n\n")
        
        f.write(telegram.format(link[index]))

def write_file_reddit(f):
    for index in range(0,len(name)):
        f.write("\n\n=============================="+ name[index] + "==============================\n\n")
        f.write("\n\n                Reddit_UNAME                \n\n")
        
        f.write(headline_reddit.format(name[index], temp_username[index]))

    for index in range(0,len(name)):
        f.write("\n\n                Reddit                \n\n")
        f.write(reddit.format(link[index]))

def write_file_discord(f):
    for index in range(0,len(name)):
        f.write(":white_check_mark: " + name[index] + " - " + link[index] + "\n\n")
    
    f.write("\n\n============================================================\n\n")
    
    f.write(":new: New links added :\n\n")
    for index in range(0,len(name)):
        f.write(":white_check_mark: " + name[index] + "\n\n")
    f.write(":new: Added content from your requests - Please check #π¦-latest-content channel.\n\n")
    
f = open("file_telegram.txt", "w", encoding='utf-8')
write_file_telegram(f)
f.close()


f = open("file_reddit.txt", "w", encoding='utf-8')
write_file_reddit(f)
f.close()

f = open("file_discord.txt", "w", encoding='utf-8')
f.write(":new: New links added :\n\n")
write_file_discord(f)
f.close()
