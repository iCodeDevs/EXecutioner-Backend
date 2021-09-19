from typing import List,Dict
from executioner.evaluate import Evaluation

def execute(evaluation: Dict) -> List[Dict]:
    ev = Evaluation.from_json_object(evaluation)
    ev.evaluate()
    del ev.program
    return [testcase.to_json_object() for testcase in ev.testcases]

