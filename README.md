## Task and Project Manager Backend
iClassroom Task and Project Management is a simple and effective tool for organising and completing assigned tasks with the best project management tool Kanban Board. Complete your tasks on time, get notified about the deadlines and pending works. Interact with your personalized AI assistant to get through the difficult or bigger projects and get them simplified and divided into small modules thereby managing your time efficiently.
## Setup development environment ##

Install dependencies
sudo apt-get install -y build-essential binutils-doc autoconf flex bison libjpeg-dev
sudo apt-get install -y libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev
sudo apt-get install -y automake libtool libffi-dev libssl-dev curl git tmux gettext

Setup Database

Install postgresql

sudo apt-get install -y postgresql postgresql-contrib
sudo apt-get install -y postgresql-doc postgresql-server-dev-all

Setup initial User, database and permissions

sudo -u postgres psql -c "CREATE ROLE name LOGIN PASSWORD ' ';"
sudo -u postgres createdb name -O name --encoding='utf-8' --locale=en_US.utf8 --template=template0
echo 'local all name peer' | sudo -u postgres tee -a $(sudo -u postgres psql -t -P format=unaligned -c 'show hba_file') > /dev/null
sudo service postgresql reload

Create your own environment with a settings/local.py file and overwrite the settings/common.py.
For a basic configuration that works simply copy this settings/local.py to settings/local.py( remember to edit your postgresql password).


Execute these commands in your virtualenv(wrapper):

```
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py sample_data
```

**IMPORTANT: Runs with python 3.5+**


