from django.db import models
from django.shortcuts import render, redirect
from .models import Text, Search, Graph, Picture, Div, Dash
from . import urls 
from django.contrib.auth.decorators import user_passes_test

import dash_html_components as html
import dash_core_components as dcc

# Create your views here.
def home(request): ##index website
    all_urls = list(set([pattern.name for pattern in urls.urlpatterns]))
    given_elements = ["graph", "picture", "subsite"] ##for the dropdown

    if request.GET.get('Search-Content') != None:
        query = request.GET.get('Search-Content')
        found,result=Search.search(query,all_urls)
        if found:
            return redirect("/"+query+"/")
        else:
            return render(request, 'raw.html', {"title": "404", "html_file": "not_found.html", "btn": ["",""]})

    title = "Home"
    html_file = "home.html"
    btn = ["-active",""]
    return render(request, 'raw.html', {"title": title, "html_file": html_file, "btn": btn, "given_elements" : given_elements})

@user_passes_test(lambda u: u.is_superuser) ##checks permission to visit the subsite
def subsite(request,pk=""): ##boring empty subsite
    all_urls = list(set([pattern.name for pattern in urls.urlpatterns]))
    subsite_add = pk ##end part of subsite url --> will be shown on site

    if request.GET.get('Search-Content') != None:
        query = request.GET.get('Search-Content')
        found,result=Search.search(query,all_urls)
        if found:
            return redirect("/"+query+"/")
        else:
            return render(request, 'raw.html', {"title": "404", "html_file": "not_found.html", "btn": ["",""]})

    title = "Subsite"
    html_file = "subsite.html"
    btn = ["","-active"]
    return render(request, 'raw.html', {"title": title, "html_file": html_file, "btn": btn, "subsite_add" : subsite_add})

@user_passes_test(lambda u: u.is_superuser) ##checks permission to visit the subsite
def graph(request,pk=""): ##shows a graph which was made with plotly
    all_urls = list(set([pattern.name for pattern in urls.urlpatterns]))
    
    graph_content = Graph.get_graph() ##see models.py to see further implementation

    if request.GET.get('Search-Content') != None:
        query = request.GET.get('Search-Content')
        found,result=Search.search(query,all_urls)
        if found:
            return redirect("/"+query+"/")
        else:
            return render(request, 'raw.html', {"title": "404", "html_file": "not_found.html", "btn": ["",""]})
    
    title = "Graph"
    html_file = "graph.html"
    btn = ["",""]
    return render(request, 'raw.html', {"title": title, "html_file": html_file, "btn": btn, "graph_content" : graph_content})

@user_passes_test(lambda u: u.is_superuser) ##checks permission to visit the subsite
def picture(request,pk=""): ##shows an given image / a dropdown and a converted dash_html_component object
    all_urls = list(set([pattern.name for pattern in urls.urlpatterns]))
    
    content = Picture.get_picture("world_by_night.jpg") ##load picture

    if request.GET.get('Search-Content') != None:
        query = request.GET.get('Search-Content')
        found,result=Search.search(query,all_urls)
        if found:
            return redirect("/"+query+"/")
        else:
            return render(request, 'raw.html', {"title": "404", "html_file": "not_found.html", "btn": ["",""]})

    given_elements = ["1","2","3"]
    if request.GET.get("Test_Dropdown") != None:
        res = request.GET.get("Test_Dropdown")

    div_test = Div.get_html_output() ##see models.py for further implementation / returns empyt div
    div_test = Dash.transform_to_html(html.P('App converts dash_html_components Paragraph into HTML')) ##see models.py for further implementation
    # div_test = Dash.transform_to_html(dcc.Markdown("this is a test", className="dropdown", style={"background-color : #000000"}))
    # print(div_test)

    title = "Picture"
    html_file = "picture.html"
    btn = ["",""]
    return render(request, 'raw.html', {"title": title, "html_file": html_file, "btn": btn, "content" : content, "given_elements" : given_elements, "div_test" : div_test})