"""Shared definition: one agent with one tool, made durable for Temporal."""

import os

from pydantic_ai import Agent
from pydantic_ai.durable_exec.temporal import PydanticAIWorkflow, TemporalDurability
from temporalio import workflow

agent = Agent(
    os.getenv("HELLO_MODEL", "openai:gpt-5.2"),
    instructions="You are a concise SRE assistant. Use your tool when asked about servers.",
    name="hello",  # required for durability, and must stay stable: it names the activities
    capabilities=[TemporalDurability()],
)


@agent.tool_plain
def get_server_status(region: str) -> dict:
    """Return the current status of the demo server in the given region."""
    return {"region": region, "status": "degraded", "open_incidents": 2}


@workflow.defn
class HelloWorkflow(PydanticAIWorkflow):
    __pydantic_ai_agents__ = [agent]

    @workflow.run
    async def run(self, prompt: str) -> str:
        result = await agent.run(prompt)
        return result.output
