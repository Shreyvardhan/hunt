from teams.models import Team, Member
from rest_framework import serializers

class MemberSerializer(serializers.HyperlinkedModelSerializer):

	name = serializers.CharField()
	email = serializers.EmailField()
	
	grade = serializers.IntegerField()
	section = serializers.CharField()

	class Meta:
		model = Member
		fields = ('name', 'grade', 'section')

members = MemberSerializer(many = True)

class TeamSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Team
		fields = ('name', 'rank', 'level','url', 'cheated')
		ordering = ('-rank')
		depth = 1