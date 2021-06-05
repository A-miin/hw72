from django.urls import path
from rest_framework.authtoken import views

from api.views import QuoteList, QuoteView, QuoteRate, QuoteUnrate, QuoteUpdateView, QuoteDeleteView


from rest_framework import permissions


urlpatterns = [
    path('quote/', QuoteList.as_view(), name='quote-list'),
    path('quote/<int:pk>/', QuoteView.as_view(), name='quote-view' ),
    path('quote/<int:pk>/edit', QuoteUpdateView.as_view(), name='quote-update' ),
    path('quote/<int:pk>/delete', QuoteDeleteView.as_view(), name='quote-delete' ),
    path('quote/<int:pk>/rate/', QuoteRate.as_view(), name='quote-rate'),
    path('quote/<int:pk>/unrate/', QuoteUnrate.as_view(), name='quote-unrate'),
    path('user/login/',views.obtain_auth_token)
]
