from django.shortcuts import render, redirect
#from django.views import generic
#from django.views.generic.edit import CreateView,DeleteView
from bs4 import BeautifulSoup
import urllib2
from search.models import Names,Character
from forms import PostForm
#from urlparse import urlparse
#import html5lib
#import urlparse
#import re


def detail(request):

            data = Names.objects.all()
            for d in data:
                urlss = d.link
                #urls = urlss.geturl()
                url = urllib2.urlopen(urlss)
                #readurl = urlss
                soup = BeautifulSoup(url)
                links = soup.find_all('a')
                for lin in links:
                    result = lin.get('href')
                    a = Character(namelink = result)
                    a.save()

            post = Character.objects.all()



            return render(request, 'search/detail.html', {'post': post, 'urls': urlss})

def home(request):
    Names.objects.all().delete()
    Character.objects.all().delete()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail')
    else:
        form = PostForm()
    return render(request, 'search/homepage.html', {'form': form})