from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/table/{first_value}&{second_value}")
async def get_table(first_value: float = Path(gt=0),
                    second_value: float = Path(gt=0)):

    table = {
        'sum': first_value + second_value,
        'sub': first_value - second_value,
        'mul': first_value * second_value,
        'div': first_value / second_value,
    }
    return table