Hireio dev proceure
================

### How to work on a new task

* Checkout and pull the latest master
* Create a new branch locally
* Finish your development and commit all the changes
* Do a thorough test! This step is very important as we have no test for now! We rely on you to provide reliable code!
* Push your development branch onto Github and Yinfei will make sure it gets reviewed (ping Yinfei once it's available on Github). Hopefully, once more people know our code style, we'll have more reviewers.
* Address all the comments and reply to each of them with your thoughts or a commit. Note that you don't have to make the change according to what I said. But you'll need to throw me with the ideas you have and why you do it that way. This step can be tedious but it's a great learning experience!!
* Now you can merge it onto master and check off the task on Asana!

## Setup

### Ubuntu

1. make sure Django is installed

```bash
python -c "import django; print(django.get_version())"
```

2. make sure `easy_insall` and `pip` installed

3. install MySQL_python

```bash
sudo apt-get install libmysqlclient-dev
pip install mysql-python
```

4. Create username and password based on hireio settings in MySQL

[reference](https://dev.mysql.com/doc/refman/5.1/en/adding-users.html)

5. run Django migrate

```bash
python manage.py migrate
```

##decode log

1. static/js/jobs/dashboard.js
ajax url changed. 
Problem: the 127.0.0.1 or localhost must be the same as URL in Broswer.
Solution: deleted `http://127.0.0.1:8000`, kept `/jobs/load_more_companies`
