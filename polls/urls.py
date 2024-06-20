from django.urls import path

from . import views

urlpatterns = [
    path("choices/<int:pk>/", views.ChoiceDetail.as_view(), name="choice-detail"),
    path("choices/", views.ChoiceList.as_view(), name="choice-list"),
    path("questions/<int:pk>/", views.QuestionDetail.as_view(), name="question-detail"),
    path("questions/", views.QuestionList.as_view(), name="question-list"),
    path("", views.api_root, name="base-api"),
]
