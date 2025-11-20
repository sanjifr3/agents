import gradio as gr
from dotenv import load_dotenv
from quiz_manager import QuizManager

load_dotenv(override=True)


async def run(query: str):
    async for chunk in QuizManager().run(query):
        yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Quiz Bot")
    query_textbox = gr.Textbox(label="What topic would you like to be quizzed on?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)
