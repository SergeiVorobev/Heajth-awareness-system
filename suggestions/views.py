"""Define views for suggestion package"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from .forms import SliderForm
from .models import SliderModel

@login_required(login_url='user:login')
def home(request):

    qs = SliderModel.objects.all()
   
    x_gl = [0]
    x_w = [0]
    y = []
    for data in qs:
        x_gl.append(data.name_range_field)
        x_w.append(data.range_field)
        y.append(data.label_range_field)


    context = {
                "nrf": x_gl,
                "rf": x_w,
                "lrf": y,
                }

    return render(request, 'base/home.html', context)

login_required(login_url='user:login')
def get_health_answers(request):
    submitted = False

    if request.method == "POST":
        form = SliderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('get-health-answers?submitted=True')
    else:
        form = SliderForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'suggestions/get_health_answers.html', {'form': form, 'submitted': submitted, })