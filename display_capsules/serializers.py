from rest_framework import serializers
from display_capsules.models import SpaceCapsules

class CapsuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=SpaceCapsules 
        fields=('CapsuleId','CapsuleSerial', 'Status', 'OriginalLaunch','Missions','Landings', 'Type', 'Details', 'ReuseCount')

