def get_token():
    with open("token.txt", "r") as file:
        TOKEN = file.readline().strip()
        return str(TOKEN)