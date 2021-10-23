from datetime import datetime

from question import Question


class QuestionGroup:
    """Group of Question objects.

    Attributes:
        questions(list[Question): Questions.
        active(bool): True if questions should still be added to group.

    """
    def __init__(self, questions: list[Question], active: bool):
        self.questions = questions
        self.active = active
