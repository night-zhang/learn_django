# learn_django
**本项目主要为了回忆Django的基础用法，参考自Django book 2.0 的中文教程**

python3.7
django3.0

## 20200720创建项目
将django的路径 `C:\Python33\Lib\site-packages\django;`添加到环境变量才可以使用`django-admin.py`

常用命令
```
#创建django命令
django-admin.py startproject project-name

#创建django的app
python manage.py startapp app-name
或 django-admin.py startapp app-name

#同步数据库
python manage.py syncdb
#注意：Django 1.7.1及以上的版本需要用以下命令
python manage.py makemigrations
python manage.py migrate

#命令行调试模式
python manage.py runserver 8001
python manage.py runserver 0.0.0.0:8000

#清除数据库
python manage.py flush

#创建超级管理员
python manage.py createsuperuser
按照提示输入
#修改管理员密码
python manage.py changepassword username（需要修改的用户名）

#导入和导出数据
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json

#进入数据库
python manage.py dbshell
```
## 20200721基础用法
有参数时url的新旧写法
```python
path('time/plus/<int:offset>/', views.hours_ahead),
#在django2之后，可以引入re_path来使用老的写法
re_path('^time/plus/(\d{1,2})/$', views.hours_ahead),
```
## 20200722
models的一些基础API
```python
# Import the models we created from our "news" app
>>> from news.models import Article, Reporter

# No reporters are in the system yet.
>>> Reporter.objects.all()
<QuerySet []>

# Create a new Reporter.
>>> r = Reporter(full_name='John Smith')

# Save the object into the database. You have to call save() explicitly.
>>> r.save()

# Now it has an ID.
>>> r.id
1

# Now the new reporter is in the database.
>>> Reporter.objects.all()
<QuerySet [<Reporter: John Smith>]>

# Fields are represented as attributes on the Python object.
>>> r.full_name
'John Smith'

# Django provides a rich database lookup API.
>>> Reporter.objects.get(id=1)
<Reporter: John Smith>
>>> Reporter.objects.get(full_name__startswith='John')
<Reporter: John Smith>
>>> Reporter.objects.get(full_name__contains='mith')
<Reporter: John Smith>
>>> Reporter.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Reporter matching query does not exist.

# Create an article.
>>> from datetime import date
>>> a = Article(pub_date=date.today(), headline='Django is cool',
...     content='Yeah.', reporter=r)
>>> a.save()

# Now the article is in the database.
>>> Article.objects.all()
<QuerySet [<Article: Django is cool>]>

# Article objects get API access to related Reporter objects.
>>> r = a.reporter
>>> r.full_name
'John Smith'

# And vice versa: Reporter objects get API access to Article objects.
>>> r.article_set.all()
<QuerySet [<Article: Django is cool>]>

# The API follows relationships as far as you need, performing efficient
# JOINs for you behind the scenes.
# This finds all articles by a reporter whose name starts with "John".
>>> Article.objects.filter(reporter__full_name__startswith='John')
<QuerySet [<Article: Django is cool>]>

# Change an object by altering its attributes and calling save().
>>> r.full_name = 'Billy Goat'
>>> r.save()

# Delete an object with delete().
>>> r.delete()
```

## 20200723 模板渲染template的一些写法
- context
    传递参数
- if/else
    {% if %} 标签检查(evaluate)一个变量，如果这个变量为真（即，变量存在，非空，不是布尔值假），系统会显示在 {% if %} 和 {% endif %} 之间的任何内容
- for
    {% for %}{% endfor %} 
- ifequal/ifnotequal
- 注释 {# This is a comment #}
- 过滤器 {{ name|lower }}
- render_to_response
- locals() 返回的字典 对所有局部变量的名称与值进行映射
- include 模板标签
    该标签允许在（模板中）包含其它的模板的内容。 标签的参数是所要包含的模板名称，可以是一个变量，也可以是用单/双引号硬编码的字符串
- 所有的 {% block %} 标签告诉模板引擎，子模板可以重载这些部分
- {% extends "base.html" %}子模版
example：
```
# base.html
<!DOCTYPE HTML PUBLIC "‐//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
<title>{% block title %}{% endblock %}</title>
</head>
<body>
<h1>My helpful timestamp site</h1>
{% block content %}{% endblock %}
{% block footer %}
<hr>
<p>Thanks for visiting my site.</p>
{% endblock %}
</body>
</html>


# 子模版页
{% extends "base.html" %}
{% block title %}The current time{% endblock %}
{% block content %}
<p>It is now {{ current_date }}.</p>
{% endblock %}
```
