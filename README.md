## Task and Project Manager Backend
iClassroom Task and Project Management is a simple and effective tool for organising and completing assigned tasks with the best project management tool Kanban Board. Complete your tasks on time, get notified about the deadlines and pending works. Interact with your personalized AI assistant to get through the difficult or bigger projects and get them simplified and divided into small modules thereby managing your time efficiently.
## Setup development environment ##

Just execute these commands in your virtualenv(wrapper):

```
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py sample_data
```

**IMPORTANT: Runs with python 3.5+**

http://taigaio.github.io/taiga-doc/dist/setup-development.html

