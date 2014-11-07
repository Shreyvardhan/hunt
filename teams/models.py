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

	name = models.CharField(max_length = 254, unique = True)
	rank = models.IntegerField(null = True, blank = True)
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

	SECTION_CHOICES = (

		('A', 'A'), 
		('B', 'B'), 
		('C', 'C'), 
		('D', 'D'), 
		('E', 'E'),

	)

	GRADE_CHOICES = (

		(6, '6'),
		(7, '7'),
		(8, '8'),
		(9, '9'),
		(10, '10'),
		(11, '11'),
		(12, '12'),

	)

	name = models.CharField(max_length = 254)
	team = models.ForeignKey(Team)
	email = models.EmailField(null = True, blank = True, max_length = 254)
	
	grade = models.IntegerField(max_length = 2, null = True, blank = True, choices = GRADE_CHOICES)
	section = models.CharField(max_length = 2,null = True, blank = True, choices = SECTION_CHOICES)

	def __unicode__(self):
		return self.name