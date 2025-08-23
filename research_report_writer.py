import gradio as gr
from dotenv import load_dotenv
from research_manager import InsightOrchestrator

load_dotenv(override=True)


async def execute_flow_ui(query: str):
    async for chunk in InsightOrchestrator().execute_flow(query):
        yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research (Refactored)")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    
    run_button.click(fn=execute_flow_ui, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=execute_flow_ui, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)
