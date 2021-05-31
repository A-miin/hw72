from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import CreateView
from webapp.models import Quote
from webapp.forms import QuoteForm
from django.urls import reverse_lazy

#
# class IndexView(CreateView):
#     template_name = 'index.html'
#     form_class = QuoteForm
#     model = Quote
#     success_url = reverse_lazy('index')

class IndexView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')