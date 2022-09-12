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
    # emails = serializers.StringRelatedField(many=True)
    # emails = ListEmailsSerializer(many=True, read_only=True)

    # emails = serializers.StringRelatedField()
    participant = serializers.StringRelatedField(many=True)


    class Meta:
        model = Participants
        fields = ['Name', 'participant']


class AggregateSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer()

    # Participant_Name = serializers.SerializerMethodField(source='Participant.Name')

    # email = ListEmailsSerializer( many=True)
    class Meta:
        model = Aggregate
        fields = ('participant', 'time_on_less', 'date')
