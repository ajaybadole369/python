import pandas as pd
import datetime
import smtplib
GMAIL_ID='ajay.badole.sdbc@gmail.com'
GMAIL_PASS=''

def sendEmail(to, sub, msg,name):
    print(f"Email to {to} sent with subject: {sub} and message str({msg})  Name: {name}")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PASS)
    s.sendmail(GMAIL_ID,to,f"subject {sub}\n\n{name}\n\n{msg} ")
    s.quit()


if __name__ == '__main__':
    df = pd.read_excel("birthday.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    # print(today)
    yearnow = datetime.datetime.now().strftime("%Y")
    # print(yearnow)
    writeInd = []
    # print(writeInd)
    for index, item in df.iterrows():
        # print(index,item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        # print(bday)
        # msg = "happy birthday bhai"
        if (today == bday) and yearnow not in str(item['Year']):
            sendEmail(item['Emailid'], 'happy birthday', item['Dialouge'],item['Name'])
            writeInd.append(index)

    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        # print(yr)
        df.loc[i, 'Year'] = str(yr) + ',' + str(yearnow)
        # print(df.loc[i,'Year'])
    # print(df)
    df.to_excel('birthday.xlsx',index=False)