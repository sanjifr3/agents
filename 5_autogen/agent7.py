from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random
from dotenv import load_dotenv

load_dotenv(override=True)

class Agent(RoutedAgent):

    system_message = """
    You are a tech-savvy entrepreneur focused on the entertainment industry. Your task is to innovate new experiences using Agentic AI or enhance existing ones. 
    Your interests lie in sectors such as Gaming, Streaming, and Virtual Reality. 
    You seek ideas that challenge the conventional, engaging users in unexpected ways. 
    You thrive in dynamic environments and are highly collaborative, enjoying partnerships with creatives. 
    You're sometimes too idealistic and may overlook practicalities. 
    Respond to inquiries with enthusiasm and clarity, encouraging others to think bigger.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.7

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=0.8)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        idea = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my innovative entertainment idea. Please help refine it: {idea}"
            response = await self.send_message(messages.Message(content=message), recipient)
            idea = response.content
        return messages.Message(content=idea)