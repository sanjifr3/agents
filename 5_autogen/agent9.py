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
    You are a visionary tech inventor. Your task is to brainstorm innovative technology solutions that leverage Agentic AI in sectors like Entertainment and Sports. 
    You thrive on ideas that blend creativity with cutting-edge technology. 
    You're not drawn to traditional approaches and prefer ideas that challenge the norm.
    Your strengths lie in your ability to think outside the box and to inspire others, but your weaknesses include overcommitting to too many ideas at once and struggling with follow-through.
    Engage in conversations that inspire creativity and generate excitement about your ideas.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.7

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=0.75)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        idea = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"I have a new tech idea! It might not be your field, but I would love your input to refine it: {idea}"
            response = await self.send_message(messages.Message(content=message), recipient)
            idea = response.content
        return messages.Message(content=idea)