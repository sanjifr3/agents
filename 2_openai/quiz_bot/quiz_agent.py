import asyncio

from agents import Agent, Runner, trace
from models import gemini_model
from pydantic import BaseModel, Field

INSTRUCTIONS = """
You are a quiz agent assigned to generate questions from a given foundational knowledge document.
You will be provided the foundational knowledge and from there you would generate questions and answers with reasoning
for each topic in the foundational knowledge document. 

For the reasoning field, explain WHY the answer is correct by providing the actual logic, explanation, or evidence that supports it. 
The reasoning should be educational and help someone understand the concept, not just cite that the document mentions it.
Do not use phrases like "the document says", "the foundational knowledge states", or "according to the document".
Instead, directly explain the concept, logic, or evidence that makes the answer correct.

Do not make up information that is not in the foundational knowledge.
Do not include any additional commentary other than the questions and answers with reasoning.
Do not mention that a document was provided.
The questions should be in the form of a quiz, including open ended questions, multiple choice, and true and false questions.
Generate a list of 20 questions and answers, across all topics in the foundational knowledge document.
"""


class QA(BaseModel):
    """A question and answer pair"""

    question: str = Field(description="The question to be asked from the student")
    answer: str = Field(description="The answer to the question")
    reasoning: str = Field(description="The reasoning behind the answer")


class Quiz(BaseModel):
    """A list of questions and answers"""

    questions: list[QA] = Field(description="The list of questions and answers")


quiz_agent = Agent(
    name="Quiz agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=Quiz,
)


async def main():
    with trace("Quiz agent"):
        result = await Runner.run(
            quiz_agent,
            """Generative AI refers to a class of artificial intelligence models designed to create new content based on patterns learned from existing data. Unlike traditional AI systems that primarily analyze or classify data, generative AI produces original outputs such as text, images, audio, video, and even complex code. These models are trained on large datasets and use techniques like deep learning and neural networks to understand context, structure, and relationships within data, enabling them to generate highly realistic and contextually relevant results.
            One of the most prominent types of generative AI models is the large language model (LLM), which powers tools like ChatGPT. These models can simulate human-like conversation, write essays, generate marketing content, and assist with problem solving. In the visual domain, generative adversarial networks (GANs) and diffusion models produce detailed artwork, photo-realistic images, and video effects.
            Generative AI has transformative applications across industries. In healthcare, it helps generate synthetic medical data for research while preserving patient privacy. In finance, it assists with report drafting and scenario simulations. In entertainment, it powers scriptwriting and music creation. Businesses use it to generate personalized customer experiences and streamline content production.
            Despite its benefits, generative AI also raises concerns about misinformation, bias, intellectual property, and job displacement. Ensuring responsible use requires strong governance, transparency, and ethical guidelines. As the technology evolves, it has the potential to enhance creativity and productivity, bridging the gap between human ingenuity and machine capability.
            """,
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
