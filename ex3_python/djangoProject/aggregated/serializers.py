from django.contrib.auth.models import User, Group
from aggregated.models import Participants, ListEmails, Aggregate
from rest_framework import serializers
from django.core.serializers.json import Serializer


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = ['Name']


class ListEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListEmails
        fields = ['user', 'email']

class AggregateSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer()
    print(participant)
    # Participant_Name = serializers.SerializerMethodField(source='Participant.Name')

    # email = ListEmailsSerializer( many=True)
    class Meta:
        model = Aggregate
        fields = ('participant', 'time_on_less', 'date')
