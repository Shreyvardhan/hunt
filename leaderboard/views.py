from django.shortcuts import render
from teams.models import Team, Member, Log
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def leaderboard(request):

	teams = Team.objects.all()
	teams = teams.order_by('level'])
	teams = teams.order_by(['last_level_time'])

	level_2 = len(Team.objects.filter(level = 2))
	level_3 = len(Team.objects.filter(level = 3))
	level_4 = len(Team.objects.filter(level = 4))
	level_5 = len(Team.objects.filter(level = 5))
	level_6 = len(Team.objects.filter(level = 6))

	return render_to_response('teams/leaderboard.html', { 'teams': teams, 'level_4': level_4, 'level_5': level_5, 'level_6': level_6 }, context_instance = RequestContext(request))