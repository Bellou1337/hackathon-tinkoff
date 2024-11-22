from fastapi.templating import Jinja2Templates
from .config import config

templates = Jinja2Templates(directory="templates")

SECRET = config["Miscellaneous"]["Secret"]