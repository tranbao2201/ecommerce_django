from base64 import urlsafe_b64decode
from email import message
from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render

from accounts.models import Account
from cart.models import Cart
from cart.service.cart import CartService
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
import requests

# activate accounts
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                               email=email, password=password)
            user.phone_number = phone_number
            user.save()

            # user activation
            current_site = get_current_site(request)
            mail_subject = "Please verify  your account"
            message = render_to_string('accounts/emails/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(
                request, 'Please verify your email address. We have sent you an email to your email address')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            CartService.merge_cart(request, user)
            auth.login(request, user)
            messages.success(request, 'Login Success')
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params.keys():
                    return redirect(params['next'])
            except Exception:
                return redirect('dashboard')
        else:
            messages.error(request, 'Login Failed')
            return redirect('login')
    return render(request, 'accounts/login.html', {})


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Success')
    return redirect('home')


def activate(request, uidb64=None, token=None):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated')
        return redirect('home')
    else:
        messages.error(request, 'Invalid actionvation link')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        user = Account.objects.filter(email__exact=email)
        if user.exists():
            user = user.first()
            # user activation
            current_site = get_current_site(request)
            mail_subject = "Reset your password"
            message = render_to_string('accounts/emails/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Password reset email sent successfully')
            return redirect('home')
        else:
            messages.error(request, 'Email does not exist')
            return redirect('forgot_password')
    return render(request, 'accounts/forgot_password.html', {})


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, 'This link has been expired')
        return redirect('login')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        password_confirmation = request.POST.get('password_confirmation', '')

        if password == password_confirmation:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password confirmation does not match')
            return redirect('forgot_password')
    return render(request, 'accounts/reset_password.html', {})
