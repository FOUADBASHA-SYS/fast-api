from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

# Set up templates directory
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

router = APIRouter(tags=["Frontend Pages"])


@router.get("/", response_class=HTMLResponse, summary="Home Page View")
def home_page(request: Request):
    """Serve the modern Home Page."""
    return templates.TemplateResponse(request=request, name="index.html")


@router.get("/login", response_class=HTMLResponse, summary="Login Page View")
def login_page(request: Request):
    """Serve the Login Page."""
    return templates.TemplateResponse(request=request, name="login.html")


@router.get("/register", response_class=HTMLResponse, summary="Registration Page View")
def register_page(request: Request):
    """Serve the Registration Page."""
    return templates.TemplateResponse(request=request, name="register.html")
