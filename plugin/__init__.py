import uuid
from flowlauncher import FlowLauncher
import pyperclip
from .type import QueryResult


class UuidPlugin(FlowLauncher):
    def query(self, query):
        result = str(uuid.uuid4())
        return [
            QueryResult(
                Title=result,
                SubTitle="Copy this uuid4 to clipboard",
                IcoPath="images/uuid.png",
                JsonRPCAction={
                    "method": "copy",
                    "parameters": [result],
                },
            ).asdict(),
        ]

    def context_menu(self, data):
        return []

    def copy(self, data):
        pyperclip.copy(data)
