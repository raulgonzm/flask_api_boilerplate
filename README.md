# Flask API Boilerplate

## Requirements
- Python 3.4+
- Flask 0.12+
- Flask-RESTful 0.3.5+

## Environment Installation

```
vagrant up
vagrant ssh
workon flask_api
```

## Run Server
Now you can go in project root (/vagrant/flask_api) and run server:

```
python server.py 
```

This should give you something like this:

```
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 126-723-095 
```

## Test API
Now you open your web-browser at:

```
http://127.0.0.1:8000/conferences/
```