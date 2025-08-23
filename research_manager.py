from agents import Runner, trace, gen_trace_id
from search_agent import search_internet_agent
from planner_agent import scout_planner, QueryIdea, QueryPlan
from writer_agent import article_writer_agent, Dossier
from email_agent import email_writer_agent
import asyncio

class InsightOrchestrator:

    async def execute_flow(self, query: str):
        """ Run the deep research process, yielding the status updates and the final compiled_dossier"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print("Starting research...")
            plan_of_queries = await self.design_query_plan(query)
            yield "Searches planned, starting to do_lookup..."     
            collected_notes = await self.conduct_queries(plan_of_queries)
            yield "Searches complete, writing compiled_dossier..."
            compiled_dossier = await self.compose_dossier(query, collected_notes)
            yield "Report written, sending email..."
            await self.deliver_via_email(compiled_dossier)
            yield "Email sent, research complete"
            yield compiled_dossier.markdown_report
        

    async def design_query_plan(self, query: str) -> QueryPlan:
        """ Plan the searches to perform for the query """
        print("Planning searches...")
        result = await Runner.run(
            scout_planner,
            f"Query: {query}",
        )
        print(f"Will perform {len(result.final_output.searches)} searches")
        return result.final_output_as(QueryPlan)

    async def conduct_queries(self, plan_of_queries: QueryPlan) -> list[str]:
        """ Perform the searches to perform for the query """
        print("Searching...")
        num_completed = 0
        tasks = [asyncio.create_task(self.do_lookup(item)) for item in plan_of_queries.searches]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
            num_completed += 1
            print(f"Searching... {num_completed}/{len(tasks)} completed")
        print("Finished searching")
        return results

    async def do_lookup(self, item: QueryIdea) -> str | None:
        """ Perform a do_lookup for the query """
        prompt_payload = f"Search term: {item.query}\nReason for searching: {item.reason}"
        try:
            result = await Runner.run(
                search_internet_agent,
                prompt_payload,
            )
            return str(result.final_output)
        except Exception:
            return None

    async def compose_dossier(self, query: str, collected_notes: list[str]) -> Dossier:
        """ Write the compiled_dossier for the query """
        print("Thinking about compiled_dossier...")
        prompt_payload = f"Original query: {query}\nSummarized do_lookup results: {collected_notes}"
        result = await Runner.run(
            article_writer_agent,
            prompt_payload,
        )

        print("Finished writing compiled_dossier")
        return result.final_output_as(Dossier)
    
    async def deliver_via_email(self, compiled_dossier: Dossier) -> None:
        print("Writing email...")
        result = await Runner.run(
            email_writer_agent,
            compiled_dossier.markdown_report,
        )
        print("Email sent")
        return compiled_dossier