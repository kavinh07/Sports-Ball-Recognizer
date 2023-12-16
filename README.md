# Ball-Classifier
An image classification model from data collection, cleaning, model training, deployment and API integration. <br/>
The model can classify 10 different types of balls <br/>
The types are the following: <br/>
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
**Data Collection:** Downloaded from DuckDuckGo using term name and adding extra string ' only balls images'<br/>
**DataLoader:** Used FastAI DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** FastAI provides default data augmentation which operates in GPU. <br/>
Details can be found in `data_prep.ipynb` or [![Colab](https://img.shields.io/badge/-you_like-blue?logo=colab)](https://colab.research.google.com/drive/1OPwZfhkUtTQgKBwDeA8-YcY08l-vU_x9?usp=sharing)

# Training and Data Cleaning
**Training:** Fine-tuned a resnet34 model for 5 epochs (5 times) and achieved ~99% accuracy. <br/>
**Data Cleaning:** This part took the longest time. Since I collected data from the browser, there were many noises. Also, some images contained. I cleaned and updated data using FastAI ImageClassifierCleaner. I cleaned the data each time after training or fine-tuning, except for the last time which was the final iteration of the model. <br/>

# Model Deployment
I deployed the model to the HuggingFace Spaces Gradio App. The implementation can be found in the `deployment` folder or [here](https://huggingface.co/spaces/kavinh07/ball-classifier). <br/>
![HuggingFaceSpaceImage.png](https://github.com/kavinh07/Ball-Classifier/blob/main/deployment/HuggingFaceSpaceImage.png)

# API integration with GitHub Pages
The deployed model API is integrated [here](https://kavinh07.github.io/Ball-Classifier/) in the GitHub Pages Website. Implementation and other details can be found in the `docs` folder.
