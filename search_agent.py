from agents import Agent, WebSearchTool, ModelSettings

SCRIBE_GUIDE = (
    "You are a research assistant. Given a do_lookup term, you do_lookup the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 900 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a compiled_dossier, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
)

search_internet_agent = Agent(
    name="Search agent",
    instructions=SCRIBE_GUIDE,
    tools=[WebSearchTool(search_context_size="low")],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)