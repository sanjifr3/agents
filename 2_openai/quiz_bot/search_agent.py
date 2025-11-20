import asyncio

from agents import Agent, ModelSettings, Runner, WebSearchTool, trace

INSTRUCTIONS = """
You are a research assistant helping to create content for a quiz bot.  
Given a topic, you search the web for that topic and 
produce a concise summary of the results. The summary must be 2-3 paragraphs and under 500 words. 
words. Capture the main points. Write succintly, no need to have complete sentences or good 
grammar. This will be consumed by someone synthesizing a report, so it's vital you capture the 
essence and ignore any fluff. 
IMPORTANT: Always preserve and include the source URLs that are provided in the search results. 
When you mention information from a source, include the URL reference in the format: (source.com) 
or [Title](URL). Keep all source links intact in your summary.
Do not include any additional commentary other than the summary itself with preserved source links.
"""

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size="low")],
    model="gpt-5-nano",
    model_settings=ModelSettings(tool_choice="required"),
)


async def main():
    with trace("Search agent"):
        result = await Runner.run(
            search_agent,
            "Generative AI",
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
