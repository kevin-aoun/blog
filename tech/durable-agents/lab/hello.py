"""Shared definition: one agent with one tool, wrapped for Temporal."""

import os

from pydantic_ai import Agent
from pydantic_ai.durable_exec.temporal import PydanticAIWorkflow, TemporalAgent
from temporalio import workflow

agent = Agent(
    os.getenv("HELLO_MODEL", "openai:gpt-5.2"),
    instructions="You are a concise SRE assistant. Use your tool when asked about servers.",
    name="hello",  # required by TemporalAgent, and must stay stable: it names the activities
)


@agent.tool_plain
def get_server_status(region: str) -> dict:
    """Return the current status of the demo server in the given region."""
    return {"region": region, "status": "degraded", "open_incidents": 2}

#--------------------------------------------

temporal_agent = TemporalAgent(agent)


@workflow.defn
class HelloWorkflow(PydanticAIWorkflow):
    __pydantic_ai_agents__ = [temporal_agent]

    @workflow.run
    async def run(self, prompt: str) -> str:
        result = await temporal_agent.run(prompt)
        return result.output
