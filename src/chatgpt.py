import asyncio
from collections.abc import Mapping, Sequence
import os
from typing import ClassVar
from typing_extensions import Self
from urllib.request import urlretrieve
from typing import Any, List, Mapping, Optional

from viam.logging import getLogger
from viam.module.module import Reconfigurable
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.proto.app.robot import ComponentConfig
from viam.resource.types import Model, ModelFamily
from viam.utils import struct_to_dict

from chat_service_api import Chat  # type: ignore
from openai import OpenAI

class viam_chatgpt(Chat, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("mcvella", "chat"), "chatgpt")
    openai: OpenAI
    openai_model: str = "gpt-4o"
    system_prompt: str = "You are a helpful assistant that speaks concisely and to the point."
    
    def __init__(self, name: str) -> None:
        super().__init__(name)

    @classmethod
    def new(
        cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]
    ) -> Self:
        llm = cls(config.name)
        llm.reconfigure(config, dependencies)
        return llm

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:

        attributes = struct_to_dict(config.attributes)
        
        api_key = attributes.get("openai_api_key", "")
        if api_key == "":
            raise Exception(f"openai_api_key must be defined")
        
        return []

    def reconfigure(
        self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]
    ):
        attributes = struct_to_dict(config.attributes)
        self.logger.debug(attributes)
        self.openai = OpenAI(api_key=str(attributes.get("openai_api_key", "")))

        return

    async def chat(self, message: str, *, extra: Optional[Mapping[str, Any]] = None, **kwargs) -> str:
        if self.openai is None:
            raise Exception("OpenAI API is not ready")

        response = self.openai.responses.create(
            model=self.openai_model,
            instructions=self.system_prompt,
            input=message,
        )

        response_text = response.output_text
        self.logger.debug(response_text)
        return response_text
