# This note are for note my understanding of django so the content will be like trivia or something

- urls.py is used for connectiong views.py function with html file
- If in one page there is error, then django will scream, not like javascript
- To make migration:
    > python manage.py makemigrations name-of-target-app
    - This command will make file called 0001_initial.py, then:
    > python manage.py migrate
    - This command will migrate the model to database (db.sqlite3 for sqlite)
- To manipulate data from shell:
    > python manage.py shell
    - This command will start manage.py as shell
    > from app_dir.models import class1,class2
    - This command will import class1 and class2 from models inside app_dir directory
    - ### Following relationships “backward”
        - If a model has a ForeignKey, ***instances of the foreign-key model will have access to a Manager that returns all instances of the first model***. By default, this Manager is named FOO_set, where FOO is the source model name, **lowercased**. This Manager returns QuerySets, which can be filtered and manipulated as described in the “Retrieving objects” section above.
        - Example
        ```python
        b = Blog.objects.get(id=1)
        b.entry_set.all() # Returns all Entry objects related to Blog.
        # b.entry_set is a Manager that returns QuerySets.
        b.entry_set.filter(headline__contains='Lennon')
        b.entry_set.count()
        ```
        or
        ```python
        q = Quest.objects.get(pk=1)#Get object in primary key
        q.choice_set.create(choice="Django",votes=0)
        q.choice_set.create(choice="Flask",votes=0)
        q.choice_set.create(choice="Web2py",votes=0)
        q.choice_set.all()# Will return all the choice that has been created
        ```
- To make admin account in django
> In virtual environment
```cmd
    python manage.py createsuperuser
```
