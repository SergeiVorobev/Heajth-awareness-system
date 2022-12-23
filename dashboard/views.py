from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import HealthDataForm

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

    return render(request, 'base/add_health_data.html', {'form': form, 'submitted': submitted, })

# @login_required(login_url='login')
# def show_data(request, event_id):
#     event = Event.objects.get(pk=event_id)
#     return render(request, 'events/event_show.html', {
#                       "event": event,
#                   })