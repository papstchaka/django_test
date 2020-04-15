# django_test
Short Implementation that shows how django can be used as framework to host webistes that are created with basic HTML + CSS.

<h2 align="center">
  <img src=https://github.com/papstchaka/django_test/blob/master/django_test/static/assets/index.jpg alt="Home View" width="800px" />
</h2>

## Requirements
* django
* plotly (for the graphs section)
--> install via `pip install django plotly`

## Fork project and set it up to work on local laptop
* Fork/Clone the repository to your local machine into a folder like `django_test`, go to that folder and run `python manage.py runserver 2222`. 2222 is the projects default backend port. Of course you can change that if you want
* head to `localhost:<desired_port>` to see the frontend

## Functionality

App provides some different things that are already implemented:
* Search Option to navigate through all subsites
* a subsite that shows a <a href="https://plotly.com/python/" target="_blank">plotly generated Graph</a>
* a subsite that shows given image and a <a href="https://dash.plotly.com/dash-html-components" target="_blank">dash_html_component</a> that was successfully transformed to HTML code, if possible.
* Error-Site if desired subsite does not exist

* Layout is almost similar to the `python`-version in my <a href="https://github.com/papstchaka/dash_test" target="_blank">dash_test</a> repo. Instead of using dash with python, this layout is implemented using HTML, CSS and JavaScript.

--> for further information please visit `views.py` in `django_test`-folder. You can see there how to implement and view all those stuff.

<h2 align="center">
  <img src=https://github.com/papstchaka/django_test/blob/master/django_test/static/assets/subsite.jpg alt="Subsite View" width="800px" />
</h2>

<h2 align="center">
  <img src=https://github.com/papstchaka/django_test/blob/master/django_test/static/assets/not_found.jpg alt="Not Found View" width="800px" />
</h2>

<h2 align="center">
  <img src=https://github.com/papstchaka/django_test/blob/master/django_test/static/assets/picture.jpg alt="Picture View" width="800px" />
</h2>

<h2 align="center">
  <img src=https://github.com/papstchaka/django_test/blob/master/django_test/static/assets/graph.jpg alt="Graph View" width="800px" />
</h2>
