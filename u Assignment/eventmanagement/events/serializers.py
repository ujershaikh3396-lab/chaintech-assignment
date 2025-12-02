from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "organizer",
            "location",
            "start_time",
            "end_time",
            "is_public",
            "created_at",
            "updated_at",
        ]
