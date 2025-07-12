from pydantic import BaseModel
from typing import Dict, Any
from datatime import datatime


class ESP32Data(BaseModel):
    data: Dict [str, Any]

