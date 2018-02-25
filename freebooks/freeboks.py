#!/user/bin/env python

import urllib2
import bs4
import smtplib
import sys



class BookMailer(object):

    def __init__(self,mail_user,mail_password):
        super(BookMailer, self).__init__()
        self.user = mail_user
        self.password = mail_password
        self.book = ""

    def get_html(self, url):

        f = urllib2.urlopen(url)
        html = f.read()
        f.close()                   

        return html

    def send_mail(self,destination):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.user,self.password)

        header = "Subject: Book of the day"
        msg = "\n" \
              "Hello! The book of the day is " + self.book

        msg = header + msg
        server.sendmail(self.user, destination, msg)

    def get_freebook_title(self):

        html = self.get_html("https://www.packtpub.com/packt/offers/free-learning")
        soup = bs4.BeautifulSoup(html, "lxml")
        deal_of_the_day = soup.find("div", "dotd-main-book cf")

        if type(deal_of_the_day) == type(None):
            print "ERROR: Book of The Day Title Deal not found"
            exit(-1)

        book_title = deal_of_the_day.find("div", "dotd-title")

        if type(book_title) == type(None):
            print "ERROR: Book of The Day Title not found"
            exit(-2)

        section_inner = deal_of_the_day.find("ul").text

        if type(section_inner) == type(None):
            print "ERROR: Book of The Day Description not found"
            exit(-3)

        title = book_title.text.replace("\t", "").replace("\n", "")
        description = section_inner.replace("\t", "")

        self.book = title + "\n" + description

        print self.book

def parameterCheck():

    destination_email=""
    gmailCheck = sys.argv[1].split("@")

    if str(gmailCheck[1]) != "gmail.com":
        print "ERROR: Incorrect Parameter Format"
        print" [from: email] must be yourmail@gmail.com"
        exit(-1)

    if len(sys.argv) == 3:
        destination_email = sys.argv[1]
    elif len(sys.argv) == 4:
        destination_email = sys.argv[3]
    else:
        print "ERROR: Incorrect Parameter number"
        print" ScriptParameterUsage: [from: email] [from: password] [to: email| Nothing]]"
        print""
        print" If [to: email] is not filled default addres will be [from: email]"
        exit(-1)
    return destination_email


if __name__=="__main__":


    destination_email = parameterCheck()
    client = BookMailer(sys.argv[1],sys.argv[2])

    client.get_freebook_title()

    if client.book != "":
        client.send_mail(destination_email)
        print "Mail sent to " + destination_email

    else:
        print "ERROR: No Deal of the Day found - Mail Not Sent"
