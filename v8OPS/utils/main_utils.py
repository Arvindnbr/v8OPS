import os.path
import sys
import yaml
import base64

from v8OPS.logger import logging
from v8OPS.exception import AppException

#function to read a yaml file
def read_yaml(filepath: str)->dict:
    try:
        with open(filepath,'rb') as yml:
            logging.info("yaml file read sucessfully")
            return yaml.safe_load(yml)
    
    except Exception as e:
        raise AppException(e, sys) from e
    
#decoding image
def decode_image(imagestring, filename):
    img = base64.b64decode(imagestring)
    with open("./data/"+filename,'wb') as f:
        f.write(img)
        f.close()

#encoding image
def encoding_image(CroppedImagePath):
    with open(CroppedImagePath,'rb') as g:
        return base64.b64encode(g.read())
    
