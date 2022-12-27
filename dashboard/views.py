from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from .forms import HealthDataForm
from .models import HealthData

login_required(login_url='user:login')
def add_health_data(request):
    submitted = False

    if request.method == "POST":
        form = HealthDataForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = HealthDataForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'dashboard/add_health_data.html', {'form': form, 'submitted': submitted, })

login_required(login_url='user:login')
def show_health_data(request, data_id):
    data = HealthData.objects.filter(user=request.user).get(pk=data_id)

    if data.day < datetime.date.today():
        time = 'was'

    if data.day == datetime.date.today():
        time = 'is'

    if data.gl_level < 140:
        gl_comment = f"On {data.day} your Glucose level {time} {data.gl_level} mg/dL. It is less then 140 mg/dL and it means, you have normal Glucose level."

    if data.gl_level >= 140 and data.gl_level < 200:
        gl_comment = f"On {data.day} your Glucose level {time} {data.gl_level} mg/dL. It exceeds 140 mg/dL and it means, you have prediabetes. You have Prediabetes."

    if data.gl_level > 200:
        gl_comment = f"On {data.day} your Glucose level {time} {data.gl_level} mg/dL. It exceeds 200 mg/dL and it means, you have diabetes. Please visit your doctor for consultation."

    if data.bmi < 18.5:
        bmi_comment = f"Your body mass index(BMI) {time} {data.bmi}  kg/m^2. It is less then 18,5 kg/m^2 and it means, you have underweight."

    if data.bmi >= 18.5 and data.bmi <=24.9:
        bmi_comment = f"Your body mass index(BMI) {time} {data.bmi} kg/m^2. It is in the range 18,5-24,5 kg/m^2 and it means, you have a normal weight."

    if data.bmi >= 25 and data.bmi <=29.9:
        bmi_comment = f"Your body mass index(BMI) {time} {data.bmi} kg/m^2. It is in the range 25-29,9 kg/m^2 and it means, you have overweight."

    if data.bmi >= 30 and data.bmi <=34.9:
        bmi_comment = f"Your body mass index(BMI) {time} {data.bmi} kg/m^2. It is in the range 30-34,9 kg/m^2 and it means, you have obesity."

    if data.bmi > 35:
        bmi_comment = f"\nYour body mass index(BMI) {time} {data.bmi} kg/m^2. It exceeds 35 kg/m^2 and it means, you have extremely obesity."

    return render(request, 'dashboard/show_data.html', {
                      "data": data,
                      "gl_com": gl_comment,
                      "bmi_com": bmi_comment,
                  })

login_required(login_url='user:login')
def edit_health_data(request, data_id):
    health_record = HealthData.objects.get(pk=data_id)
    form = HealthDataForm(request.POST or None, instance=health_record)
    if form.is_valid():
        form.save()
        return redirect('user:users-home', data_id)

    return render(request, 'dashboard/edit_data.html', {'record': health_record,'form': form})

login_required(login_url='user:login')
def del_health_data(request, data_id):
    event = HealthData.objects.get(pk=data_id)
    event.delete()
    return redirect('user:users-home')

login_required(login_url='user:login')
def print_home_page(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')