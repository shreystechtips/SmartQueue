from datetime import datetime
from question import Question


class QuestionCluster:
    """Group of Question objects.

    Attributes:
        questions: Questions.
        active: True if questions should still be added to group.

    """

    def __init__(self, cluster_id: str, questions: list[Question], active:
                 bool):
        self.questions = questions
        self.active = active
