"""The starter: submits one workflow execution and waits for the result.

Note it never runs the agent itself; it only asks the Temporal server to
schedule the work. The worker picks it up from the task queue.
"""

import asyncio
import sys
import uuid

from pydantic_ai.durable_exec.temporal import PydanticAIPlugin
from temporalio.client import Client

from hello import HelloWorkflow

TASK_QUEUE = "hello"


async def main() -> None:
    prompt = " ".join(sys.argv[1:]) or "What is the status of the eu-west server? One sentence."
    client = await Client.connect("localhost:7233", plugins=[PydanticAIPlugin()])
    workflow_id = f"hello-{uuid.uuid4().hex[:8]}"
    output = await client.execute_workflow(
        HelloWorkflow.run,
        args=[prompt],
        id=workflow_id,
        task_queue=TASK_QUEUE,
    )
    print(f"workflow id: {workflow_id}")
    print(output)


if __name__ == "__main__":
    asyncio.run(main())
