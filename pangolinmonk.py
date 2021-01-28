import random
import os
import sys
from flask import Flask, render_template, url_for
sys.path.insert(0, os.path.basename(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "blarrghhdshsg"


def validImage(fp):
    '''
    A bunch of checks to see if the file is valid.
    '''
    # If it's a dir, don't add. 
    if not os.path.isfile(fp):
        return False
    # If it isn't a common image format, don't add. 
    if os.path.splitext(fp)[1] not in [".jpg",
                                       ".jpeg",
                                       ".png",
                                       ".gif"]:
        return False
    # If it hasn't returned False yet, it passes!
    return True

def randomImage(dir='pmimages'):
    folder = os.path.join(app.static_folder, dir)
    images = list()
    for f in os.listdir(folder):
        item = os.path.join(folder, f)
        if validImage(item):
            images.append(f)
    if len(images) > 0:
        image_name = "{dir}/{fname}".format(dir=dir, fname=random.choice(images))
        image = url_for('static', filename=image_name)
        return image
    else:
        image = url_for('static', filename='pmimages/pangolinmonk.jpg')
        return image

def randomTitle():
    choices = ["HELLO PANGOLIN MONK",
               "LOOK AT THIS MONK",
               "PANGOLIN? MONK? YES",
               "MANIS JAVANICA MONK",
               "UM EXCUSE ME PLEASE"]
    return random.choice(choices)



@app.route('/')
def main():
    title = randomTitle()
    img_fp = randomImage()
    return render_template("index.html", title=title, img_fp=img_fp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
