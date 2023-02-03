from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.
class Quiz(models.Model):
	name = models.CharField(max_length=1000)
	questions_count = models.IntegerField(default=0)
	description = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	slug = models.SlugField()
	roll_out = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("vote", kwargs={"pk": self.pk})

class Meta:
	ordering = ['created',]
	verbose_name_plural = "Quizzes"
	db_table = 'Answer'

	def __str__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	label = models.CharField(max_length=1000)
	order = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')
	last_answer_time = models.DateTimeField(null=True)

	def __str__(self):
		return self.label

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def get_next(self):
		next = Question.objects.filter(id__gt=self.id).order_by('id').first()
		if next:
			return next
		else:
			return none


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=1000)
	is_correct = models.BooleanField('Correct answer', default=False)

	def __str__(self):
		return self.text
		

### Save current score ###
class Scorer(models.Model):
	score = models.IntegerField(default=0)
	page = models.IntegerField()

