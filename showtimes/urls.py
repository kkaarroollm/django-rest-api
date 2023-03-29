from django.urls import path
from .views import CinemaListView, CinemaView, ScreeningView, ScreeningListView

app_name = 'showtimes'

urlpatterns = [
    path('cinemas/', CinemaListView.as_view(), name='cinemas'),
    path('cinemas/<int:pk>', CinemaView.as_view(), name='cinema'),
    path('screening/', ScreeningListView.as_view(), name='screenings'),
    path('screening/<int:pk>', ScreeningView.as_view(), name='screening'),
]