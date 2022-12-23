"""Define views for suggestion package"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


from .forms import QuestionaryForm
from .models import QuestionaryModel, SuggestionModel


@login_required(login_url='user:login')
def get_answers(request):

    qs = QuestionaryModel.objects.all().last()
    points = 0
    risk_forecast = [
        "The risk to significantly increase Glucose level in your blood is very high.",
        "The risk to significantly increase Glucose level in your blood is medium.",
        "The risk to significantly increase Glucose level in your blood is low."]
    suggestions = [
        "Visit a doctor! You urgently need to change your lifestyle and your diet.",
        "Eat with diet. Do sport. Physical exercise helps lower your blood sugar level.You\n"+ 
        "\tshould aim for 2.5 hours of activity a week.Move a few minutes after 30 minutes sitting.",
        "You are in good track to be healthy. Keep this style and you will decrease \n" +
        "\tGlucose level  in your blood."
    ]
    if qs.on_a_diet=='Yes':
        points +=5
    if qs.diet_meal_quantity=="Always on diet":
        points +=5
    if qs.diet_meal_quantity=="1 time":
        points +=4
    if qs.diet_meal_quantity=="2 times":
        points +=3
    if qs.diet_meal_quantity=="3 times":
        points +=2
    if qs.diet_meal_quantity=="4 times":
        points +=1
    if qs.phisical_exercises=="Yes, and more then 2 hours per week":
        points +=5
    if qs.phisical_exercises=="Yes, but less then 2 hours per week":
        points +=3
    if qs.physical_activity=="Yes":
        points +=5
    if points < 6:
        forecast = risk_forecast[0]
        suggestion = suggestions[0]
    if points > 5 and points < 13:
        forecast = risk_forecast[1]
        suggestion = suggestions[1]
    if points > 12:
        forecast = risk_forecast[2]
        suggestion = suggestions[2]

    SuggestionModel.objects.create(points_achived=points, suggestion=suggestion, forecast=forecast)
    """calculate BMI"""
    
    obj = SuggestionModel.objects.last()
    max = obj.points_max
    percentage = round(points/max*100, 1)
    context = {
        "points": points,
        "points_max": max,
        "success": percentage,
        "forecast": forecast,
        "suggestion": suggestion
        }
    

    return render(request, 'suggestions/summary.html', context)

login_required(login_url='user:login')
def get_health_answers(request):
    submitted = False

    if request.method == "POST":
        form = QuestionaryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = QuestionaryForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'suggestions/get_health_answers.html', {'form': form, 'submitted': submitted, 'user': request.user.username})

login_required(login_url='user:login')
def print_suggestion(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=suggestion_report.txt'

    # Designate the Model
    q =  QuestionaryModel.objects.last()
    s = SuggestionModel.objects.last()
    # if q.on_a_diet="YES":
    lines = []
    lines.append(f'\n\n\n\t\t\t\t\tSUGGESTION REPORT\n\n\n\t\tQUESTIONARY:\n\n\t\'Are you guided by a diet against diabetes?\': \'{q.on_a_diet}\'\n'
    f'\n\t\'How often do you take a meal without a diet per week?\': \'{q.diet_meal_quantity}\'\n'
    f'\n\t\'Do you do physical exercises?\': \'{q.phisical_exercises}\'\n'
    f'\n\t\'Are you getting up and moving after 30 minutes sitting usually?\': \'{q.physical_activity}\'\n\n'
    f'\n\t\tRESULT:\n\tAchieved points: {s.points_achived} from {s.points_max}\n'
    f'\n\tYou have a healthy life style for {round(s.points_achived/s.points_max*100, 1)}% \n\n'
    f'\n\t\tRISK FORECAST:\n\t{s.forecast}\n\n\t\tSUGGESTION:\n\t{s.suggestion}\n'
    f'\n\n\t\tUser: {request.user.username}\n\t\tDate and time: {q.datetime.strftime("%m/%d/%Y, %H:%M:%S")}')

    # Write to text file
    response.writelines(lines)
    return response