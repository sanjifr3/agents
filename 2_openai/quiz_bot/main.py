import gradio as gr
from agents import Runner, trace
from dotenv import load_dotenv
from research_manager import research_manager_agent

load_dotenv(override=True)


async def run(query: str):
    with trace("Quiz Bot"):
        result = Runner.run_streamed(research_manager_agent, query)
        output = ""
        async for event in result.stream_events():
            # 🔹 Skip raw streaming chunks, only show relevant messages
            if event.type == "raw_response_event":
                # Skip raw response events for cleaner output
                continue
            elif event.type == "agent_updated_stream_event":
                agent_name = getattr(event, "new_agent", None)
                if agent_name:
                    output += f"🧠 Agent switched to: **{agent_name.name}**\n\n"
                    yield output
            elif event.type == "run_item_stream_event":
                item = getattr(event, "item", None)
                if item:
                    item_type = getattr(item, "type", "")
                    if item_type == "tool_call_item":
                        raw_item = getattr(item, "raw_item", None)
                        tool_name = (
                            getattr(raw_item, "name", "Unknown")
                            if raw_item
                            else "Unknown"
                        )
                        output += f"🔧 Tool called: **{tool_name}**\n\n"
                        yield output
                    elif item_type == "tool_call_output_item":
                        output += "📨 Tool output received\n\n"
                        yield output
                    elif item_type == "message_output_item":
                        # This contains the final agent message/output
                        message_output = getattr(item, "output", "")
                        if message_output:
                            output += f"\n\n{message_output}"
                            yield output

        # Yield final output at the end if available
        try:
            if hasattr(result, "final_output") and result.final_output:
                final = result.final_output
                if final and final not in output:
                    output += f"\n\n{final}"
        except Exception:
            pass  # Ignore errors accessing final_output

        yield output


# async def run(query: str):
#     async for chunk in ResearchManager().run(query):
#         yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Quiz Bot")
    query_textbox = gr.Textbox(label="What topic would you like to be quizzed on?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)
