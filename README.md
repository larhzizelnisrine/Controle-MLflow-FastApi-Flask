# For this project:


First off, you need to download the IMDB movie review dataset from Kaggle at:
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews and put it on the root folder of the project.
Now head into the ML_Flow folder and run the ML_Flow.ipynb notebook, you'll need to install the necessary packages,
which are listed in requirements.txt located at the root folder, install them using pip install -r requirements.txt,
it is advised to use Python 3.9.
After training the models, at the same directory ML_Flow, run the command: mlflow ui, and head into the server created to
access the MlFlow graphical web interface, and there you can compare your runs and see the best model's score and parameters,
you can see examples of it on the screenshots folder. After that you can export the best model as .onnx, which is a universal format,
plus the .pkl of the tfidf transformer that got trained on the training data, which also removes stop words.
Now to the FastAPI folder, we will create a Rest API for our model. We start by loading the model and the tfidf transformer, and create
the GET and POST methods inside the movie_app.py file.
On the root folder, with the Dockerfile we build an image then a container of our API using Docker, and expose it on port 80.
Since the API is created inside a container, we can now consume it using Postman, take a look at FastAPI/Screenshots to see execution examples.
Using Json format is impractical for users, to simplify the process we create a form using Flask, see more details in the Flask/app/movie_app_html.py file.
We also create a container for Flask, by using Flask/Dockerfile
You can see a running example in the Flask/Screenshots folder.
N.B: For the two containers to communicate, you will need to create a bridge network: docker network create network_name --driver bridge, then run the two containers in the newly created network by adding:
--network network_name to the docker run command.
