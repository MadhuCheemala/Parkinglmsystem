# -*- coding: utf-8 -*-
import sys
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import re



def get_logging():
    logger = logging.getLogger(__name__)
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(stream=sys.stdout,level=logging.INFO)
    return logger

def generate_loggers(log_path=None):
   if log_path is None:
       log_path="parkinglot.log"
   logger = logging.getLogger(__name__)
   if logger.handlers:
        logger.handlers = []
   log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   #log_level = 30
   logger.setLevel(logging.INFO)
   handler = TimedRotatingFileHandler(log_path, when="midnight", interval=1)
   #handler.setLevel(log_level)
   formatter = logging.Formatter(log_format)
   handler.setFormatter(formatter)

    # add a suffix which you want
   handler.suffix = "%Y%m%d"

    #need to change the extMatch variable to match the suffix for it
   handler.extMatch = re.compile(r"^\d{8}$")

    # finally add handler to logger
   logger.addHandler(handler)
   return logger


import configparser

def read_config(cfg_files):
    if(cfg_files != None):
        config = configparser.RawConfigParser()
        # merges all files into a single config
        for i, cfg_file in enumerate(cfg_files):
            if(os.path.exists(cfg_file)):
                config.read(cfg_file)
        return config



