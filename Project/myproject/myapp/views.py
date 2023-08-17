from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Student
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# def get_students(request):
#     students = Student.objects.all().values()
#     return JsonResponse(list(students), safe=False)
def update_items_in_database(name,branch):
    students=Student.objects.get(sname=name)
    students=Student.objects.get(branch=name)

    students.branch="Chemical"
    students.save()

    updated_items=list(Student.objects.all().values())
    channel_layer=get_channel_layer()
    async_to_sync(channel_layer.group_send())(
        "websocket_group",
        {"type":"update_items","students":updated_items},
    )

# Create your views here.
