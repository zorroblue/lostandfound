from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import *
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.

#view all notices
def view_all_notices(request):
	if request.method == 'GET':
		notices = Notice.objects.all()
		return JsonResponse(json.loads(serializers.serialize('json',notices)),safe = False)

#make a new notice
@csrf_exempt
def create_notice(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		description = request.POST.get('description')
		user_id = request.POST.get('userid')
		image_url = request.POST.get('url')
		
		if image_url==None:
			image_url = "http://placehold.it/350x150"
		notice = Notice(title = title, description = description, user_id = user_id,image_url = image_url )
		notice.save()
		return JsonResponse({'status' : 'success'})

#delete notice
@csrf_exempt
def delete_notice(request):
	if request.method == 'POST':
		notice_id = request.POST.get('noticeid')
		user_id = request.POST.get('userid')
		
		try:
			notice = Notice.objects.get(notice_id = notice_id)
		except:
			notice = None
			return JsonResponse({'status':'failure','reason':'No such Notice'})

		if notice != None:
			notice.delete()
		return JsonResponse({'status' : 'success'})

#update details
#compulsory params : noticeid, userid
#give params for the ones to be updated
@csrf_exempt
def update_notice(request):
	notice_id = request.POST.get('noticeid')
	title = request.POST.get('title')
	description = request.POST.get('description')
	user_id = request.POST.get('userid')
	image_url = request.POST.get('url')
	try:
		notice = Notice.objects.get(notice_id = notice_id)
	except:
		notice = None
		return JsonResponse({'status':'failure','reason':'No such Notice'})

	if notice!=None:
		if title == None:
			title = notice.title
		if description == None:
			description = notice.description
		if image_url == None:
			image_url = notice.image_url
		Notice.objects.filter(notice_id__exact = notice_id).update(title=title, description = description, image_url=image_url,user_id = user_id)
		return JsonResponse({'status': 'success'})	