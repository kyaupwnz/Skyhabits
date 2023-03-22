from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class Telegram(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        return Response({"url": "t.me/Kyau_habits_bot"})
