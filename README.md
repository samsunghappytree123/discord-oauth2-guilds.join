# discord-oauth-guilds.join
Discord Oauth2의 "Guilds.join" Scope를 활용한 코드입니다.

## 사용법
1. 이 코드를 clone(`git clone https://github.com/samsunghappytree123/discord-oauth2-guilds.join`) 또는 fork 등으로 다운로드합니다. 
2. cmd에 ``pip install -r "requirements.txt"``를 사용해 필수적으로 설치해야 하는 의존성 모듈을 설치합니다.
3. [``.env.example``](.env.example) 파일을 참고하여 ``.env`` 파일을, [``config.py.example``](config.py.example)을 참고하여 ``config.py``를 만들어주세요. (상세한 예시는 [여기](#envexample과-configpyexample-내용-설명)를 확인해주세요.)
4. ``python app.py``를 사용하여 [``app.py``](app.py)를 실행해주세요.
5. ``${config.py HOST}/login``에 접속하여 인증을 테스트를 하세요.

---

## .env.example과 config.py.example 내용 설명

### .env.example
```py
TOKEN=YOUR_TOKEN # 봇의 토큰을 입력해주세요.
OAUTH2_CLIENT_SECRET=YOUR_SECRET_KEY # 봇의 CLIENT_SECRET_KEY를 입력해주세요.
```

### config.py.example
```py
GUILD_ID = 1234567890 # 강제 초대할 서버의 ID를 입력하세요.
CLIENT_ID = 1234567890 # APPLICATION ID (BOT ID)를 입력해주세요.
REDIRECT_URI = 'http://localhost:5000/callback' # OAUTH 로그인 후 이동할 웹사이트의 주소를 입력하세요.
                                                # APPLICATION OAUTH 탭에서 REDIRECT URL을 http://[아이피]/callback으로 지정하세요!

# -- Sanic 호스트 설정 -- #
HOST = '127.0.0.1' # 127.0.0.1과 같이 수정해주세요.
PORT = 5000 # 포트를 지정해주세요.
```
