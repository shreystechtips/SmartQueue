from datetime import datetime
from uuid import UUID


class Question:
    """Question asked by user.

    Attributes:
        text(str): Question text.
        time_posted(datetime): Date posted.

    """
    def __init__(self, text: str, time_posted: datetime, user_id: UUID):
        self.text = text
        self.time_posted = time_posted
        self.user_id = user_id
