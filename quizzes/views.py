

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import TemplateView, ListView
from django.template.response import TemplateResponse


from flask import Flask, render_template
from .models import Quiz, Meta, Question, Answer, Scorer

# Create your views here.


### For homepage view ###
class IndexView(generic.ListView):
	template_name = 'quizzes/index.html'
	context_object_name = 'latest_question_list'

	
	
	def get_queryset(self):
		
		scorer, created = Scorer.objects.update_or_create(page=0)
		
		### To reset scores to 0 ###
		if Question.objects.filter(id=1):
			scorer.score = (scorer.score - scorer.score)
			scorer.save()

		"""Return the first published question """
		return Question.objects.filter(id=1)


### Each question's view ###
class DetailView(generic.DetailView):
	model = Question 
	template_name = 'quizzes/detail.html'




	def get_queryset(self):
		"""Return the last ten published questions (not including those set to be published in the future). """
		return Question.objects.filter(pub_date__lte=timezone.now())



	


### Results View ###
def vote(request, question_id, *args, **kwargs):
	model = Question
	template_name = 'quizzes/vote.html'
	question = get_object_or_404(Question, pk=question_id)

	### For template link to redirect ###
	first = Question.objects.get(pk=question_id)
	last = Question.objects.get(id=10)

	
	### To create user scoring system ###
	scorer, created = Scorer.objects.update_or_create(page=0)

	try:
		selected_choice = question.answer_set.get(pk=request.POST['answer'])


		### To save user score ###
		if selected_choice in Answer.objects.filter(id=1):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=6):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=12):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=13):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=19):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=22):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=28):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=30):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=36):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=37):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=38):
			scorer.score +=10
			scorer.save()

		if selected_choice in Answer.objects.filter(id=40):
			scorer.score += 10
			scorer.save()
			

		### For conditional background based on user selected answer ###
		context_dict = {}
		context_dict['selected_choice'] = str(selected_choice)
		context_dict['question'] = str(question)
		context_dict['score'] = str(scorer.score)
		context_dict['ans1'] = str(Answer.objects.get(id=1))
		context_dict['ans2'] = str(Answer.objects.get(id=6))
		context_dict['ans3'] = str(Answer.objects.get(id=12))
		context_dict['ans4'] = str(Answer.objects.get(id=13))
		context_dict['ans5'] = str(Answer.objects.get(id=19))
		context_dict['ans6'] = str(Answer.objects.get(id=22))
		context_dict['ans7'] = str(Answer.objects.get(id=28))
		context_dict['ans8'] = str(Answer.objects.get(id=30))
		context_dict['ans9'] = str(Answer.objects.get(id=36))
		context_dict['ans10'] = str(Answer.objects.get(id=37))
		context_dict['ans11'] = str(Answer.objects.get(id=38))
		context_dict['ans12'] = str(Answer.objects.get(id=40))

		
		context_dict['first'] = first
		context_dict['last'] = last


		### Passing a context dictionary from vote view to final_score view ###
		request.session['score'] = str(scorer.score)
		

	
	except (KeyError, Answer.DoesNotExist, ObjectDoesNotExist, MultipleObjectsReturned):
		pass

	# Redisplay the question voting form.
		return render(request, 'quizzes/detail.html', {'question': question })
	
	else:



		return render(request, 'quizzes/vote.html', context_dict)





### Final results once quiz is completed ###
class Final_ScoreView(generic.DetailView):
	model = Question
	template_name = 'quizzes/final_score.html'


	

