first clone the reposirory using below command

git clone https://github.com/lpaul95621p/machinetest.git
then open machinetest folder
then healthcare folder
then open command terminal in this folder
first create a virtual env for run below command
python -m venv patients
then activate virtual envirments
using the commands below one by one
1.cd patients
2.cd Scripts
3.actiavte
then install python django using below commmand
pip install django
then run this command
cd patients
then run this command
pip install psycopg2
then create database healthcare in pgadmin
then run this command
python manage.py makemigrations
then run this command
python manage.py migrate
then run this command
python manage.py runserver
for testing open postman
put this url in post http://127.0.0.1:8000/api/v1/patient-intake/
then input your sample data and check it is creating

put this url in get http://127.0.0.1:8000/api/v1/patient-intake/
then chack data is comming with ssn masked
for ssn masked i hve used
this mecahnism available in python 
 item["value"] = "***-**-" + ssn[-4:]
then alos checked ssn is valid serializer using re
this method
re.match(r"^\d{3}-\d{2}-\d{4}$", ssn):

 then run same post method using same data with different id and date of bith less than 18 then it will show Patient must be at least 18 years old
 for checking date of birth
 i have used date function to check 18 years or less than 18




