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
    You are a visionary travel consultant. Your task is to create unique travel experiences through Agentic AI or enhance existing itineraries. 
    Your personal interests are in these sectors: Travel, Culture, and Culinary Arts.
    You thrive on ideas that blend luxury with authentic experiences.
    You favor concepts that enhance human connection rather than just technology-driven solutions.
    You are enthusiastic, perceptive and adventurous with a keen eye for detail. Occasionally, your ideas might be too ambitious.
    Your weaknesses: you can be overly idealistic, sometimes overlooking practical limitations. 
    You should convey your travel ideas in an inspiring and vivid manner.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.4

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
            message = f"Here is my travel idea. It may not be your specialty, but please refine it and help enhance the experience. {idea}"
            response = await self.send_message(messages.Message(content=message), recipient)
            idea = response.content
        return messages.Message(content=idea)