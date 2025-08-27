from dataclasses import dataclass
import re

# Interner Speicher (stateless, nur zur Laufzeit)
todos: list["Todo"] = []

@dataclass
class Todo:
    title: str
    isCompleted: bool = False

def bbbify(text: str) -> str:
    """Ersetzt 'b' → 'bbb' und 'B' → 'Bbb'."""
    return re.sub(r"[bB]", lambda m: "Bbb" if m.group(0).isupper() else "bbb", text)

def add(title: str) -> None:
    title = bbbify(title)
    todos.append(Todo(title=title))

def get_all() -> list["Todo"]:
    return todos

def toggle(index: int) -> None:
    if 0 <= index < len(todos):
        todos[index].isCompleted = not todos[index].isCompleted
