Scraping latest news using BeautifulSoup and sending it to mail

Following dependencies/packages should be installed

Python Version: 2


1) BeautifulSoup4: 

  sudo pip install bs4

2) Requests: 

  sudo apt install requests


3) CSV: 

  sudo apt install csv


4) smtplib: 

  sudo apt install apcupsd


5) lxml: 

  sudo apt install lxml


Mail Configuration

Change from address email:  
fromaddr = "Enter from address email-id"

Change form address email password: 

server.login(fromaddr, "Enter the from address email password")

