import asyncio
import os
from typing import Dict

import sendgrid
from agents import Agent, Runner, function_tool, trace
from dotenv import load_dotenv
from models import gemini_model
from sendgrid.helpers.mail import Content, Email, Mail, To

load_dotenv(override=True)


@function_tool
def send_email(subject: str, html_body: str, to_email: str) -> Dict[str, str]:
    """Send an email to the given email address with the given subject and HTML body"""
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    from_email = Email(os.getenv("SENDGRID_EMAIL"))
    to_email = To(to_email)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    print("Email response", response.status_code)
    print(f"Email sent to {to_email} with subject {subject} and body {html_body}")
    return {"status": "success", "status_code": str(response.status_code)}


INSTRUCTIONS = """
You can send an email to a given email address based on a detailed report.
You will be provided with a detailed report and the target email address. 
From the report, create a clean, well presented HTML email with an appropriate subject line.
Use your tool to send the email to the target email address.
"""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model=gemini_model,
)


async def main():
    with trace("Email agent"):
        result = await Runner.run(
            email_agent,
            """Send an email to r.sanjif@hotmail.com with the details about this report: 
            Generative AI refers to a class of artificial intelligence models designed to create new content, such as text, images, audio, video, or even software code. Unlike traditional AI systems that focus on classification or prediction, generative models learn patterns from large datasets and use that knowledge to produce original outputs that resemble human-created content. Modern generative AI is largely powered by deep learning architectures, including Generative Adversarial Networks (GANs), Variational Autoencoders (VAEs), and transformer-based models like large language models (LLMs).

Applications of generative AI span a wide range of industries. In creative fields, it supports design, music composition, storytelling, and digital art. In business, it enables automated customer support, personalized marketing, and rapid content production. Scientific research uses generative models to accelerate drug discovery, simulate physical systems, and interpret complex data. Software engineering benefits from AI-assisted coding tools that increase productivity and reduce development time.

Despite its advantages, generative AI also raises concerns. Issues such as misinformation, copyright challenges, bias, and the ethical use of synthetic media require careful management. Effective governance, transparency, and responsible deployment are essential to ensure the technology benefits society. As generative AI continues to evolve, it promises transformative impact while demanding thoughtful oversight.

            """,
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
