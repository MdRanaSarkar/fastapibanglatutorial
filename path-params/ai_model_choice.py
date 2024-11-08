from enum import Enum
from fastapi import FastAPI

app = FastAPI()

    
class ModelName(str, Enum):
    efficient_net = "efficient-net"
    resnet = "resnet"
    lesnet = "lesnet"
    vgg = "vgg"


@app.get("/model/{model_name}")
async def get_model(model_name : ModelName):
    if model_name is ModelName.efficient_net:
        return  {"model_name": model_name, "MSG": "Chosen Efficient "}
    elif model_name is ModelName.resnet:
        return  {"model_name": model_name, "MSG": "Chosen ResNet "}
    else:
        return  {"model_name": model_name, "MSG": "Chosen VGG or Lesnet "}