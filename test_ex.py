import pytest

from ex import ex_funcs

# PDPM

def greet(name):
    return f"Hello, {name}!"


# テスト用の関数呼び出し
if __name__ == "__main__":
    print(greet("World"))
