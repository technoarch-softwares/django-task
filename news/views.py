import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import render_to_string
from news.models import News


def home(request):
    all_news = News.objects.all()
    if len(all_news) > 10:
        all_news = all_news[:10]
        more = True
    else:
        more = False             

    return render_to_response("news/homepage.html", {
      	'start': 10,
      	'more': more,
        'all_news': all_news                     
    }, context_instance=RequestContext(request))


def load_more_news(request):
    start = int(request.GET.get('start'))
    all_news = News.objects.all()

    if len(all_news) > start+10:
        all_news = all_news[start:start+10]
        more = True
    else:
        all_news = all_news[start:]
        more = False

    context = {"all_news": all_news}
    data = render_to_string("news/load_more_news.html", context ,context_instance=RequestContext(request))

    response = {"start": start+10, "more": more, "data": data}
    return HttpResponse(json.dumps(response), content_type="applicaton/json")