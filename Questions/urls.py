from django.urls import path
from .views import *

urlpatterns = [
    path('getAllRounds/', RoundView.as_view()),
    path('getQuestionsByRound/', QuestionByRound.as_view()),
    path('getAnswerByQuestion/', AnswerByQuestionView.as_view()),
    path('generateRandomTask/', GenerateRandomTask.as_view()),

]