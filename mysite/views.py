from django.http import Http404,HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import test
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from mysite.forms import ContactForm

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

def Current_url_path(request):
	return HttpResponse("Welocom to the page at %s" % request.path)
	
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('Enter a search form.')
        elif len(q) > 20:
            error.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'error': error})
		
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
			initial={'subject': 'I love your site!'}
			)
    return render_to_response('contact_form.html', {'form': form})