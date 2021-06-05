from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
# from rest_framework.

from webapp.models import Quote
from api.serializers import QuoteSerializer, QuoteUpdateSerializer

from django.shortcuts import get_object_or_404
import json
class QuoteList(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer
    def get_queryset(self):
        if self.request.user.is_staff:
            return Quote.objects.all()
        return Quote.objects.filter(is_moderated=True)


class QuoteView(generics.RetrieveAPIView):
    serializer_class = QuoteSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        if self.request.user.is_staff:
            return Quote.objects.all()
        return Quote.objects.filter(is_moderated=True)

    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return (AllowAny(),)
    #     return (IsAdminUser(),)


class QuoteUpdateView(generics.UpdateAPIView):
    serializer_class = QuoteUpdateSerializer
    permission_classes = [IsAdminUser]
    queryset = Quote.objects.all()

class QuoteDeleteView(generics.DestroyAPIView):
    serializer_class = QuoteUpdateSerializer
    permission_classes = [IsAdminUser]
    queryset = Quote.objects.all()


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