from tokenize import generate_tokens
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.views import View
# Create your views here.
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str,DjangoUnicodeDecodeError
from .utils import TokenGenerator , generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login
# Create your views here.
def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        if password != confirm_password:
            messages.warning(request, "Password is not matching ")
            return render(request, 'signup.html')

        try:
            if User.objects.get(username=email):
                messages.warning(request, "email already exists") 
                return render(request, 'signup.html')
                # return HttpResponse("email already exists")
                # return render(request, 'auth/signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email, email, password)
        user.is_active = False
        user.save()
        email_subject = "Activate your account"
        message=render_to_string('authentication/activate.html', {
            'user': user,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
        })
        email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],)
        email_message.send()
        messages.success(request, "User created, Please verify your email !")
        return redirect('/auth/signup')
    
    return render(request, 'signup.html')

class ActivateAccountViews(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account activated successfully, now you can login!! ")
            return redirect('/auth/signup')
        return render(request,'authentication/activatefail.html')



def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username, password=userpassword)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login successful")
            return render(request,'index.html')
        else:
            messages.warning(request, "Invalid password")
            return render(request,'authentication/login.html')
    return render(request,'authentication/login.html')

def handlelogout(request):
    return redirect('/auth/login')
#2hrs