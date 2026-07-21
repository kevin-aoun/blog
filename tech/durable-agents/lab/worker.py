"""The worker: a long-running process that executes workflows and activities.

This is the process that dies in later experiments. For now it just runs.
"""

import asyncio

from pydantic_ai.durable_exec.temporal import PydanticAIPlugin
from temporalio.client import Client
from temporalio.worker import Worker

from hello import HelloWorkflow

TASK_QUEUE = "hello"


async def main() -> None:
    client = await Client.connect("localhost:7233", plugins=[PydanticAIPlugin()])
    worker = Worker(client, task_queue=TASK_QUEUE, workflows=[HelloWorkflow])
    print(f"worker up on task queue {TASK_QUEUE!r} (ctrl-c to stop)")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
