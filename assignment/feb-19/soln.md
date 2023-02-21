
## 19 Feb Assignment Solution 
### Q1. What is Flask Framework? What are the advantages of Flask Framework?
Flask is a popular Python `web framework`, meaning it is a third-party Python library used for developing `web applications`.

Flask is a `lightweight WSGI` web application framework. It is designed to make getting started `quick and easy` with the ability to `scale up` to complex applications.


### Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")
```
![](https://ik.imagekit.io/8fh0zzm0gxio/ds-pwskills/as/feb-19-1.png)

### Q3. What is App routing in Flask? Why do we use app routes?
App Routing means `mapping the URLs to a specific function` that will handle the logic for that URL. Modern web frameworks use more meaningful URLs to help users remember the URLs and make navigation simpler. 

On the top of the function we want to map, wll add `@app.route("</path>")`. In above example `/`(root) is mapped to hello_word function.


### Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/” route to show the following details:Company Name: ABC Corporation Location: India Contact Detail: 999-999-9999 Attach the screenshot of the output in Jupyter Notebook.

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def company():
    data = '''<p>Name: ABC Corporation <br>
    Location: India <br>
    Contact Detail: 999-999-9999<p>
    '''
    return data


@app.route('/welcome')
def welcome():
    return "Welcome to ABC Corporation"

if __name__=="__main__":
    app.run(host="0.0.0.0")
```
* `/welcome`
![](https://ik.imagekit.io/8fh0zzm0gxio/ds-pwskills/as/feb-19-2.png)
* `/`
![](https://ik.imagekit.io/8fh0zzm0gxio/ds-pwskills/as/feb-19-3.png)

### Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.

The url_for() function is used to build a URL to the specific function dynamically. The first argument is the name of the specified function, and then we can pass any number of keyword argument corresponding to the variable part of the URL.

* In below example using url_for() to redirect `/home` to `/`
```
from flask import *

app = Flask(__name__)

@app.route("/")
def company():
    data = '''
    <a href="{{ url_for('welcome') }}"> Welcome Page </a>
    <p>Name: ABC Corporation <br>
    Location: India <br>
    Contact Detail: 999-999-9999<br><p>
    '''
    return data


@app.route('/home')
def home():
    return redirect(url_for('company')) 

if __name__=="__main__":
    app.run(host="0.0.0.0")
```