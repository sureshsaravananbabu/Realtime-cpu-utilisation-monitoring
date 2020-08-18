from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import psutil
sendmail=0
class Home(View):
    template_name = 'Home.html'
    def get(self, request, *args, **kwargs):
        print("hello")
        return render(request, self.template_name)
        
def emailfield(request):
    global sendmail
    sendmail = request.POST['email']
    return HttpResponse('THANK YOU')


def return_email():
    return sendmail
