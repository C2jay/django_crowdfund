from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status, permissions, filters, generics
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication

import logging



class ProjectList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self, search_category="CP"):
        return Project.objects.filter(category__exact=search_category)

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        print(self.get_queryset())
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        logger = logging.getLogger('django.server')
        logger.error("What the what")
        logger.error(str(serializer.errors))
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        print(self.total_pledges(pk))
        return Response(serializer.data)
    
    def put(self, request, pk):
        print("1")
        project = self.get_object(pk)
        print("2")
        self.check_object_permissions(request, project)
        print("3")
        data = request.data
        print("4")
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        print("5")
        if serializer.is_valid():
            serializer.save()
            return Response(
                    serializer.data,
                    status=status.HTTP_202_ACCEPTED
                )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request,pk):
        project = self.get_object(pk)
        self.check_object_permissions(request, project)
        project.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def get_pledges(self, pk):
        return Pledge.objects.filter(project__exact=self.get_object(pk))
    
    def total_pledges(self, pk):
        total = 0
        for pledge in self.get_pledges(pk):
            total += pledge.amount
        return total


class PledgeList(APIView):

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )




