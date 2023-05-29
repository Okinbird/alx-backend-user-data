#   0x01. Basic authentication


# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)


##  0. Simple-basic-API

Download and start your project from this [archive.zip](https://intranet.alxswe.com/rltoken/2o4gAozNufil_KjoxKI5bA)

In this archive, you will find a simple API with one model: `User`. Storage of these users is done via a serialization/deserialization in files.

**Setup and start server**

```
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
```

**Use the API (in another tab or in your browser)**

```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.7.5
< Date: Mon, 18 May 2020 20:29:21 GMT
< 
{"status":"OK"}
* Closing connection 0
bob@dylan:~$
```
