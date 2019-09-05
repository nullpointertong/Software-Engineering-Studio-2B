from django.core.mail import send_mail


def send_email(subject, message, contacts):
    # Send an email
    print('sending')
    try:
        send_mail(
            subject,
            message,
            'softwarestudio2ab@gmail.com',
            contacts,
            fail_silently=False,
        )
        return True
    except:
        return False
