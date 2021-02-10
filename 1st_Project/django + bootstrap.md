

### django + bootstrap

합치는 방법

>  프롤로그:
>
> * 만들어진 가상환경(python_venv)에서 cmd로 djangovenv\Scripts (cd djangovenv\Scripts) 로 가서 `activate`하면 (djangovenv)가 실행된다.
>
> + file에서 setting에 들어간 후 프로젝트 인터프리터를 가상환경으로 선택한다.



1. pycham 터미널에 django-admin startproject `ProjectName`을 쓴다. 

   ```shell
   django-admin startproject ProjectName
   ```

   

2. 1. cd ProjectName으로 이동한다.

   2. file에서 하위 폴더로 재오픈한다.

      ![image-20210210234157560](C:\Users\ajgkw\AppData\Roaming\Typora\typora-user-images\image-20210210234157560.png)

      ✔ 터미널 창에 다음과 같이 뜨면 성공

3. python manage.py runserver를 한 후, Chrome에 localhost:8000을 입력하면 된 것을 확인 할 수 있다.

   ![image-20210210234345823](C:\Users\ajgkw\AppData\Roaming\Typora\typora-user-images\image-20210210234345823.png)

4. 다시 pycham 터미널로 들어와서 python manage.py startapp `appName`을 입력하면 장고앱이 생성된다.

5. `appName`파일에 이제 static 디렉토리와 templates 디렉토리를 생성한다.

6. static 디렉토리 안에는 css, img, js 등으 파일을 담고, templates에 `appName`디렉토리를 생성후 .html파일들을 넣어준다

   * EVproject/EVapp/static/css
   * EVproject/EVapp/templates/EVapp/index.html

   ![image-20210210233528063](C:\Users\ajgkw\AppData\Roaming\Typora\typora-user-images\image-20210210233528063.png)

7. 페이지 실행을 해보기 위해 

   📁EVapp/urls.py

   ```python
   from django.urls import path
   from . import views
   urlpatterns = [
    path('', views.index, name='index'),
   ]
   ```

   

   📁EVapp/views.py

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   from django.template import loader
   
   def index(request):
    return render(request, 'EVapp/index.html', None)
   ```

   혹은 (위아래 다 같은 실행을 한다.)

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   from django.template import loader
   
   def index(request):
    template = loader.get_template('EVapp/index.html')
    return HttpResponse(template.render(None, request))
   ```

   

   📁EVproject/urls.py

   ```
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('EVapp/', include('EVapp.urls')),
   ]
   ```

   

   📁EVproject/setting.py

   ```python
   INSTALLED_APPS = [
       'EVapp',
       ..........
   ]
   ```

   [Line 33] APP이름을 등록해준다.

   그리고 107-109줄도 아래와 같이 바꿔준다.

   ```python
   LANGUAGE_CODE = 'ko-kr'
   
   TIME_ZONE = 'Asia/Seoul'
   ```

   🙋‍♀️템플릿 변수들을 만들어 주기위해 📁EVproject/setting.py에 아래 내용을 추가해준다.

   ```python
   import os
   
   STATICFILES_DIRS = (
       os.path.join(BASE_DIR,'static'),
   )
   ```

8. 이제 html에 들어가면 아마도 템플릿이 없다는 오류가 뜰텐데..

   📁EVapp/templates/EVapp/index.html

   ```python
   {% load static %}
   ```

    line 맨 위쯤에 해당 템플릿변수를 선언해주고,

   템플릿에서 쓰인 css, img, js 코드들을 템플릿 변수로 바뀌준다.

   ex) 

   ```python
   <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
   <link rel="stylesheet" href='{% static "css/bootstrap.min.css" %}'>
   <section class="hero spad set-bg" data-setbg="{% static 'img/hero-bg.jpg' %}">
   ```

   페이지 이동이 있는 경우,  아래와 같이 바꿔주면 된다.

   ```python
   <a href="{% url 'index' %}">
   ```

9. 그리구 실행을 해보면 잘 연결이 되어있을 것이다 (●'◡'●)(●'◡'●)