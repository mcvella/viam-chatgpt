from viam.resource.registry import Registry, ResourceCreatorRegistration
from chat_service_api import Chat  # type: ignore

from src.chatgpt import viam_chatgpt

Registry.register_resource_creator(
    Chat.API, viam_chatgpt.MODEL, ResourceCreatorRegistration(viam_chatgpt.new, viam_chatgpt.validate_config)
)
