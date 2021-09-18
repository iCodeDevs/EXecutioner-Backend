from typing import List,Dict
from executioner.program import Program
from executioner.evaluate import Evaluation,TestCase

from .celery import app

@app.task
def execute(source: str,language: str,inputs: List[str],outputs: List[str]) -> List[Dict[str,int]]:
    with Program(source,language) as pgm:
        testcases = [TestCase(inp,out) for inp,out in zip(inputs,outputs)]
        ev = Evaluation(pgm,testcases)
        ev.evaluate()
    return [testcase.scores for testcase in testcases]

