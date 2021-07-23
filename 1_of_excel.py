from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import xlsxwriter
import requests
import openpyxl

# paste bin link all content private.Click on the link to download.
# download pastebin link all content private asap enjoyyy....

# Download spreadsheet from URL
links_to_read_from = int(input("Enter row number FROM (ENTER ROW NUMBER): ")) 
links_to_read_to = int(input("Enter row number TO (ENTER ROW NUMBER): "))

char = input("Do you want to download file? (y/n) : ")
if(char=='y' or char=='Y'):
    url = 'https://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=1u7ykDr6YaVQi-npQgkIyDdFyc98RdlZD-htOPT6s5Hs&exportFormat=xlsx'
    r = requests.get(url, allow_redirects=True)
    open('mega.xlsx', 'wb').write(r.content)

# Excel File
df = pd.read_excel ('mega.xlsx')

# Content
default_content = """Want more content?

Make sure to download the images/videos in the Mega.nz to your device, as the folder may get taken down due to DMCA at any moment.

Follow us via these links below for Daily Free OnlyFans Content. We drop only Up-to-date OnlyFans content, none of that old recycled content that other groups post.

Reddit : https://www.reddit.com/r/nsfw_chick_of/

How to use : https://reddit.com/r/howto/comments/k4gyr4/how_to_use_linkvertise/

Telegram : https://t.me/nsfw_chick_backup

Discord : https://discord.gg/YX9SpUWzA8

Request : https://discord.gg/Me7mwRpd32

Donate : https://rentry.org/u3wvf

Spreadsheet Containing ALL MEGA LINKS : https://docs.google.com/spreadsheets/d/1-E-1EPLt0XSxAjek-8ufV-rZ6ggKaqyIIHmgCvr_o6k/edit#gid=0

MEGA LINK (Mega won't be re-uploaded if it goes down, so please Download or import to your own drive!)

"""

# Data
headers = ["Username", "Name", "Link"]
lv_content=["# paste bin link all content private.Click on the link to download.",
"# download pastebin link all content private asap enjoyyy...."]

name = df["Name"].tolist()
username = df["Username"].tolist()
link = df["Link"].tolist()
rentry_url = []


# Initialize Driver
chromedriver = "C:/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

driver.get("http://rentry.org/")



# Rentry Link Loop
try:
    for index in range(links_to_read_from - 2,links_to_read_to - 1):
        txt = driver.find_element_by_class_name('CodeMirror-code')
        txt.send_keys(default_content)
        txt.send_keys(name[index] + " - " + username[index] + "\n\n")
        txt.send_keys(link[index])
        go = driver.find_element_by_id('submitButton')
        go.click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'edit-code')))
        url = driver.current_url
        rentry_url.append(url)

        driver.find_element_by_link_text('new').click()

    driver.quit()
except:
    print("Something went wrong")

try:
    # Write to excel
    print(rentry_url)
    number=input("Enter file number: ")

    # workbook = xlsxwriter.Workbook('rentry' + number + '.xlsx')
    # worksheet = workbook.add_worksheet()

    # worksheet.write_row('A1', headers)

    # worksheet.write_column('A2',username)
    # worksheet.write_column('B2',name)
    # worksheet.write_column('C'+ str(links_to_read_from), rentry_url)

    # worksheet.write_column('D1',lv_content)

    # workbook.close()

    # POC - Code to update excel file 

    # xfile = openpyxl.load_workbook('rentry' + number + '.xlsx')

    # sheet = xfile.get_sheet_by_name('Sheet1')
    # sheet['Link'] = 'hello world'
    # xfile.save('text2.xlsx')

except:
    print("Something went wrong")


# Write to txt file - rentry links

rentry_no = input("Enter file number for rentry text file: ")

f = open("rentry_links_"+ rentry_no + ".txt", "w", encoding='utf-8')

for index in range(0,len(rentry_url)):
    f.write(rentry_url[index])
    f.write("\n")

f.close() 


print("Suggested Next FROM Row : " + str(links_to_read_from + len(rentry_url)))

print("Suggested Next TO Row : " + str(links_to_read_from + len(rentry_url) + 6))

# print("Total Number of Rows : " + str(links_to_read_from + len(name)))
