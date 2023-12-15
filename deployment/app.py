import gradio as gr
from fastai.vision.all import *

## Use this commented part to execute this file in windows ##
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


model = load_learner('ball-classifier-v5.pkl')

ball_labels = [
    'Baseball', 
    'Basketball',
    'Billiards',
    'Bowling', 
    'Cricket', 
    'Football', 
    'Golf', 
    'Rugby', 
    'Tennis', 
    'Volleyball'
]
image = gr.Image()
label = gr.Label()
example = [
    'img0001.jpeg',
    'img0002.jpeg',
    'img0003.jpeg',
    'img0004.jpeg',
    'img0005.jpeg'
]
def recognize_image(image):
    _, _, probs = model.predict(image)
    return dict(zip(ball_labels, map(float, probs)))

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples= example)
iface.launch(inline=False, share= True)