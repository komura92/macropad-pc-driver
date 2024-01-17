from pathlib import Path


class Template:
    def __init__(self):
        self.TEMPLATE_ENTITY_NAME = "Task"
        self.TEMPLATE_PACKAGE_NAME = "com.itninja.simplecrudpgjdk21.domain.task"
        self.TEMPLATE_ELEMENTS = [
            "service",
            "controller",
            "repository",
            "mapper",
            "model",
            "entity"
        ]
        self.SUFFIX_BY_TEMPLATE_ELEMENT = {
            "model": "Dto",
            "entity": ""
        }

        self.templateEntityLowercase = self.TEMPLATE_ENTITY_NAME[0].lower() + self.TEMPLATE_ENTITY_NAME[1:]

    def generateForEntity(self,
                          entityName: str,
                          workingPath: str,
                          targetPath: str):
        targetPackagePath = targetPath + "\\" + entityName.lower()

        for template_element in self.TEMPLATE_ELEMENTS:
            template_element_dir_path = Path(workingPath).joinpath("template").joinpath(template_element)

            # create subpackage
            targetSubpackagePath = Path(targetPath).joinpath(entityName.lower()).joinpath(template_element)
            Path(targetSubpackagePath).mkdir(parents=True, exist_ok=True)

            # load template class
            templateFilename = self.TEMPLATE_ENTITY_NAME + self.getSuffix(template_element) + ".java"
            templateContent = Path(template_element_dir_path).joinpath(templateFilename).read_text()

            # fix package name and replace self.TEMPLATE_ENTITY_NAME with entityName
            targetContent = templateContent.replace(self.TEMPLATE_PACKAGE_NAME,
                                                    targetPackagePath
                                                    .replace("\\", ".")
                                                    .replace("/", ".")
                                                    .split(".src.main.java.")[1])
            targetContent = targetContent.replace(self.TEMPLATE_ENTITY_NAME, entityName)
            entityNameLowercase = entityName[0].lower() + entityName[1:]
            targetContent = targetContent.replace(self.templateEntityLowercase, entityNameLowercase)

            # save to target dir with proper name
            targetFilename = entityName + self.getSuffix(template_element) + ".java"
            Path(targetSubpackagePath).joinpath(targetFilename).write_text(targetContent)

    def getSuffix(self, template_element):
        if template_element in self.SUFFIX_BY_TEMPLATE_ELEMENT.keys():
            return self.SUFFIX_BY_TEMPLATE_ELEMENT[template_element]
        return template_element.capitalize()
