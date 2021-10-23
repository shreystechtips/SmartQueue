from datetime import datetime
from question import Question


class QuestionGroup:
    """Group of Questions.

    Attributes:
        cluster_id: Cluster identifier.
        questions: Question objects.
        active: True if questions should still be added to group.

    """

    def __init__(self, group_id: str, questions: list[Question], active:
                 bool):
        self.cluster_id = group_id
        self.questions = questions
        self.active = active
