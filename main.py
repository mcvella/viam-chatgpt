import asyncio

from viam.module.module import Module
from chat_service_api import Chat  # type: ignore

from src import viam_chatgpt


async def main():
    module = Module.from_args()
    module.add_model_from_registry(Chat.API, viam_chatgpt.MODEL)
    await module.start()


asyncio.run(main())
