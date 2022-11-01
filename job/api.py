#views
import imp
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view([ 'GEt'])
def job_list_api(request):
    alljobs=Job.objects.all()
    data=JobSerializer(alljobs,many=True).data
    return Response({'data':data})

@api_view([ 'GEt'])
def job_detail_api(request,id):
    job_detail=Job.objects.get(id=id)
    data=JobSerializer(job_detail ).data
    return Response({'data':data})

class Job_listapi(generics.ListAPIView):
    model=Job
    queryset=Job.objects.all()
    serializer_class=JobSerializer
class JobDetial(generics.RetrieveUpdateDestroyAPIView):

    queryset=Job.objects.all()

    serializer_class=JobSerializer
    lookup_field='id'


     