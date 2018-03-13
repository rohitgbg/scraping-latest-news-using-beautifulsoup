from bs4 import BeautifulSoup
import requests
import csv
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


class LatestNews:
	def __init__(self):
		self.title = ""
		self.url = ""

	
	url = 'https://timesofindia.indiatimes.com/news'
	req = requests.get(url)
	html_doc = req.text
	soup = BeautifulSoup(html_doc, 'lxml')

	news_list = []

	def get_latest_news(self):
		soup = LatestNews.soup
		find_news = soup.find_all('a', class_='w_img')
		for news in find_news:
			store_news = LatestNews()
			store_news.title = news['title']
			store_news.url = news['href']
			LatestNews.news_list.append(store_news)

	def print_latest_news(self):
		count = 0
		for news in LatestNews.news_list:
			count = count + 1
			print "%s|%s|%s\n" % (count, news.title, news.url)

	
	def store_news_in_file(self):
		print "Started to write news to file"
		count = 0
		file_news = csv.writer(open("news.csv", "w"))
		file_news.writerow(["Count","Title", 'URL'])
		for news in LatestNews.news_list:
			count = count + 1
			file_news.writerow([count, news.title.encode('utf-8'), news.url.encode('utf-8')])	
		print "Successfully written %s latest news to file" % count


	def send_mail(self):

		print "Enter following details to send mail"
		toaddr = raw_input('Enter receiver mail: ')
		subject = raw_input('Enter subject: ')
		description = raw_input('Enter Description of mail: ')


		fromaddr = "Enter from address email-id"
		
		msg = MIMEMultipart()
		 
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = subject
		 
		body = description
		 
		msg.attach(MIMEText(body, 'plain'))
		 
		filename = "news.csv"
		attachment = open("news.csv", "rb")
		 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		 
		msg.attach(part)
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "Enter the from address email password")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print "Mail Sent Successfully"



	def options(self):
		obj = LatestNews()
		obj.get_latest_news()
		print "1. Just Print News"
		print "2. Send to mail"
		print "3. Exit"	
		choice = int(raw_input('Enter your choice: '))
		if choice == 1:
			obj.print_latest_news()
		elif choice == 2:

			obj.store_news_in_file()
			obj.send_mail()
		else:
			exit()


object = LatestNews()
object.options()

		



