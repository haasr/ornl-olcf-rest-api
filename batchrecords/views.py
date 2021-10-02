from django.shortcuts import render
from rest_framework import generics # Create generic views
from .models import BatchJob
from .serializers import BatchJobSerializer

class BatchJobList(generics.ListAPIView):
    serializer_class = BatchJobSerializer

    def get_queryset(self):
        """
        View to return a list of all BatchJobs.
        """
        return BatchJob.objects.all()
