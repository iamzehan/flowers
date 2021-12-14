from io import BytesIO
from keras.models import model_from_json
from PIL import Image
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import tensorflow as tf

app = FastAPI(docs_url=None)
class_names=['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

@app.get("/",response_class=HTMLResponse)
async def main():
    content = """
<head>
        <style> 
            input[type=submit] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            float: middle;
            }
            input[type=text] {
            width: 20%;
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
            border-radius: 5px;
            border: 2px solid black;
            background-color: #f2f2f2;
            }
            .container {
            border-radius: 5px;
            background-color: #f2f2f2;
            padding: 100px;
            width: 40%;
            display: block;
            margin-left: auto;
            margin-right: auto;
            }
            h1{
                text-align: center;
            }
        </style>
    </head>
<body>
<h1>Upload a jpeg Image</h1>
        <div class="container">
        <p> The model can recognize 'daisy', 'dandelion', 'roses', 'sunflowers', and 'tulips'</p>
            <form action="/prediction/" enctype="multipart/form-data" method="post">
                <input name="file" type="file" multiple>
                <input type="submit">
            </form>
        </div>
</body>
    """
    return HTMLResponse(content=content)


json_file = open('./model/flower_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

model.load_weights("./model/flower_model.h5")

@app.post('/prediction/')
async def get_flower_class(file: UploadFile = File(...)):
    file=await file.read()
    image1=Image.open(BytesIO(file))
    image=image1.resize((180,180))
    image_array = np.array(image)
    image_array= np.expand_dims(image_array, axis=0)
    predictions=model.predict(image_array)
    score = tf.nn.softmax(predictions[0])
    return {"class": class_names[np.argmax(score)], "confidence": f"{round(100 * np.max(score))}%"}