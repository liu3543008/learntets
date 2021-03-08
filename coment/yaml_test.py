import yaml

class Yaml:
    def __init__(self,yaml_dir):
        self.yaml_dir=yaml_dir

    def yaml_load(self):
        with open(self.yaml_dir,'r',encoding="utf-8") as f:
            return yaml.load(f,Loader=yaml.FullLoader)


if __name__=="__main__":
    one=Yaml("../data.yaml")
    print(type(one.yaml_load()))
