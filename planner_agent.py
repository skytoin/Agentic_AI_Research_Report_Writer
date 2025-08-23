from pydantic import BaseModel, Field
from agents import Agent

NUM_SUGGESTED_QUERIES = 5

SCRIBE_GUIDE = f"You are a helpful research assistant. Given a query, come up with a set of web searches \
to perform to best answer the query. Output {NUM_SUGGESTED_QUERIES} terms to query for."


class QueryIdea(BaseModel):
    reason: str = Field(description="Your reasoning for why this do_lookup is important to the query.")
    query: str = Field(description="The do_lookup term to use for the web do_lookup.")


class QueryPlan(BaseModel):
    searches: list[QueryIdea] = Field(description="A list of web searches to perform to best answer the query.")
    
scout_planner = Agent(
    name="PlannerAgent",
    instructions=SCRIBE_GUIDE,
    model="gpt-5",
    output_type=QueryPlan,
)