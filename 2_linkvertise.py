import pandas as pd
import emoji 


rentry = input("Enter rentry file number to read from : ")

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
        ❓How To Use Links❓ - https://reddit.com/r/howto/comments/k4gyr4/how_to_use_linkvertise/ 
        | 
        📲 Follow on Telegram 📲 - https://t.me/nsfw_chick_backup
        |
        💾 Join Backup Channel 💾 - https://t.me/nsfw_chick
        |
        👾 Join Discord Server 👾 - https://discord.gg/eSYrfWnxcX
        '''
reddit = '''
✅ Click for Onlyfans ✅ - {0}

❓How To Use Links❓ - https://reddit.com/r/howto/comments/k4gyr4/how_to_use_linkvertise/

📲 Follow on Telegram 📲 - https://t.me/nsfw_chick_backup

👾 Join Discord Server 👾 - https://discord.gg/eSYrfWnxcX
'''

username=[]
for uname in temp_username:
    uname = uname.replace("_", r"\_")
    username.append(uname)


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


f = open("file_telegram.txt", "w", encoding='utf-8')
write_file_telegram(f)
f.close()


f = open("file_reddit.txt", "w", encoding='utf-8')
write_file_reddit(f)
f.close()
