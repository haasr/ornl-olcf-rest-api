from rest_framework import serializers
from .models import *

class BatchJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchJob
        fields = [
            'pk',
            'batch_number',
            'submitted_at',
            'nodes_used',
        ]