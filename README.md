# The Problem


Design a RESTful web service API call that will return menu items for specific restaurant

# Reasoning

I chose to use Python language and Flask microframework for application itself and PonyORM to work with database.

### Why Flask
Flask is a microframework, 
which while being small is very functional.

Comparing to Django, it does not make you 
follow any architectural pattern, 
so you are free to choose what fits your needs here.

For instance it gives you freedom to use or not to use ORM, 
while with Django choice of not using ORM would look strange.

### Why PonyORM
PonyORM is an ORM of my choice because it  
allows you to make requests in a very similar to SQL way

For instance

```python
from models import orm, Restaurant

with orm.db_session:
    restaurant = orm.select(r for r in Restaurant if r.id == 1).first()
```

It's purely Pythonic and does not make you learn some ORM-specific syntax for quering, 
plus it has a lot of additional features such as permissions for actions on models


# Trade offs

* I would write my own recursive version of serialization.to_dict, so it would be possible to get modifier's modifiers too
* I would create Dockerfiles for database and application and docker-compose.yml for those services
* I would write tests and/or create a small front-end application for tests