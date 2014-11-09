from teams.models import Team, Member
from rest_framework import serializers

class MemberSerializer(serializers.HyperlinkedModelSerializer):

	name = serializers.CharField()
	email = serializers.EmailField()
	
	grade = serializers.IntegerField()
	section = serializers.CharField()


	class Meta:
		model = Member
		fields = ('name', 'grade', 'section', 'team')


class TeamSerializer(serializers.HyperlinkedModelSerializer):

	members = MemberSerializer(many = True, read_only = True)

	class Meta:
		model = Team
		fields = ('name', 'rank', 'members', 'password')