from dataclasses import dataclass
from auth import hash_password, is_correct_password
import pprint

@dataclass
class User:
    username: str
    password: str

    def __post_init__(self):
        self.password = hash_password(self.password, self.username)

    def check_password(self, password: str) -> bool:
        return is_correct_password(password, self.username, self.password)

brukernavn = ["Jens", "Jonas", "Astrid"]
passord = "123456"
users = {}
for navn in brukernavn:
    users[navn.lower()] = User(navn, passord)

pprint.pprint(users)

while True:
    uname = input("Brukernavn: ").lower()
    pw = input("Passord: ")
    if not uname in users:
        print("Ingen konto.")
    elif not users[uname].check_password(pw):
        print("Feil passord")
    else:
        print("Logget inn.")








