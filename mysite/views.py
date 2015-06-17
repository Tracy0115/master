from django.http import Http404,HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello World")
	
def stone(request):
    return HttpResponse("HeartStone")
	
def Current_Time(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
	
def hours_ahead(request,offset):
	try:
	 	offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	dic = {'next_time':dt,'hour_offset':offset}
	return render_to_response('future datetime.html',dic)

def Current_DateTime(request):
	now = datetime.datetime.now()
	t = get_template('current.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)
	
def Current_DateTime1(request):
	now = datetime.datetime.now()
	return render_to_response('current datetime.html',{'current_date':now})