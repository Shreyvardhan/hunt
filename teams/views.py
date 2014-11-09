from django.shortcuts import render
from teams.models import Team, Member
from rest_framework import viewsets
from teams.serializers import TeamSerializer, MemberSerializer

class TeamViewSet(viewsets.ModelViewSet):

	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class MemberViewSet(viewsets.ModelViewSet):

	queryset = Member.objects.all()
	serializer_class = MemberSerializer

# Create your views here.
