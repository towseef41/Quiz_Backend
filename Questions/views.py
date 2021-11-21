from django.core.exceptions import AppRegistryNotReady
from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Round, Question
from rest_framework import status
from .serializers import *
import random

class RoundView(APIView):

    def get(self, request, *args, **kwargs):
        rounds = Round.objects.all()
        ser = RoundSerializer(rounds, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

class QuestionView(APIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        ser = QuestionSerializer(questions, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

class QuestionByRound(APIView):
    def get(self, request, *args, **kwargs):
        round_number = request.data.get('round_number')
        round_object = Round.objects.get(round_number=round_number)
        questions = Question.objects.filter(belongs_to=round_number)
        ser = QuestionSerializer(questions, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

class AnswerByQuestionView(APIView):
    def get(self, request, *args, **kwargs):
        question_id = request.GET.get('question_id')
        question_object = Question.objects.get(id=question_id)
        answer = Answer.objects.get(question=question_object)
        ser = AnswerSerializer(answer)
        return Response(ser.data, status.HTTP_200_OK)

class GenerateRandomTask(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(used=False)
        if(len(tasks) == 0):
            tasks = tasks.objects.all()
            for task in tasks:
                task.used = False
                task.save()
        index = random.randint(0, len(tasks))
        task_object = tasks[index]
        task_object.used = True
        task_object.save()
        ser = TaskSerializer(task_object)
        return Response(ser.data, status=status.HTTP_200_OK)


