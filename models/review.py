from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review for a place in the system"""

    place_id = ""
    user_id = ""
    text = ""
