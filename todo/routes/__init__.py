from flask import Blueprint


bp = Blueprint('routes', __name__)

from .task import *
from .user import *
