## * How to deploy a neural network based image classifier on the web with FastAPI

### _(Hold up! This repository does not contain the code for training the Neural Network, we are using a pretrained saved model.)_  

### * Before you go ahead and clone this repository check your python version

### * Since Tensorflow is being used in the project, python 3.9.x is used, tensorflow yet has to release a version for 3.10.x

### * Make sure you have wheels installed in your python scripts. If you don't then run this command anyway, just to be safe -

    pip install wheels

### Clone this repository

    git clone "https://github.com/iamzehan/flowers.git" 

### Create a virtual environment in the root directory

    virtualenv env

### Activate virtual environment

for bash-

    source env/Scripts/activate

for cmd-

    ./env/Scripts/activate
    

### Install dependencies/packages

    pip install requirements.txt


### Run the app

    uvicorn app:app --reload
    
### Checkout SwaggerUI docs, make sure you go to ```app.py``` and change this line ```app = FastAPI(docs_url=None)``` to ```app = FastAPI(docs_url='/docs')```

    <localhostserver>/docs

### Go checkout FastAPI over at https://fastapi.tiangolo.com/tutorial/ to know more! 
