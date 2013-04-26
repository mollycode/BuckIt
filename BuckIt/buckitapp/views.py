# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Tag, Task, User, Ownership

def home(request):
	userId = "Molly Nacey" #we should be able to get user info from login
	user_obj = get_object_or_404(User, name=userId)
	
	if request.method == 'POST':
		print request.POST['task']
		print request.POST['tags']
		# create the new tag and task if they don't exist already
		new_tag = Tag.objects.filter(tag_text = request.POST['tags'])
		if len(new_tag) == 1:
			new_tag = new_tag[0]
		else:
			new_tag = Tag(tag_text = request.POST['tags'])
			new_tag.save()
		
		new_task = Task.objects.filter(task_text = request.POST['task'])
		if len(new_task) == 1:
			pass
		else:
			new_task = Task(task_text = request.POST['task'])
			new_task.save()
			new_task.tags.add(new_tag)
			new_ownership = Ownership(user = user_obj, task = new_task)
			new_ownership.save()


		owns = Ownership.objects.filter(user=user_obj).order_by('-date_set').order_by('completed')
		topTasks = Task.objects.order_by('count')[0:3]
		return render_to_response('home.html',
		                          {'topTasks':topTasks, 'owns':owns},
		                          context_instance = RequestContext(request))

	else:	
		owns = Ownership.objects.filter(user=user_obj).order_by('-date_set').order_by('completed')
		topTasks = Task.objects.order_by('count')[0:3]
		return render_to_response('home.html',
		                          {'topTasks':topTasks, 'owns':owns},
		                          context_instance = RequestContext(request))

def login(request):
	return render_to_response('login.html', context_instance=RequestContext(request))

def profile(request, userid):
	newid = userid.replace('_',' ')

	user_obj = get_object_or_404(User, name=newid)
	owns = Ownership.objects.filter(user=user_obj)

	return render_to_response('profile.html', 
	    {'owns': owns}, 
		context_instance = RequestContext(request))

def search(request):
	if request.method == 'POST':
		tagname = request.POST['tagQuery']
		try:
			tag = Tag.objects.get(tag_text=tagname)
			tasks = Task.objects.filter(tags=tag)
		except Tag.DoesNotExist:
			tasks = None
	else:
		tasks = Task.objects.all()
	return render_to_response('search.html',
		{'tasks': tasks}, context_instance=RequestContext(request))

