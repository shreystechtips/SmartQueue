from datetime import datetime

class Question:
    """Question asked by user.

    Attributes:
        text(str): Question text.
        time_posted(datetime): Date posted.

    """
    def __init__(self, text: str, time_posted: datetime):
        self.text = text
        self.time_posted = time_posted
