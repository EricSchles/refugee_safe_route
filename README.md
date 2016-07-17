[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg?maxAge=2592000)](https://gitter.im/EricSchles/refugee_safe_route)

# refugee_safe_route

The goal of this project is to make google maps for refugees where red means unsafe and green means safe.  Rather than being a reference to speed of travel, it is a reference to safety of travel.


##Creating our database

For this project we will be creating a postgres database!  How to set up postgres:

```
createuser -P -s -e -d hackathon_user
#password is 1234
createdb refugee_safe_route -U hackathon_user
#making sure the user and database 

map_app : username$ python init_db.py

map_app : username$ python manage.py db init
map_app : username$ python manage.py db migrate
map_app : username$ python manage.py db upgrade
```



