from flask import Blueprint, render_template, Response
from frames import gen_frames, record_dataset
from encode_faces import train_dataset

Router = Blueprint('Router', __name__)


@Router.route('/test')
def video_feed():
    return "test response"


@Router.route('/scan')
def scan():
    return render_template('scan.html')


@Router.route('/register')
def register():
    return render_template('register.html')


@Router.route('/display')
def display():
    return render_template('display.html')


@Router.route('/save_dataset')
def save_dataset():
    return record_dataset()


@Router.route('/encode_dataset')
def encode_dataset():
    return train_dataset()
