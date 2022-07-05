# short-sns-server
## 환경 구성
### 초기 환경 구성 (1회성)
```commandline 
$ cd <프로젝트 디렉토리>

# 1. 가상환경 생성 
$ python3 -m venv .venv

# 2. ls로 가상환경(venv) 생성되었는지 확인
$ ls
.venv

# 3. 가상환경 활성화
$ source .venv/bin/activate

# 4. 패키지 관리(requirements.txt 활용)
$ pip3 install -r requirements.txt
```

### 가상환경 활성화 / 비활성화
```commandline
# 가상환경 활성화
$ source .venv/bin/activate

# 가상환경 비활성화
$ deactivate
```

## HOW TO RUN
### 1.
```commandline
uvicorn main:app --port {PORT} --reload
```

### 2.
```commandline
sh ./run.sh
```

### 3.
각자 터미널에서 알아서 main 함수 실행

## 프로젝트 구조
```commandline
.
├── README.md
├── main.py
└── src
    └── app
        ├── routers
        └── utils
```