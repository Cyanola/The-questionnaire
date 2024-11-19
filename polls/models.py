from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, blank=True, null=True)
    votes = models.IntegerField(default=0)
    user_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.choice_text if self.choice_text else "Custom Answer"
