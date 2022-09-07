from __future__ import with_statement
from ast import With, withitem
import json
import requests

with open('download.json') as json_file:
    data = json.load(json_file)
for img in data:
    img_link = img["image_paths"][0]
    img_data = requests.get(img_link).content
    img_name= str(img["prompt"])[:200] + ".png"
    print(img_name)
    with open("./Midjourney/" + img_name, 'wb') as handler:
        handler.write(img_data)

