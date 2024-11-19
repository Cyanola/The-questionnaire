from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# В views.py
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices,
    }
    return render(request, 'polls/results.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    standard_choices = question.choice_set.filter(choice_text__isnull=False)

    has_standard_choices = standard_choices.exists()
   
    has_custom_answer = not has_standard_choices

    return render(request, 'polls/detail.html', {
        'question': question,
        'has_standard_choices': has_standard_choices,
        'has_custom_answer': has_custom_answer,
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
     
        selected_choice_id = request.POST.get('choice')
        if selected_choice_id:  # если выбран существующий вариант
            choice = question.choice_set.get(pk=selected_choice_id)
            choice.votes += 1
            choice.save()

       
        elif request.POST.get('custom_text'):  
            custom_text = request.POST.get('custom_text').strip()
            if custom_text:  
               
                choice = Choice.objects.create(question=question, user_response=custom_text)
        
        else:
            raise KeyError("Ответ не выбран, и текст не введён.")

    except (KeyError, Choice.DoesNotExist):
       
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Вы не выбрали или не ввели ответ.",
        })

    else:
      
        return HttpResponseRedirect(reverse('results', kwargs={'question_id': question.id}))

  

   

