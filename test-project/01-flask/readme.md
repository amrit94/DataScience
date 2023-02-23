## Flask Calculator

### Render HTML
* `render_template('results.html' , result = result)`
* All HTML files goes inside `templates folder`

### Load static files
* `href="{{ url_for('static', filename='css/style.css') }}`
* ``


### Run App
* `python app.py`
* Test API using Postman
```
# Request
http://127.0.0.1:5000/postman_action
# body > raw > json
{ "operation": "add", "num1": 1, "num2": 2 }

# Response
"The sum of 1and 2is 3"
```