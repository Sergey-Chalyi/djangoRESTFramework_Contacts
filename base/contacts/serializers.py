from dataclasses import fields

from rest_framework import serializers
from rest_framework.response import Response

from contacts.models import Contact

# сериализатор для класса представления
# class ContactsSerializer(serializers.ModelSerializer):
#     class Meta:
#         # модель, для которой будет создан сериализатор
#         model = Contact
#         # поля, которые будут возвращаться API
#         fields = ('first_name', 'last_name', 'phone_number', 'email')



# преобразовывает данные в JSON формат
# тут по сути тоже проходит валидация значений (сначала тут, а потом уже на уровне модели)
# class ContactSerializer(serializers.Serializer):
#     # объявляем, что first_name это CharField
#     # first_name должно быть таким же по имени, как в ContactModel
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)
#     phone_number = serializers.CharField(max_length=255)
#     email = serializers.CharField()
#
#     # метод, чтобы сериализатор сам сохранял объекты в бд
#     def create(self, validated_data):
#         return Contact.objects.create(**validated_data)
#
#     # для обновления данных
#     def update(self, instance, validated_data):
#         # instance - это объект самой модели
#         # validated_data - словарь с данными для обновления
#         instance.first_name = validated_data.get('first_name', instance.first_name) # второй параметр - если нее получится обновить данные, то подставиться это значение
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.phone_number = validated_data.get('phone_number', instance.phone_number)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # можно просто указать "__all__"
        fields = "__all__"
