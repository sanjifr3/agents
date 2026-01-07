import os
from typing import Type

import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class PushNotificationInput(BaseModel):
    """A message to best sent to the user"""

    message: str = Field(..., description="The message to be sent to the user.")


class PushNotificationTool(BaseTool):
    name: str = "Push Notification Tool"
    description: str = (
        "This tool is used to send a push notification to a user with a given message."
    )
    args_schema: Type[BaseModel] = PushNotificationInput

    def _run(self, message: str) -> str:
        url = "https://api.pushover.net/1/messages.json"
        token = os.getenv("PUSHOVER_TOKEN")
        user = os.getenv("PUSHOVER_USER")

        print(f"Push: {message}")
        payload = {"user": user, "token": token, "message": message}
        requests.post(url, data=payload)
        return '{"notification":"ok"}'
