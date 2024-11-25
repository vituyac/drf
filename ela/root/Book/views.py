from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render
from .documents import BookDocument
from rest_framework.response import Response
from rest_framework import generics
from elasticsearch_dsl.query import MultiMatch
from .models import *
from .serializers import *

class BookAdd(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
    
    
class BookSearch(APIView):
    
    def get(self, request):
        q = request.GET.get("q")
        context = {}
        if q:
            query = MultiMatch(query=q, fields=["title", "description"], fuzziness="AUTO")
            s = BookDocument.search().query(query)[0:5]
            context["books"] = [hit.title for hit in s]
        return Response(context)
