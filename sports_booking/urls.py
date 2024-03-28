from django.urls import path, include

from sports_booking import views


urlpatterns = [
    path('sports-facility/', views.SportsFacilityListView.as_view()),
    path('sports-facility/<int:pk>/', views.SportsFacilityDetailView.as_view()),
]