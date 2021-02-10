## django 프롤로그

- c:\xxx\python_venv 라는 폴더를 생성한다.

- c:\xxx\python_venv 폴더로 옮겨서 다음 명령을 입력하고 실행시켜 가상 환경, djangovenv 를 생성한다.

```shell
cd \xxx\python_venv

python -m venv djangovenv

cd djangovenv\Scripts

activate
```

위와 같이 cmd창에서 실행한다.

그러면 앞에 (djangovenv)가 뜨면서 창이 clear된다.

```shell
pip install django

python -m pip install --upgrade pip
```

그리고 위와 같이 실행하면 **가상환경 만들기과 가상환경 안에 장고 개발 환경 설치하기** 끝 (●'◡'●)(●'◡'●)