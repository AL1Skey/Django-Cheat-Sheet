from django.db import models

# Create your models here.
class Quest(models.Model):
    quest_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) : #This is to print quest_text when called
        return self.quest_text

class Option(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE) #If Quest is deleted, then quest is deleted too
    choice_text = models.CharField(max_length=200) #Displaying choice text in web
    votes = models.IntegerField(default=0)

    def __str__(self) :
        return self.choice_text
