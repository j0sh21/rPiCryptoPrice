import smtplib

def mail(info_m, subject_m, mailfrom_m, mailto_m, smtp_m, mail_usr_m, mail_pwd_m):
    # E-Mail zusammenbau
    msg_m = 'From:' + mailfrom_m + '\n' + 'To:' + mailto_m + '\n' + 'Subject:' + subject_m + '\n' + info_m
    # E-Mail versenden, dann zuvor aufgebaute Verbindung schließen
    server = smtplib.SMTP(smtp_m)
    server.starttls()
    server.login(mail_usr_m, mail_pwd_m)
    server.sendmail(mailfrom_m, mailto_m, msg_m)
    server.quit()