import asyncio
from fastapi import WebSocket, APIRouter, Depends
from rq import Queue
from executioner.program import Program
from executioner.evaluate import TestCase
from executioner_worker.tasks import execute

from app.deps import get_queue

submission_router = APIRouter()


async def run_program(websocket: WebSocket, queue: Queue, program: str, language: str, input_text: str):
    with Program(program, language) as pgm:
        job = queue.enqueue(execute, pgm.to_json_object(),
                            TestCase(input_text).to_json_object())
        while not job.result:
            await asyncio.sleep(1)
        await websocket.send_json({"command": "response", "result": job.result})


@submission_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, queue: Queue = Depends(get_queue)):
    await websocket.accept()
    await websocket.send_json({"command": "welcome"})
    while True:
        data = await websocket.receive_json()
        if data["command"] == "execute":
            if ("program" not in data) or ("language" not in data):
                await websocket.send_json({"command": "error", "text": "invalid execute command"})
                continue
            await run_program(
                    websocket,
                    queue,
                    data["program"],
                    data["language"],
                    data.get("input", ""),
                )
