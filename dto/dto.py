from pydantic import BaseModel

# Defining input / output classes of api requests
class UserRequestIn(BaseModel):
    input: dict

class PredictionOut(BaseModel):
    prediction: dict