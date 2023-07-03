from django.shortcuts import redirect


def custom_password_reset_redirect(request, uid, token):
    redirect_url = f'http://localhost:3000/password-confirm?uuid={uid}&token={token}'
    return redirect(redirect_url)
