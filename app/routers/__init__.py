from app.routers.auth import router as auth_router
from app.routers.home import router as home_router
from app.routers.pages import router as pages_router

__all__ = ["auth_router", "home_router", "pages_router"]
