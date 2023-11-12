from datetime import datetime
import uuid


def slug_generator():
    # Generate a unique identifier (UUID)
    unique_id = uuid.uuid4().hex[:6]
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    slug = f"{unique_id}{current_datetime}"
    return slug
