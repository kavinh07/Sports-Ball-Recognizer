# Ball-Classifier
An image classification model from data collection, cleaning, model training, deployment and API integration. <br/>
The model can classify 10 different types of balls <br/>
The types are following: <br/>
    1. Football<br/>
    2. Basketball<br/>
    3. Volleyball<br/>
    4. Rugby<br/>
    5. Golf<br/>
    6. Cricket<br/>
    7. Tennis<br/>
    8. Bowling<br/>
    9. Billiards<br/>
    10. Baseball<br/>

# Dataset Preparation
**Data Collection:** Downloaded from DuckDuckGo using term name <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `data_prep.ipynb`

# Training and Data Cleaning
**Training:** Fine-tuned a resnet34 model for 5 epochs (5 times) and got upto ~98% accuracy. <br/>
**Data Cleaning:** This part took the highest time. Since I collected data from browser, there were many noises. Also, there were images that contained. I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or finetuning, except for the last time which was the final iteration of the model. <br/>

# Model Deployment
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/kavinh07/ball-classifier). <br/>
<img src = "HuggingFaceSpaceImage.png" width="700" height="350">

# API integration with GitHub Pages
The deployed model API is integrated [here](kavinh07.github.io/Ball-Classifier/) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.
