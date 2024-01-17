import os
from crudgenerator.template import Template

template = Template()


def generate(entityName: str, targetPath: str):
    workingPath = os.getcwd()
    template.generateForEntity(entityName, workingPath, targetPath)
