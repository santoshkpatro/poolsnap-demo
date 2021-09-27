# How to Setup

### Step 1 - Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### Step 2 - Install all the dependencies

```
pip3 install -r requirements.txt
npm install
```

### Step 3 - Migrate the changes to database

```
python3 manage.py migrate
```

### Step 4 - Create a superuser/admin for accessing admin panel

```
python3 manage.py createsuperuser
```

Please enter information as per instruction

### Step 5 - Now let's start the server

```
python3 manage.py runserver
```

### Step 6 - Create a .env.local file in the root 
```
VUE_APP_API=HTTP://127.0.0.1:8000
```

### Step 7 - Start frontend server

```
npm run serve
```

### Step 8 - Now visit localhost:8080 [Click Here](http://localhost:8080/admin)

2. For admin panel [Click Here](http://localhost:8000/admin)
1. For backend [Click Here](http://localhost:8000)
