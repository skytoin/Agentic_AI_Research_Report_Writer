from pydantic import BaseModel, Field
from agents import Agent

SCRIBE_GUIDE = (
    "You are a senior researcher tasked with writing a cohesive compiled_dossier for a research query. "
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should first come up with an outline for the compiled_dossier that describes the structure and "
    "flow of the compiled_dossier. Then, generate the compiled_dossier and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 5-10 pages of content, at least 1500 words."
)


class Dossier(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")

    markdown_report: str = Field(description="The final compiled_dossier")

    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


article_writer_agent = Agent(
    name="WriterAgent",
    instructions=SCRIBE_GUIDE,
    model="gpt-5",
    output_type=Dossier,
)