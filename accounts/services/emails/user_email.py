from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from accounts.models import Account

class UserEmailService:
    @classmethod
    def send_activate_email(cls,current_site, user_id, to_email):
        user = Account.objects.get(id=user_id)
        template = 'accounts/emails/account_verification_email.html'
        mail_subject = "Please verify  your account"
        message = render_to_string(template, {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()

    def send_email_reset_password(cls,current_site, user, to_email):
        template = 'accounts/emails/reset_password_email.html'
        mail_subject = "Reset your password"
        message = render_to_string(template, {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()