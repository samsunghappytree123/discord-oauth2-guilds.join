import aiohttp, os, asyncio, dotenv, config
from sanic import Sanic, response, request
from sanic.response import json, text, html, redirect
from requests_oauthlib import OAuth2Session

dotenv.load_dotenv(verbose=True)

app = Sanic(__name__)
app.config["SECRET_KEY"] = os.getenv("OAUTH2_CLIENT_SECRET")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

if "http://" in os.getenv("OAUTH2_CLIENT_SECRET"):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"

AUTHORIZATION_BASE_URL = "https://discord.com/api/oauth2/authorize"
TOKEN_URL = "https://discord.com/api/oauth2/token"

def token_updater(token):
    request.cookies["oauth2_token"] = token


def make_session(token=None, state=None, scope=None):
    return OAuth2Session(
        client_id=config.CLIENT_ID,
        token=token,
        state=state,
        scope=scope,
        redirect_uri=config.REDIRECT_URI,
        auto_refresh_kwargs={
            "client_id": config.CLIENT_ID,
            "client_secret": app.config["SECRET_KEY"],
        },
        auto_refresh_url=TOKEN_URL,
        token_updater=token_updater,
    )

@app.route("/login")
async def login(request):
    scope = request.args.get("scope", "identify email guilds guilds.join")
    discordoauth = make_session(scope=scope.split(" "))
    authorization_url, state = discordoauth.authorization_url(AUTHORIZATION_BASE_URL)
    return redirect(authorization_url)

@app.route("/error")
async def error(request):
    return text("어라...? 알 수 없는 오류가 발생했어요.")

@app.route("/callback")
async def callback(request):
    code = request.args.get('code')
    if request.args.get("error"):
        return redirect("/error")
    discordoauth = make_session()
    token = discordoauth.fetch_token(
        TOKEN_URL,
        client_secret=app.config["SECRET_KEY"],
        authorization_response=request.url,
    )
    user = discordoauth.get("https://discord.com/api/users/@me").json()
    url = f"https://discord.com/api/guilds/{config.GUILD_ID}/members/{user['id']}"

    async with aiohttp.ClientSession() as session:
        async with session.put(url, json={'access_token' : token['access_token']}, headers={"Authorization": f"Bot {os.getenv('TOKEN')}", "Content-Type":"application/json"}) as response:
            try:
                data = await response.json()
            except:
                return 

    return text("서버 강제 초대가 성공적으로 이루어졌습니다.")


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
