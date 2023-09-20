import os

class Client:
    def __init__(self, name):
        self._fullname = name.title() + " LLC"
        self._homepage = f"https://{''.join(name.split(' ')).lower()}.net/"
        self._brand = name.title()
        self._staff = []
        stafflist = os.environ[f"{'_'.join(name.upper().split(' '))}_STAFF"]
        for i in stafflist.split(" "):
            self._staff.append(i)

    def fullname(self) -> str | None:
        if self._fullname is not None:
            return str(self._fullname)
        else:
            return None

    def homepage(self) -> str | None:
        if self._homepage is not None:
            return str(self._homepage)
        else:
            return None

    def brand(self) -> str | None:
        if self._brand is not None:
            return str(self._brand)
        else:
            return None

    def staff(self) -> list | None:
        if self._staff is not None:
            return list(self._staff)
        else:
            return None

if __name__ == "__main__":
    client = Client("Ark Computing")
    print(client.fullname())
