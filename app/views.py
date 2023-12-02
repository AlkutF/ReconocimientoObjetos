import os
import cv2
from app.YoloObject import objectRecognitionPipeline
from flask import rende_template, request
import matplotlib.image as mating

UPLOAD_FOLDER = 'static/upload'

def index():
    return rende_template('index.html')

def app():
    return rende_template('app.html')