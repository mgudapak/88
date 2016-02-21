Mostly notes for me to remember things about Flask templates, the Jinja2 templating language it uses and other things concerning how to organize templates in this directory ..

- Structure of the templates directory parallels the structure of our routes. For e.g. the template for the route myapp.com/admin/analytics would be in templates/admin/analytics.html

- Stick with the default JINJA2 templating language! Docs are here http://jinja.pocoo.org/

- There are two kinds of delimiters in Jinja2
    {% ... %} is used to execute statements such as for-loops or assign values

    {{ ... }} is used to print the result of an expression to the template.

- The parent template usually defines a generalized structure that all of the child templates will work within. In our example,
    "layout.html" is the parent template and
    all the other .html files are child templates

