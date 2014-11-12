from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class TeamManager(BaseUserManager):
	
	def create_user(self, name, password = None):
		
		user = self.model(name = name,)

		user.set_password(password)
		user.save(using = self._db)

		return user

	def create_superuser(self, name, password):
		user = self.create_user(name, password = password)
		user.is_admin = True
		user.save(using = self._db)
		return user

"""
Custom User Class
"""
class Team(AbstractBaseUser):

	name = models.CharField(max_length = 254, unique = True, verbose_name = u'Name')
	level = models.IntegerField(null = True, blank = True, default = 0, verbose_name = u'Level')
	last_level_time = models.DateTimeField(auto_now_add = False, null = True, blank = True, verbose_name = u'Time When Last Level Was Cleared')
	cheated = models.BooleanField(default = False, verbose_name = u'Cheaters?')
	is_active = models.BooleanField(default = True)
	is_admin = models.BooleanField(default = False)
	
	objects = TeamManager()

	USERNAME_FIELD = 'name'
	
	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name

	def has_perm(self, perm, obj = None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
	    return self.is_admin

"""
Team Member Class
"""
class Member(models.Model):

	# SECTION_CHOICES = (

	# 	('A', 'A'), 
	# 	('B', 'B'), 
	# 	('C', 'C'), 
	# 	('D', 'D'), 
	# 	('E', 'E'),

	# )

	# GRADE_CHOICES = (

	# 	(8, '8'),
	# 	(9, '9'),
	# 	(10, '10'),
	# 	(11, '11'),
	# 	(12, '12'),

	# )

	name = models.CharField(max_length = 254, null = True, blank = True)
	team = models.ForeignKey(Team, related_name = 'members', null = True, blank = True)
	email = models.EmailField(null = True, blank = True, max_length = 254)
	
	grade = models.CharField(max_length = 222, null = True, blank = True)
	section = models.CharField(max_length = 222,null = True, blank = True)

	def __unicode__(self):
		return self.name

	def get_admin_url(self):
		return "/admin/teams/member/%s/" % self.id	