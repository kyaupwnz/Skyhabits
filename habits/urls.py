from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitsViewSet, PublicHabitsListView

app_name = HabitsConfig.name
router = DefaultRouter()
router.register(r'', HabitsViewSet, basename='habits')

urlpatterns = [
    path('public_habits/', PublicHabitsListView.as_view(), name='public_habits_list'),
              ] + router.urls
