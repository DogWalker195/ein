from typing import Any

def ein(msg: str = "", intype: type | None = None, valuemsg: str = "Invalid Input") -> Any:
    while True:
        try:
            in_str: str = input(msg)
            if intype is None:
                return in_str
            return intype(in_str)
        except ValueError:
            print(valuemsg)