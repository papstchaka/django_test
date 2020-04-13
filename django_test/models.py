from django.db import models
from django.views.generic.base import TemplateView
import plotly.offline as py
import plotly.graph_objs as go

# Create your models here.

class Text(models.Model):

    def show_text(text):
        return str(text)

class Search(models.Model):

    def search(query, suburls):
        if query in suburls:
            return True, query
        return False,"not found"

class Graph(TemplateView):

    def get_graph():
        x = [-2,0,4,6,7]
        y = [q**2-q+3 for q in x]

        data = [go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},mode="lines",  name='1st Trace')]
        layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
        figure=go.Figure(data=data,layout=layout)
        div = py.plot(figure, auto_open=False, output_type='div')
        return div

class Picture(models.Model):

    def get_picture(path=""):
        if path != "":   
            return path

class Div(models.Model):

    def get_html_output():
        return  '''
                    <div class="row bg-white has-shadow justify-content-center row-title">
                        <div class="col-auto">
                            <h2 class="sub-header" style="text-align: center;">This is a test!</h2>
                        </div>
                    </div>
                '''

class Dash(models.Model):

    def transform_to_html(dash_object):
        dash_json = dash_object.to_plotly_json()

        if dash_json["namespace"] == "dash_html_components":
            html_type = dash_json["type"].lower()
            props = dash_json["props"]
            children = props["children"] if props["children"] != None else ""
            
            try:
                className = 'class="{}"'.format(props["className"])
            except:
                className = ''
            try:
                style = 'style="'
                style_props = props["style"].items()
                for style_type, style_value in style_props:
                    style += '{}: {}; '.format(style_type,style_value)
                style += '"'.strip()
            except:
                style = ''

            html_object = '<{} {} {}>{}</{}>'.format(html_type,className,style,children,html_type)
        
        else:
            html_object = '<h2 class="sub-header" style="text-align: center;">Object is no embedded HTML object and could not be transformed!</h2>'

        return  '''
                    <div class="row bg-white has-shadow justify-content-center row-title">
                        <div class="col-auto">
                            {}
                        </div>
                    </div>
                '''.format(html_object)