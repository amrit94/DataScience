## 20 Feb Assignment Solution 

### Q1. Explain GET and POST methods.
**GET Request**
GET requests is used to `retrieve resource` representation/information only – and not modify it in any way.As GET requests do not change the resource’s state, these are said to be safe methods.

Additionally, GET APIs should be `idempotent`. Making multiple identical requests must produce the same result every time until another API (POST or PUT) has changed the state of the resource on the server.

**POST Request**
POST request is used to `create new` subordinate resources, e.g., a file is subordinate to a directory containing it or a row is subordinate to a database table.

POST is `neither safe nor idempotent`, and invoking two identical POST requests will result in two different resources containing the same information (except resource ids).

### Q2. Why is request used in Flask?
The Request, in Flask, is an object that contains all the data sent from the Client to Server. This data can be recovered using the GET/POST Methods

### Q3. Why is redirect() used in Flask?
Flask class has a redirect() function. When called, it returns a response object and redirects the user to another target location with specified status code. location parameter is the URL where response should be redirected.

### Q4. What are templates in Flask? Why is the render_template() function used?
Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the Jinja template library to render templates.

render_template is a Flask function from the flask.templating package. render_template is used to generate output from a template file based on the Jinja2 engine that is found in the application's templates folder.

### Q5. Create a simple API. Use Postman to test it. Attach the screenshot of the output in the Jupyter Notebook.

```
from flask import Flask, request ,render_template , jsonify

app = Flask(__name__)

@app.route('/details')
def get_details():
    name = request.args.get('n1')
    print(name)
    result = f'Hi this is {name}'
    return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
```
![](https://ik.imagekit.io/8fh0zzm0gxio/ds-pwskills/as/feb-20-1.png)