"""Views for learning package"""
from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Material
from .models import Question, Answer
from .models import Result
from .models import Quiz

# Create your views here.
@login_required(login_url='user:login')
def list_cards(request):
    cards = Material.objects.all().order_by('created_date')
    return render(request, 'learning/base.html', {"cards": cards})

@login_required(login_url='user:login')
def show_card(request, card_id):
    card = Material.objects.get(pk=card_id)
    return render(request, 'learning/show_card.html', {
                      "card": card,
                  })

# @login_required(login_url='user:login')
class QuizListView(ListView):
    model = Quiz 
    template_name = 'learning/quiz_main.html'
 
@login_required(login_url='user:login')
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'learning/quiz.html', {'obj': quiz})

@login_required(login_url='user:login')
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

@login_required(login_url='user:login')
def save_quiz_view(request, pk):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})
