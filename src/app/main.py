from app.db import init_db, disconnect_db
from app.db import engine
import uvicorn
from app.config.config import get_settings
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from app.web.


app = FastAPI(title = "Splitwise", description="Splitwise clone in FastAPI", version=1.0.0)

app.include_router()