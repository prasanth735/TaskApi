from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView

from api.models import Task
from api.serializers import TaskSerialzer,UserSerializer



# Create your views here.



class TaskViewsetView(ViewSet):

    def list(self,request,*args,**kwargs):
        
        qs=Task.objects.all()
        serializer_instance=TaskSerialzer(qs,many=True)

        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)


    def create(self,request,*args,**kwargs):

        data=request.data
        serializer_instance=TaskSerialzer(data=data)
        if serializer_instance.is_valid():
            # task.objects.create
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_406_NOT_ACCEPTABLE)


    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk") 
        qs=Task.objects.get(id=id)
        serializer_instance=TaskSerialzer(qs)

        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)

    

    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        task_obj=Task.objects.get(id=id)
        serializer_instance=TaskSerialzer(data=request.data,instance=task_obj)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        
        return Response(data=serializer_instance.errors,status=status.HTTP_404_NOT_FOUND)


    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Task.objects.get(id=id).delete()
        return Response(data={"message":"deleted"},status=status.HTTP_200_OK)



class UserView(APIView):

    def post(self,request,*args,**kwargs):
        
        serializer_instance=UserSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer_instance.errors,status=status.HTTP_406_NOT_ACCEPTABLE)