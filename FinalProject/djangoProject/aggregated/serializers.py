from django.contrib.auth.models import User, Group
from aggregated.models import Participants, ListEmails, Aggregate
from rest_framework import serializers
from django.core.serializers.json import Serializer


class ListEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListEmails
        fields = ['email']

    def get_queryset(self):
        return ListEmails.objects.all()

class ParticipantSerializer(serializers.ModelSerializer):
    participant = serializers.StringRelatedField(many=True)
    value = serializers.CharField(source='Name')

    class Meta:
        model = Participants
        fields = ['id', 'value', 'status', 'participant']


class AggregateSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer()

    class Meta:
        model = Aggregate
        fields = ('participant', 'time_on_less', 'date')
