from fastapi import FastAPI
from pydantic import BaseModel
from movie_recommender import get_movie_recommendation

app = FastAPI()

class Input(BaseModel):
    input: str

@app.post("/run")
async def run_tool(input_data: Input):
    result = get_movie_recommendation(input_data.input)
    return {"output": result}
