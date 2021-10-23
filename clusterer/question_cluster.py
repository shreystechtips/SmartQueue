from datetime import datetime
from question import Question


class QuestionCluster:
    """Group of Questions.

    Attributes:
        cluster_id: Cluster identifier.
        questions: Question objects.
        active: True if questions should still be added to group.

    """

    def __init__(self, cluster_id: str, questions: list[Question], active:
                 bool):
        self.cluster_id = cluster_id
        self.questions = questions
        self.active = active
