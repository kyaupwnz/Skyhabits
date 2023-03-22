from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.serializers import HabitsSerializer


# Create your views here.
class HabitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)


class PublicHabitsListView(generics.ListAPIView):
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habits.objects.filter(is_public=True)
