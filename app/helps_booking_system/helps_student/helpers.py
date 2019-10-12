from django.core.mail import send_mail

def send_email(content):
    # Send an email
    print('sending')
    try:
        send_mail(
            content['subject'],
            content['plain_message'],
            'softwarestudio2ab@gmail.com',
            content['contacts'],
            fail_silently=False,
            html_message=content['html_message']
        )
        print('Sent')
        return True
    except:
        return False
