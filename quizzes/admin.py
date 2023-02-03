from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Answer

# Register your models here.
class AnswerInline(nested_admin.NestedTabularInline):
	model = Answer
	extra = 4
	max_num = 4

class QuestionInline(nested_admin.NestedTabularInline):
	model = Question
	inlines = [AnswerInline,]
	extra = 11

class QuizAdmin(nested_admin.NestedModelAdmin):
	inlines = [QuestionInline,]



admin.site.register(Quiz, QuizAdmin)

