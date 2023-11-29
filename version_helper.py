def get_version():
    with open("version", "r") as file:
        VERSION = file.readline().strip()
        return str(VERSION)