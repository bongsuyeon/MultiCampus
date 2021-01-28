from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.template import loader


def exercise1(request):
 template = loader.get_template('exercise1.html')
 if request.method == 'GET':
   msg ="get함"
 else:
  msg="post함"
 context={'result': msg}
 logging.warning(msg+"나는로깅")
 return HttpResponse(template.render(context, request))

def exercise2(request):
 if request.method == 'POST':
  Writer = request.POST['name']
  opinion = request.POST['opinion']
  context = {'name': Writer, 'opinion': opinion}
 else:
  context = None
 return render(request, 'exercise2.html', context)


def product1(request):
 return render(request, 'product1.html')


def basket1(request):
  print(request.GET.get('pid'))
  pid = request.GET.get('pid')
  context = {
   'pid': pid
  }
  return render(request, 'basket1.html', context)