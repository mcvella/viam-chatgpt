# ChatGPT Modular Resource

`viam-chatgpt` is a modular resource that provides ChatGPT text integration for machines running on the Viam platform.

This module connects to OpenAI's API to provide state-of-the-art language model capabilities to your Viam machines.

## Prerequisites

The machine using this module must have Python 3.8+ and pip installed on the system. You will also need an OpenAI API key to use this module.

## Config

**openai_api_key** (Required): Your OpenAI API key.

**openai_model** (Optional): The OpenAI model to use. Defaults to "gpt-4o".

**system_prompt** (Optional): The context for the chat system to use when interpreting input from the user. Defaults to "You are a helpful assistant that speaks concisely and to the point."

The following is an example configuration for this resource's attributes:

```json
{
    "openai_api_key": "your-api-key-here",
    "openai_model": "gpt-4o",
    "system_prompt": "You are a helpful robot assistant. Provide clear and concise answers."
}
```

## Usage

This module is built as a [Chat service](https://github.com/viam-labs/chat-service-api) that has a single method called "chat".

### Python

First, you'll need to add the Chat API to your project (for example, add this to your requirements.txt):

``` bash
chat-service-api @ git+https://github.com/viam-labs/chat-service-api.git@v0.1.5
```

```python
from chat_service_api import Chat

# machine connection logic above

chatgpt = Chat.from_robot(robot, name="chatgpt")
response = await chatgpt.chat("What is the meaning of life?")
print(response)
```

### Go

```go
import chat "github.com/viam-labs/chat-service-api/src/chat_go"

chatgpt, err := chat.FromRobot(robot, "chatgpt")
resp, err := chatgpt.Chat(ctx, "What is the meaning of life?")
fmt.Println(resp)
```
