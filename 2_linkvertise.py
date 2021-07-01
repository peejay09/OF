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
headline_reddit = '''👙 DM FOR {0} {1} Onlyfans Mega Link Leak **DO NOT ASK IN COMMENTS** 👅'''
headline_telegram = '''👙 {0} {1} Onlyfans Mega Link Leak 👅'''

telegram='''
        ✅ Click for Onlyfans ✅ - {0}
        |
        ❓ How To Use Links❓ - https://reddit.com/r/howto/comments/k4gyr4/how_to_use_linkvertise/ 
        | 
        📲 Follow on Telegram 📲 - https://t.me/nsfw_chick_backup
        |
        📝 All Links Till Now 📝 - https://docs.google.com/spreadsheets/d/1-E-1EPLt0XSxAjek-8ufV-rZ6ggKaqyIIHmgCvr_o6k/edit#gid=0
        |
        💾 Join Backup Channel 💾 - https://t.me/nsfw_chick
        |
        👾 Join Discord Server 👾 - https://discord.gg/YX9SpUWzA8
        |
        ✍️ Post Your Requests ✍️ - https://discord.gg/Me7mwRpd32
        '''
reddit = '''
✅ Click for Onlyfans ✅ - {0}

❓ How To Use Links❓ - https://reddit.com/r/howto/comments/k4gyr4/how_to_use_linkvertise/

📲 Follow on Telegram 📲 - https://t.me/nsfw_chick_backup

👾 Join Discord Server 👾 - https://discord.gg/YX9SpUWzA8
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
    f.write(":new: Added content from your requests - Please check #📦-latest-content channel.\n\n")
    
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
