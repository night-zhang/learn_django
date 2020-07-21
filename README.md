# learn_django
**本项目主要为了回忆Django的基础用法，参考自django文档的中文教程**
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
