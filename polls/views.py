from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Choice, Question
from .permissions import IsOwnerOrReadOnly
from .serializers import ChoiceSerializer, QuestionSerializer


@api_view(["GET"])
def api_root(request):
    return Response(
        {
            "questions": reverse("question-list", request=request),
            "choices": reverse("choice-list", request=request),
        }
    )


class QuestionList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Question.objects.order_by("-pub_date")
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Question.objects.order_by("-pub_date")
    serializer_class = QuestionSerializer


class ChoiceList(generics.ListAPIView):
    queryset = Choice.objects.order_by("-pk")
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveAPIView):
    queryset = Choice.objects.order_by("-pk")
    serializer_class = ChoiceSerializer
