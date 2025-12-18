from scrapy.mail import MailSender

maier=MailSender()
maier.send(
    to=["mayankdri.tagline@gmail.com"],
    subject="Some subject",
    body="Some body",
    cc=["another@example.com"],
)