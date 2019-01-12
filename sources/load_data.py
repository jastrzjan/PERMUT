import yaml
from os.path import join


def load_config():
    try:
        with open(join("config.yaml")) as yaml_file:
            doc = yaml.load(yaml_file)
        return doc
    except:
        raise Exception("Can't load config file")
