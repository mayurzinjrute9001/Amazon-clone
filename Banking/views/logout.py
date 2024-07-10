from django .shortcuts import render,redirect
from django.views import View

class Logout(View):
    def get(self,request):
        request.session.clear()
        return render(request,'login.html')