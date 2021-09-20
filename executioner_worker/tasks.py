from typing import List,Dict
from executioner.evaluate import Evaluation,TestCase
from executioner.program import Program

def evaluate(evaluation: Dict) -> List[Dict]:
    ev = Evaluation.from_json_object(evaluation)
    ev.evaluate()
    del ev.program
    return [testcase.to_json_object() for testcase in ev.testcases]

def execute(program: Dict,testcase: Dict) -> Dict:
    test = TestCase.from_json_object(testcase)
    with Program.from_json_object(program) as pgm:
        pgm.compile()
        pgm.execute(test)
    return test.to_json_object()
