from django .shortcuts import render
from Banking.models import User
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            password = request.POST.get('password')
            print(name, email, number, password)
            user = User(name=name, email=email, phone=number, password=password)
            user.save()
        except:
            pass
        return render(request,'login.html')