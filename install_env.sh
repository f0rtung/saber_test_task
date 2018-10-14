sudo apt-get install python2.7
sudo apt-get install python-pip
virtualenv --no-site-packages myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd backend_server/log_streamer
python generate_log.py
cd ..
python manage.py migrate
python manage.py runserver
