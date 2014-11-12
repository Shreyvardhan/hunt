# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from teams.models import Team, Member 
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from array import *

from django.shortcuts import render_to_response

# Create your views here.
def level(request):

	team = Team.objects.filter(name = request.user)[0]
	question = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	answer[5] = "nissangtr"
	answer[1] = "daisy"
	question[0] = "Jobs"
	answer[3] = "telescope"
	answer[4] = "1945"
	answer[0] = "steve"

	answer[2] = "frankincense"
	question[1] = """
	<p>Greetings, detective, and welcome to the world of Pokemon.</p>

	<p>There’s a storm brewing this evening, and so is a battle. The wind is stirring up the shrubs, sending Rattata scurrying for cover. Looking up through the tall grass towards the greying sky, Bulbasaur finds an angry Zapdos suddenly descending upon him. Readying himself for combat, he uses Razor Leaf on his approaching foe. Zapdos dodges and screeches in annoyance as rain beats down on his wings.</p>

	<p>Mildly alarmed by the proceedings nearby, Goldeen retreats deeper into his home of pond reeds. All this turbulence is not to his taste. Meanwhile, Zapdos charges downwards, unleashing upon his opponent a powerful round of Thundershock. Although confident of victory, he is forced by the downpour to fly away in search of cover.</p>

	<p>The next day, the effects of the storm are evident. Bulbasaur, however, roams merrily in the bushes, unscathed by the recent battle. Floating lifeless on the surface of the pond amid the withered reeds, ironically enough, is Goldeen.</p>

	<p>Strange isn’t it, Detective? That’s why we need your assistance. You must find out what it was that killed Goldeen.</p>

	<p>What’s that? You require a laboratory?</p>
	<p>Of course, sir. Please follow me.</p>

	<p>Here we are. You’ll find all the equipment and chemicals you may need for your study.</p>

	<p>There is one glitch, though. We don’t have electricity at the moment.</p>
	<p>I hope that won’t hinder your study. I’ll be back tomorrow to discuss your findings.</p>

	<p>x__________________x</p>

	<p>You get to work in the laboratory. The lack of electricity is certainly a nuisance, but you finally manage to find out the cause of Goldeen’s demise. You are fascinated by the results, and decide to experiment further.</p>

	<p>Yes! You’ve done it. You’ve succeeded in recreating the conditions of yesterday’s unfortunate events, and the outcome explains it all. Give yourself a pat on the back, but don’t get ahead of yourself. You owe your success to someone who’s already done this before. In fact, he was the very first to discover this method. What a brilliant man he was.</p>

	<p>It won’t do to let his legacy be lost. You decide to immortalize him in your own way.</p>
	<p>But how?</p>

	<p>The most convenient recourse would be to name someone after him.</p>
	<p>But who?</p>

	<p>Aha! It’ll have to be the little blue pet you have waiting for you back home. An odd little troupe of friends he has; the oddest would have to be the hyper one who prefers wheels to feet. The wheels are never in fours; always in sixes, twos and frequent ones. The sunny disposition makes her quite amiable, but for the life of you, you can’t remember her name.

	<p>It’s time you jog your memory, and tell us what you find.</p>
	"""

	question[2] = """
	<p>Once upon a time, members of a family that hadn’t yet become a family bumped into each other on the street and said, “You’ll do.” Years later, I knew these people as my grandparents.</p>

	<p>By the time I was four, they knew I was special. Growing up, I saw the world trying to tame the fire of a global crisis. Because my years dragged slower than yours, I found time to recognize a second and equally concerning climate crisis. When I tell you about it, I know you find my idea worth spreading because you nod and laugh at all the right moments, as do the seven million others listening in even after I’ve finished.</p>

	<p>Do you know who I am, yet?</p>
	<p>No?</p>

	<p>Well then I suggest you sit yourself down and give my greatest speech a listen. It makes for an entertaining watch.</p>

	<p>Done?</p>
	<p>Alright, now answer me this: What did Frank send?</p>

	"""

	question[3] = """

	<p>This is with reference to the job interview you appeared for last week, for  the world’s toughest job. Well, congratulations! You’ve been selected! A slight warning though; this post is severely underrated. Not many appreciate the enormity of your services. However, there is one person who does- your celebrity chaiwala. </p>

	<p>Let me tell you about the job profile. In order to excel here, you will be required to expand your resources. You must learn to read between the lines. </p>

	<p>Once you master these skills, your work may take on a new dimension. You will be led into the harshest of conditions; into unforgiving environments. Don’t be overwhelmed, though. You are not alone. There are many to help you along the way. In fact, you are only the medium. It is they who are the orchestrators of it all, and it’s time they were accorded celebrity status. </p>

	<p>There was another gentleman who very passionately said the same. He finds himself in that rare slice of the Indian population that does not judge our country by its past, but by its potential for innovation. Find him and tell us what instrument sits behind him as he speaks.</p>

	<p>ps: Listen to him carefully enough and he’ll give you the solution to India’s impending energy crisis in a nutshell.</p>

	<p>We realize you may find this question to be a challenge, and we sincerely pray that Thor will guide you in your quest.</p>

	"""

	question[4] = """

	<p>Are you alright down there? You seem to have fallen pretty far down that well. </p>

	<p>It’s pitch black, and all you can hear is a growing sound of flapping. In the sudden swirling, leathery vortex, you find a remarkable clarity of mind. You’ve finally found your way out, and with it, a part-time job. But this work is tiring, and you need an alternative. In between night-shifts, you decide to fascinate the world with your illusion. </p>

	<p>Sitting in the audience today is an Indian entrepreneur looking to name his new company. This hardly seems the place for him to find his answer. But miraculously, he finds inspiration in the last 5 minutes of your spectacular display. </p>

	<p>The name must have been lucky, because the products his company manufactures have taken India by storm. One such appliance has made itself heard in the Indian household far more loudly than others.</p>

	<p>In times of war and guns, a fledgeling Japanese company had experimented along the same lines and failed, but went on to become a multimillion dollar company anyway. Would you be kind enough to tell us the year that saw the launch of this failed product?</p>
	"""

	question[5] = """
	<p>Choosing a stream is a tiring business. With so many suggestions on how to play your cards, and so many ways to fill five slots, stream selection is confusing, to say the least.</p>

	<p>But wait. Let’s put things in perspective. I once knew a man called Dr. Lawyer.</p>
	<p>Now if that isn’t the epitome of confusion, I don’t know what is. Quite a famous character he was. The man playing his part took on the role of a doctor in another on-screen venture. </p>

	<p>A slight philosophical insight at this point, hunters. Don’t ever let yourselves settle for the conventional. Let your minds run with the creepy crawlies!</p>
	<p>Rant over.

	<p>Getting back, said doctor had an evil enemy of unconventional origin. Given that he is evil, it may seem unlikely that he would find such a productive diversion in warming the hearts of millions with sentimental batter. But that is exactly where the situation stands.</p>

	<p>Not too long ago, he reduced us to emotional puddles through his tribute to the 17 year-old who taught the world how to live, by telling us his story; of the battle that was lost, but won.</p>

	<p>Your job is to tell us the name of this boy’s favourite car.</p>
	"""

	question[6] = """

	He was the son of ruthless parents, whose only desire was vengeance. He wasn’t a large boy, but he had been imbued with deadly power. For a long time now, his parents had held a grudge, and he would be the one to go to war with those against whom the grudge was harboured.

	For years he was trained; his skills perfected. For years he lay dormant until one day, the enemy saw him descend upon them like a flash of lightning. In a matter of minutes, they were mere shadows of their former selves.

	A year later, one among his kin sought to test his abilities within the atolls. Some say his display was lost in the depths. But it wasn’t. 

	In fact, we are all too familiar with it. The prickly fruit of his effort houses rather dysfunctional families, whose dark secret hides behind the veil of their ridiculous laughter, their childishness, their daftness and their money-mindedness. 

	The residents here are not quite what we’d expect. In an environment that doesn’t support their existence, they find remarkable ways to breathe easy. The natives, however, are naturally endowed with something that makes the job a cakewalk.

	There’s a man we know, named coincidentally after this ‘natural endowment’. He is perceptive, and appreciative of the arts. Although not quite a singer, he may be called a drama and music connoisseur. 

	Just the other day, he put into our heads an infectious song, that plays itself over and over again. Not only does it make for an entertaining listen, but it also holds a wealth of educational content. You know that song?
	Wonderful!

	Why don’t you sing it for us? 
	And while you’re at it, take a video of yourself in action and share it with us at minet@themis.in!
	"""

	question[7] = """


	"""

	if request.method == "POST":

		if answer[team.level] == request.POST.get("answer", ""):
			team.level += 1
			team.save()
			return redirect('/level')
		else:
			return render_to_response('levels/index.html', {'question': question[team.level], 'level': team.level, 'incorrect': 'animated wobble' }, context_instance = RequestContext(request))
			

		# return render_to_response('teams/members.html', {'question': question[team.level], 'level': team.level }, context_instance = RequestContext(request))


	# return HttpResponse(question[1])
	return render_to_response('levels/index.html', {'question': question[team.level], 'level': team.level }, context_instance = RequestContext(request))