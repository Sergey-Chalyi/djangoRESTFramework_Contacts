from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # можно просто указать "__all__"
        fields = "__all__"
