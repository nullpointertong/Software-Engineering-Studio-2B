from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
import os

# def send_email(content):
#     # Send an email
#     print('sending')
#     try:
#         send_mail(
#             content['subject'],
#             content['plain_message'],
#             'softwarestudio2ab@gmail.com',
#             content['contacts'],
#             fail_silently=False,
#             html_message=content['html_message']
#         )
#         print('Sent')
#         return True
#     except SystemError:
#         print('Authentication error')
#         return False
#     except:
#         return False

# send email with images
def send_email(content):
    print('sending')
    msg = EmailMultiAlternatives(content['subject'], 
                                content['plain_message'], 
                                'softwarestudio2ab@gmail.com', 
                                content['contacts'])
    msg.attach_alternative(content['html_message'], "text/html")
    msg.mixed_subtype = 'related'
    root_dir = os.path.dirname(__file__) 
    img_path = os.path.join(root_dir, 'static', 'images', 'uts_logo_black.png')
    pic = open(img_path, 'rb')
    msg_img = MIMEImage(pic.read())
    pic.close()
    msg_img.add_header('Content-ID', '<{}>'.format('uts_logo_black.png'))
    msg.attach(msg_img)
    msg.send()
    print('Sent')
