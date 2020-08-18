import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings 
from .views import return_email
from django.core.mail import send_mail 
import psutil
import json

class SendData(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        flag=list()
        while True:
            await asyncio.sleep(1)
            vcpu=psutil.cpu_percent()
            rp=psutil.virtual_memory().percent
            a=return_email()
            if(rp>50):
                flag.append(1)
            else:
                flag.clear()
            if(rp>50  and  len(flag)==10):
                print("send")
                subject = 'NOTIFICATION regarding RAM USAGE'
                message = 'your RAM utilisation is more than 50%'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [a] 
                send_mail( subject, message, email_from ,recipient_list )
                flag.clear()
            await self.send(text_data=json.dumps({'cpu':vcpu,'ram':rp}))


    async def receive(self, event):
        print("hellooooo")
        print("receive", event)

    async def disconnect(self, event):
        print("disconnected", event)