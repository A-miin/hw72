from django.urls import path

from api.views import QuoteList, QuoteView, QuoteRate, QuoteUnrate

from rest_framework import permissions


urlpatterns = [
    path('quote/', QuoteList.as_view(), name='quote-list'),
    path('quote/<int:pk>/', QuoteView.as_view(), name='quote-view' ),
    path('quote/<int:pk>/rate/', QuoteRate.as_view(), name='quote-rate'),
    path('quote/<int:pk>/unrate/', QuoteUnrate.as_view(), name='quote-unrate'),
]
