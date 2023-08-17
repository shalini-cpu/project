from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from myapp.models import Student

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        students = await sync_to_async(list)(Student.objects.all().values())
        await self.send(json.dumps({'students': list(students)}))


    async def disconnect(self, close_code):
        pass

    async def update_items(self,text_data):
        data=text_data['students']
        await self.send(json.dumps({'students':data}))
    # async def receive(self, text_data):
    #     data = json.loads(text_data)
    #     if data.get('action') == 'fetch':
    #         students = await sync_to_async(list)(Student.objects.all().values())
    #         await self.send(json.dumps({'students': list(students)}))

    # async def receive(self, text_data):
        # data = json.loads(text_data)
        # if data.get('action') == 'fetch':
            # Fetch student data from the database
            # students = await async_to_sync(Student.objects.all().values)

            # students = await sync_to_async(list)(Student.objects.all().values())
            # Send the student data to the connected WebSocket client
            # await self.send(json.dumps({'students': list(students)}))
