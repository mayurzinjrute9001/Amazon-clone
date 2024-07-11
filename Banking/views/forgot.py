from django.views import View
from django.shortcuts import render
from Banking.models import User

class Forgot_Password(View):
    def get(self,request):
        return render(request, 'forgot.html')
    def post(self,request):
        temp=False
        email=request.POST.get('email')
        password=request.POST.get('password')


        try:
            user=User.objects.get(email=email)
            temp=True
            result="user match successfully"
            color="success"
            if password:
                user.password=password
                user.save()
                temp=False
                result="password changed succesfully "
                color="success"

        except:
            result="enter valid email"
            color="danger"
        return render(request,'forgot.html',{'result':result,'temp':temp,'email':email,'color':color})
