def get_token():
    with open("./token.txt", "r") as file:
        token = file.readline().strip()
        return str(token)