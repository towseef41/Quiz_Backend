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
        print(round_number)
        if round_number is None:
            return Response({'error': 'expecting round number in request'}, status=status.HTTP_400_BAD_REQUEST)
        round_object = Round.objects.get(round_number=round_number)
        questions = Question.objects.filter(belongs_to=round_object)
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
            tasks = Task.objects.all()
            for task in tasks:
                task.used = False
                task.save()
        tasks = Task.objects.filter(used=False)
        index = random.randint(0, len(tasks)-1)
        task_object = tasks[index]
        task_object.used = True
        task_object.save()
        ser = TaskSerializer(task_object)
        return Response(ser.data, status=status.HTTP_200_OK)


