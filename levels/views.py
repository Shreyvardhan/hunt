import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Question 1: Hi.")
