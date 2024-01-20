# Sports-Ball-Recognizer
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

## Dataset Preparation
**Data Collection:** Downloaded from DuckDuckGo using term name and adding extra string ' only balls images'. A total of **2872** images were collected initially. After unlinking the damaged data, the total number of images was **2776**.<br/>
**DataLoader:** Used FastAI DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** FastAI provides default data augmentation which operates in GPU. <br/>
Details can be found in `data_prep.ipynb` or [![Colab](https://img.shields.io/badge/Colab-data_prep-blue?logo=googlecolab)](https://colab.research.google.com/drive/1OPwZfhkUtTQgKBwDeA8-YcY08l-vU_x9?usp=sharing)

## Training and Data Cleaning
**Training:** Fine-tuned several pre-trained models for 5 epochs and got resnet34 as the best model. Then resnet34 was finetuned for 4 more times (Total 5 times) and achieved ~99% accuracy. <br/>
**Results Comparison:**
Models|Train Loss|Valid Loss|Error Rate|Accuracy
:---|---:|---:|---:|---:
Resnet34|0.052|0.043|0.011|98.87%
GoogleNet|0.694|0.811|0.213|78.65%
VGG16|0.472|0.557|0.176|82.4%
MobileNet V3 Small|0.920|0.882|0.250|74.91%

**Data Cleaning:** This part took the longest time. Since I collected data from the browser, there were many noises. Also, some images contained. I cleaned and updated data using FastAI ImageClassifierCleaner. I cleaned the data each time after training or fine-tuning, except for the last time which was the final iteration of the model. <br/>
You can check the data training and cleaning process in `model_imp.ipynb` or [![Colab](https://img.shields.io/badge/Colab-model_imp-blue?logo=googlecolab)](https://drive.google.com/file/d/1F9vbLydTH0h-tOJwaLiBJ_vmrjL-cfUp/view?usp=sharing).

## Model Deployment
I deployed the model to the HuggingFace Spaces Gradio App. The implementation can be found in the `deployment` folder or [![Hugging Face Interface](https://img.shields.io/badge/Hugging_Face-Sports_Ball_Recognizer-ffff00)](https://huggingface.co/spaces/kavinh07/ball-classifier). <br/>
![HuggingFaceSpaceImage.png](https://github.com/kavinh07/Ball-Classifier/blob/main/deployment/HuggingFaceSpaceImage.png)

## API integration with GitHub Pages
The deployed model API is integrated [![Git Interface](https://img.shields.io/badge/-Sports_Ball_Recognizer-blue?logo=githubpages)](https://kavinh07.github.io/Ball-Classifier/) in the GitHub Pages Website. Implementation and other details can be found in the `docs` folder.
