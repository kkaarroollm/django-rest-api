from rest_framework import generics
from .models import Cinema, Screening
from .serializers import CinemaSerializer, ScreeningSerializer


class CinemaListView(generics.ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class ScreeningListView(generics.ListAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer


class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer

