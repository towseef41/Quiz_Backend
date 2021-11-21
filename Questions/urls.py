from django.urls import path
from .views import *

url_patterns = [
    path('/getAllRounds', RoundView.as_view()),
    path('/getRoundsByQuestion', QuestionByRound.as_view()),
    path('/getAnswerByQuestion', AnswerByQuestionView.as_view()),
    path('/generateRandomTask', GenerateRandomTask.as_view()),
    
]