from typing import List
from pydantic import BaseModel

class TestcaseBase(BaseModel):
    input: str
    output: str

class Testcase(TestcaseBase):
    id: int
    class Config:
        orm_mode = True

class ProblemBase(BaseModel):
    statement: str

class Problem(ProblemBase):
    id: int
    testcases: List[Testcase] = []
    class Config:
        orm_mode = True
