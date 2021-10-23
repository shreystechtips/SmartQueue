from datetime import datetime


class Question:
    """Question asked by user.

    Attributes:
        question_id: Question identifier.
        user_id: User who asked the question.
        text Question text.
        time_posted: Date posted.

    """

    def __init__(self, question_id: str, user_id: str, text: str,
                 time_posted: datetime):
        self.question_id = question_id
        self.user_id = user_id
        self.text = text
        self.time_posted = time_posted
