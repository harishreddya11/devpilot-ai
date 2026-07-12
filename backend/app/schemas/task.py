from enum import Enum


class TaskType(str, Enum):
    REVIEW = "review"
    GENERATE = "generate"
    EXPLAIN = "explain"
    FIX = "fix"