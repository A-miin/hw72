from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Quote
from api.serializers import QuoteSerializer
from django.shortcuts import get_object_or_404
import json
class QuoteList(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        if not self.request.user.is_anonymous and self.request.user.is_staff:
            return Quote.objects.all()
        return Quote.objects.filter(is_moderated=True)
    # def get_queryset(self):
    #     if self.request.user.is_authenticated and self.request.user.has_perm()

class QuoteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.filter(is_moderated=True)
    serializer_class = QuoteSerializer
    permission_classes = [3]

class QuoteRate(APIView):
    def get_object(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        quote = self.get_object(pk)
        quote.rate += 1
        quote.save()
        serilizer = QuoteSerializer(instance=quote)
        return Response(serilizer.data)


class QuoteUnrate(APIView):
    def get_object(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        quote = self.get_object(pk)
        quote.rate -= 1
        quote.save()
        serilizer = QuoteSerializer(instance=quote)
        return Response(serilizer.data)
#
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)