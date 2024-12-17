from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import init_db, get_recipes_by_purpose
import uvicorn

app = FastAPI()

# 정적 파일과 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 데이터베이스 초기화
init_db()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/recipes/{purpose}")
async def get_recipes(request: Request, purpose: str):
    recipes = get_recipes_by_purpose(purpose)
    return templates.TemplateResponse("recipes.html", {
        "request": request,
        "recipes": recipes,
        "purpose": purpose
    })

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 