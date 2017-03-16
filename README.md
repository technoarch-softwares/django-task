# django-task
This is test task showing off django, DRF skills

# **Articles** #

This is a test app that renders news list with 10 news articles per page and having endless scroll ability. This test app also contains API endpoint for getting news articles via API.

**Steps to Setup project locally:**

1. Clone the project repository using SSH access and command will be

```
git clone https://github.com/technoarch-softwares/django-task.git
```

2. Now create a virtual environment using the following command:

```
virtualenv --no-site-packages venv
```

3. Activate the virtual Environment using the following command:

```
source /path/to/venv/bin/activate
```

4. Make the project directory as your current directory and run the following command to install the environment specific dependencies

```
pip install -r requirements.txt
```

5. Run the local server using the following:

```
python manage.py runserver
```

6. News articles list should be accssible at http://127.0.0.1:8000/ and API endpoint should be accessible at http://127.0.0.1:8000/api
