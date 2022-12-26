from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

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
    
    if data.gl_level < 140:
        gl_comment = f"Your glucose level is {data.gl_level}. It is less then 140 mg/dL. It means, you have normal Glucose llevel."

    if data.gl_level >= 140 and data.gl_level < 200:
        gl_comment = f"Your glucose level is {data.gl_level}. It exceeds 140 mg/dL. It means, you have prediabetes. You have Prediabetes."

    if data.gl_level > 200:
        gl_comment = f"Your glucose level is {data.gl_level}. It exceeds 200 mg/dL. It means, you have diabetes. Please visit your doctor for consultation."

    if data.bmi < 18.5:
        bmi_comment = f"\nYour body mass index(BMI) is {data.bmi}. It is less then 18,5 kg/m^2. It means, you have underweight."

    if data.bmi >= 18.5 and data.bmi <=24.9:
        bmi_comment = f"\nYour body mass index(BMI) is {data.bmi}. It is in the range 18,5-24,5 kg/m^2. It means, you have a normal weight."

    if data.bmi >= 25 and data.bmi <=29.9:
        bmi_comment = f"\nYour body mass index(BMI) is {data.bmi}. It is in the range 25-29,9 kg/m^2. It means, you have overweight."

    if data.bmi >= 30 and data.bmi <=34.9:
        bmi_comment = f"\nYour body mass index(BMI) is {data.bmi}. It is in the range 30-34,9 kg/m^2. It means, you have obesity."

    if data.bmi > 35:
        bmi_comment = f"\nYour body mass index(BMI) is {data.bmi}. It exceeds 35 kg/m^2. It means, you have extremely obesity."
    comment = f'{gl_comment}\n{bmi_comment}'

    return render(request, 'dashboard/show_data.html', {
                      "data": data,
                      "comment": comment,
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