from django .shortcuts import render,redirect
from Banking.models import User
from django.views import View

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.get(email=email)
            if user:
                if(user.password==password):
                    request.session['name']=user.name


                    return redirect('home')
                else:
                    print("enter correct password")

        except:
            print("enter valid email")
        return render(request, 'login.html')