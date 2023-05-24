from .logging import AbstractLogger

from todoist_api_python.api_async import TodoistAPIAsync

class TodoistSDK:
    def __init__(self, api_token:str, logger:AbstractLogger):
        self._api = TodoistAPIAsync(api_token)
            
    async def get_tasks(self):
        try:
            tasks = await self._api.get_tasks()
            return tasks
        except Exception as error:
            print(error)