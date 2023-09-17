import os
import shutil

LICENSE = "{{cookiecutter.license}}"
JWT = "{{cookiecutter.use_jwt}}"
PROJECT_SLUG = "{{cookiecutter.project_slug}}"


def delete_resource(resource) -> None:
    if os.path.isfile(path=resource):
        print(f"removing file: {resource}")
        os.remove(path=resource)
    elif os.path.isdir(s=resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


if LICENSE == "None":
    delete_resource(resource="LICENSE")
if JWT == "n":
    delete_resource(resource=f"{PROJECT_SLUG}/authentication/")
    delete_resource(resource=f"{PROJECT_SLUG}/users/")
