import smtplib

server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login("vishnuselva21@gmail.com","9945066927")
server.sendmail(
	"vishnuselva21@gmail.com",
	"vishnudeepak130@gmail.com",
	"this message is from python")
server.quit()