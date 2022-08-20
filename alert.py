# Gaby
# Alert on results

import os
import smtplib
import datetime

clear = lambda: os.system('cls')

def alert(result):
    # Request & check results from resultmanager    
    if len(result) != 0 :
        print("You have new results!")
    else:
        print("There are no new results. :(")

    # Create alert format
        # counter: number of times keyword appears per site? Is this happening in search or results already?
        # clickable direct link to positive hit
        x = datetime.datetime.now()
        y = len(result) != 0
        text_1 = ("For search run on", x, "you have", y, "results.")
 
  
    """# Configurable search alerts (conditional????)
        # Priority alerts
        # Persistent Monitoring alert 
        # Timing of alerts (short turn or long term search)    

    # Notification Setup
        #input account(s) to send alert
            # multiple locations
                # Alert distribution via email
                #   get_email
                # Alert distribution via console
                # Alert distribution via messaging
                # Alert distribution via web/social media
    gmail_user = #########
    gmail_password = ############
    sent_from = gmail_user
    to = {get_email}
    subject = {get_fname}, "Here Are Your Search Results"
    email_text = "./Results_1.json"

    # Deployment: email send request
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print("Email sent!")
    except Exception as e:
        print(e)
        print("Something went wrong...")"""

def main():
    """
    result = [{
        "datetime":"now",
        "result":"information"
    }]"""
    #result = []
    alert(result)

if __name__ == "__main__":
    clear()
    main()


