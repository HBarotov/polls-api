from rest_framework import serializers

from .models import Choice, Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Question
        fields = ["url", "id", "creator", "question_text", "pub_date"]


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ["url", "id", "choice_text", "votes", "question"]
