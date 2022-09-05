from django.contrib.auth.models import User, Group
from aggregated.models import Participants, ListEmails, Aggregate
from rest_framework import serializers
from django.core.serializers.json import Serializer


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participants
        fields = ['Name']


class ListEmailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListEmails
        fields = ['user', 'email']

class AggregateSerializer(serializers.ModelSerializer):
    user = ParticipantSerializer(source='participant')
    # email = ListEmailsSerializer( many=True)
    class Meta:
        model = Aggregate
        fields = ('user', 'time_on_less', 'date')

