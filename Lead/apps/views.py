from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Classroom, Bulb,Status

import requests
Userver = "blr1.blynk.cloud"
def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        if (username == 'Lead@Head' and password == '1234') or \
                (username == 'Lead@Control' and password == '1234') or \
                (username == 'Grow@Dev' and password == '1234'):
            request.session['username'] = username
            return redirect('index/')
        else:
            error_message = "Invalid Login"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def index(request):
    classrooms = Classroom.objects.all()
    return render(request,'index.html',{'classrooms':classrooms})
def bulb_control(request, classroom_id):
    classrooms1 = Classroom.objects.all()
    classroom = get_object_or_404(Classroom, id=classroom_id)
    bulbs = Bulb.objects.filter(classroom=classroom)
    statuss = Status.objects.filter(classroom=classroom)
    return render(request, 'bulb_control.html', {'classroom': classroom, 'bulbs': bulbs,'classrooms1':classrooms1,'statuss': statuss})
def update_pin(request, classroom_id, bulb_id):
    classrooms1 = Classroom.objects.all()
    if request.method == 'POST':
        pin = request.POST.get('pin')
        status = request.POST.get('status')

        # Update the bulb status
        bulb = get_object_or_404(Bulb, id=bulb_id)
        bulb.status = 1 if status.lower() == 'on' else 0
        bulb.save()

        # Send API request to update the physical bulb
        classroom = get_object_or_404(Classroom, id=classroom_id)
        token = classroom.token  # Access the token from the Classroom model
        url = f"https://{Userver}/external/api/update?token={token}&{pin}={bulb.status}"
        requests.get(url)


    classroom = get_object_or_404(Classroom, id=classroom_id)
    bulbs = Bulb.objects.filter(classroom=classroom)
    return render(request, 'bulb_control.html', {'classroom': classroom, 'bulbs': bulbs,'classrooms1':classrooms1})
def get_status(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    statuss = Status.objects.filter(classroom=classroom)

    status_data = []
    for sts in statuss:
        url = f"https://{Userver}/external/api/get?token={classroom.token}&pin={sts.pin}"
        response = requests.get(url)
        status = response.text
        status_data.append({'id': sts.id, 'status': status})



    return JsonResponse(status_data, safe=False)
