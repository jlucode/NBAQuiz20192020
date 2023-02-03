from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView




app_name = 'quizzes'
urlpatterns = [
	# ex: /quizzes/
	path('', views.IndexView.as_view(), name= 'index'),
	# ex: /quizzes/5/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: /quizzes/5/results/
	path('<int:question_id>/vote/', views.vote, name= 'vote'),
	# ex: /quizzes/final_score/
	path('<int:pk>/final_score/', views.Final_ScoreView.as_view(), name= 'final_score'),

	



]

urlpatterns += staticfiles_urlpatterns() 