import text
from datetime import datetime
from typing import Callable, Optional


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


# функция для вывода сообщений
def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_notes(notes: list[dict[str, str, str, datetime]], error: str, filter_: Optional[Callable] = None):
    if notes:
        print('\n' + '=' * 80)
        if filter_:
            notes = filter_(notes)
        for i, note in enumerate(notes, 1):
            # print(f'{i} . {note.get("title")} | {note.get("body")} | {note.get("date")}')
            print(
                f'{i:>3}. {note.get("title"):<20.20} | {note.get("body"):<20.20} | {str(note.get("timestamp")):>20.20}')
            if i == note.__len__():
                print('=' * 70 + '\n')
            else:
                print('-' * 70 + '\n')
    else:
        print_message(error)


def print_a_note(note: dict[str, str, str, datetime], error: str):
    if note:
        print('\n' + '-' * 80)
        print(f'{note.get("title"):<30.30} | {note.get("timestamp"):>20.20}')
        print(note["body"])
        print('-' * 70 + '\n')
    else:
        print_message(error)


def input_note(message: str, cansel: str) -> dict:
    note = {}
    print(message)

    for key, value in text.input_note.items():
        data = input(value)
        if data:
            note[key] = data
        else:
            print_message(text.cancel_input)
            return {}
    date_ = input_date(text.input_date)
    note['timestamp'] = date_
    return note


def input_index(message: str, note: list, error: str):
    print_notes(note, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(note) + 1:
            return int(index)


def input_find_note():
    message = input(text.find_note_info)
    return message


def input_date(message=text.input_date):
    date = input(message)
    if date:
        date = datetime.strptime(date, "%d.%m.%Y %H:%M")
    else:
        date = datetime.now()
    return date


def input_dates():
    date_filter = input(text.date_choices)
    return None
