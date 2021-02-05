### django + bootstrap

합치는 방법

>  프롤로그:
>
> * 만들어진 가상환경(python_venv)에서 cmd로 djangovenv\Scripts (cd djangovenv\Scripts) 로 가서 `activate`하면 (djangovenv)가 실행된다.
>
> + file에서 setting에 들어간 후 프로젝트 인터프리터를 가상환경으로 선택한다.



1. pycham 터미널에 django-admin startproject `ProjectName`을 쓴다.
2. 1. cd ProjectName으로 이동한다
   2. file에서 하위 폴더로 재오픈한다.
3. python manage.py runserver를 한 후, Chrome에 localhost:8000을 입력하면 된 것을 확인 할 수 있다.
4. 다시 pycham 터미널로 들어와서 python manage.py startapp `appName`을 입력하면 장고앱이 생성된다.
5. 
   