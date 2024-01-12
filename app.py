import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse

from controller.app_controller import application
from controller.auth_controller import authentication
from face_auth.constant.application import APP_HOST, APP_PORT

app = FastAPI()

# app has two route Authentication(/auth) and application(/application)
# all route are POST
@app.get("/")
def read_root():
    return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

# contain login and registration route
app.include_router(authentication.router)

# contain login embedding and registration embedding route
app.include_router(application.router)

app.add_middleware(SessionMiddleware, secret_key="!secret")


if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
