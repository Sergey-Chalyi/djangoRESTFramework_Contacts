from multiprocessing.connection import Connection

from django.forms import model_to_dict
from django.shortcuts import render
from django.utils.termcolors import color_names
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.models import Contact
from contacts.serializers import ContactSerializer


# # создание класса представления для API (на основе сериализатора)
# class ContactsAPIView(generics.ListAPIView):
#     # получаем все доступные из модели объекты
#     queryset = Contact.objects.all()
#     # устанавливаем сериализатор
#     serializer_class = ContactsSerializer

# можно использовать встроенные классы представления
class ContactsAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# class ContactsAPIView(APIView):
#     def get(self, request):
#         contacts = Contact.objects.all()
#         # ContactSerializer - сериализатор для данного класса
#         # many=True - сериализатор должен обрабатывать список записей (а не одну запись)
#         # Response преобразовывает все в байтовую JSON строку
#         return Response({'posts' : ContactSerializer(contacts, many=True).data})
#
#
#     # метод для обработки post запросов
#     def post(self, request):
#         serializer = ContactSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # возвращаем словарь, который потом будет преобразовать в JSON
#         return Response({'result' : serializer.data})
#
#
#     # метод для обработки put запросов (обновление)
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error" : "Method PUT is not allowed"})
#
#         try:
#             instance = Contact.objects.get(pk=pk)
#         except:
#             return Response({"error" : "Object doesn't exist"})
#
#         # instance - запись, которую мы будем менять на request.data
#         serializers = ContactSerializer(data=request.data, instance=instance)
#         serializers.is_valid(raise_exception=True)
#         # т.к. у ContactSerializer 2 параметра в конструкторе, то save вызовет метод updata
#         serializers.save()
#         return Response({"post" : serializers.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error" : "Method PUT is not allowed"})
#
#         try:
#             instance = Contact.objects.get(pk=pk)
#         except:
#             return Response({"error" : "Object doesn't exist"})
#
#         Contact.objects.get(pk=pk).delete()
#         return Response({"delete": "TRUE"})
