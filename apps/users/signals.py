from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # subject:
        "تكوين - إسترجاع كلمة المرور",
        # message:
        email_plaintext_message,
        # from:
        "noreply@takwine.ma",
        # to:
        [reset_password_token.user.email]
    )
