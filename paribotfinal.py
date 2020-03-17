import json 
import requests
import time
import urllib
import sqlite3

TOKEN = "1093473891:AAHXqKsbhCvIb4dzM1gz02-AUlLBwKk8e2I"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
conn = sqlite3.connect('hos.db')



def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    if(text=="hello" or text=="Hello" or text=="Hi"):
        global day
        global doc
        global slot
        text = urllib.parse.quote_plus("Enter the day you want to meet the doctor- today or tomorrow?")
        url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        get_url(url)
    if text=="Thanks" or text=="Thank you" or text=="Thank u":
        text = urllib.parse.quote_plus("Happy to help! :)")
        url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        get_url(url)
        
    if(text=="today" or text=="Today"):
        
        day="today"
        text1 = urllib.parse.quote_plus("Please tell us  the doctor you would like to consult: Dr.Allen-EYE SPEACIALIST Dr.Mishra-Pediatrician Dr.John-Dermatologist")
        url = URL + "sendMessage?text={}&chat_id={}".format(text1, chat_id)
        get_url(url)
    if(text=="tomorrow" or text=="Tomorrow"):
       
        day="tomorrow"
        text1 = urllib.parse.quote_plus("Please tell us  the doctor you would like to consult: Dr.Allen-EYE SPEACIALIST Dr.Mishra-Pediatrician Dr.John-Dermatologist")
        url = URL + "sendMessage?text={}&chat_id={}".format(text1, chat_id)
        get_url(url)
    if(text=="Dr.Allen" or text=="Allen" or text=="Dr. Allen" or text=="Eye specialist"):
      
        doc="Dr.Allen"
        text = urllib.parse.quote_plus("Please enter the slot number you wish to meet the doctor SLOT1-9:00AM TO 12:00 NOON   SLOT2-3:00PM TO 5:00 PM   SLOT3-6:00PM TO 8:00 PM...Enter 1,2 or 3")
        url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        get_url(url)
    if(text=="1"):
         
        slot="1"
        
        if(day=="tomorrow"):
            if(slot=="1"):
                if(doc=="Dr.Allen"):
                    cursor=conn.execute('SELECT SLOT1 FROM T WHERE NAME="Dr.Allen"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 1
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 2
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 3
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="1"):
                if(doc=="Dr.Allen"):
                    cursor=conn.execute('SELECT SLOT1 FROM M WHERE NAME="Dr.Allen"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 1
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 2
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 3
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
    conn.commit()
    if(text=="2"):
         
        slot="2"
        
        if(day=="tomorrow"):
            if(slot=="2"):
                if(doc=="Dr.Allen"):
                    cursor=conn.execute('SELECT SLOT2 FROM T WHERE NAME="Dr.Allen"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 1
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 2
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 3
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="2"):
                if(doc=="Dr.Allen"):
                    cursor=conn.execute('SELECT SLOT2 FROM M WHERE NAME="Dr.Allen"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 1
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 2
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 3
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
    conn.commit()
    if(text=="3"):
         
        slot="3"
        
        if(day=="tomorrow"):
            if(slot=="3"):
                if(doc=="Dr.Allen"):
                    cursor=conn.execute('SELECT SLOT3 FROM T WHERE NAME="Dr.Allen"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 1
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 2
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 3
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="3"):
                if(doc=="Dr.Allen"):
                    cursor=conn.execute('SELECT SLOT3 FROM M WHERE NAME="Dr.Allen"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 1
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 2
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 3
                            WHERE Name = 'Dr.Allen'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
    conn.commit()

    if(text=="Dr.Mishra" or text=="Mishra" or text=="Dr. Mishra" or text=="Pediatrition"):
      
        doc="Dr.Mishra"
        text = urllib.parse.quote_plus("Please enter the slot number you wish to meet the doctor SLOT1-9:00AM TO 12:00 NOON   SLOT2-3:00PM TO 5:00 PM   SLOT3-6:00PM TO 8:00 PM...Enter 1,2 or 3")
        url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        get_url(url)
    if(text=="1"):
         
        slot="1"
        
        if(day=="tomorrow"):
            if(slot=="1"):
                if(doc=="Dr.Mishra"):
                    cursor=conn.execute('SELECT SLOT1 FROM T WHERE NAME="Dr.Mishra"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 1
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 2
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 3
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="1"):
                if(doc=="Dr.Mishra"):
                    cursor=conn.execute('SELECT SLOT1 FROM M WHERE NAME="Dr.Mishra"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 1
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 2
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 3
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
    if(text=="2"):
         
        slot="2"
        
        if(day=="tomorrow"):
            if(slot=="2"):
                if(doc=="Dr.Mishra"):
                    cursor=conn.execute('SELECT SLOT2 FROM T WHERE NAME="Dr.Mishra"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 1
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 2
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 3
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="2"):
                if(doc=="Dr.Mishra"):
                    cursor=conn.execute('SELECT SLOT2 FROM M WHERE NAME="Dr.Mishra"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 1
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 2
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 3
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)

    conn.commit()

    if(text=="3"):
         
        slot="3"
        
        if(day=="tomorrow"):
            if(slot=="3"):
                if(doc=="Dr.Mishra"):
                    cursor=conn.execute('SELECT SLOT3 FROM T WHERE NAME="Dr.Mishra"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 1
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 2
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 3
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="3"):
                if(doc=="Dr.Mishra"):
                    cursor=conn.execute('SELECT SLOT3 FROM M WHERE NAME="Dr.Mishra"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 1
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 2
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 3
                            WHERE Name = 'Dr.Mishra'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)

    if(text=="Dr.John" or text=="John" or text=="Dr. John" or text=="Dermatologist"):
      
        doc="Dr.John"
        text = urllib.parse.quote_plus("Please enter the slot number you wish to meet the doctor SLOT1-9:00AM TO 12:00 NOON   SLOT2-3:00PM TO 5:00 PM   SLOT3-6:00PM TO 8:00 PM...Enter 1,2 or 3")
        url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        get_url(url)
    if(text=="1"):
         
        slot="1"
        
        if(day=="tomorrow"):
            if(slot=="1"):
                if(doc=="Dr.John"):
                    cursor=conn.execute('SELECT SLOT1 FROM T WHERE NAME="Dr.John"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 1
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 2
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT1 = 3
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="1"):
                if(doc=="Dr.John"):
                    cursor=conn.execute('SELECT SLOT1 FROM M WHERE NAME="Dr.John"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 1
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 2
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT1 = 3
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
    conn.commit()
    if(text=="2"):
         
        slot="2"
        
        if(day=="tomorrow"):
            if(slot=="2"):
                if(doc=="Dr.John"):
                    cursor=conn.execute('SELECT SLOT2 FROM T WHERE NAME="Dr.John"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 1
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 2
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT2 = 3
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="2"):
                if(doc=="Dr.John"):
                    cursor=conn.execute('SELECT SLOT2 FROM M WHERE NAME="Dr.John"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 1
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 2
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT2 = 3
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
    conn.commit()

    if(text=="3"):
         
        slot="3"
        
        if(day=="tomorrow"):
            if(slot=="3"):
                if(doc=="Dr.John"):
                    cursor=conn.execute('SELECT SLOT3 FROM T WHERE NAME="Dr.John"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 1
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 2
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE T
                            SET SLOT3 = 3
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
        
        if(day=="today"):
            if(slot=="3"):
                if(doc=="Dr.John"):
                    cursor=conn.execute('SELECT SLOT3 FROM M WHERE NAME="Dr.John"')
                    for row in cursor:
                        if row[0]==0:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 1
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==1:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 2
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        if row[0]==2:
                            conn.execute('''
                            UPDATE M
                            SET SLOT3 = 3
                            WHERE Name = 'Dr.John'
                            ''')
                            text = urllib.parse.quote_plus("YOUR BOOKING HAS BEEN CONFIRMED")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
                        elif row[0]==3:
                            text = urllib.parse.quote_plus("SORRY THE SLOT IS NOT AVAILABLE")
                            url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
                            get_url(url)
    conn.commit()




def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)
            
    

def main():
    last_update_id = None
   
    while True:
        updates = get_updates(last_update_id)                
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
