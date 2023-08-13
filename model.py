from uuid import UUID, uuid4

import text
import view
import csv
from datetime import datetime


class Notes:

    def __init__(self, path: str = 'notes.csv'):
        self.app_notes: list[dict[str, str, str, datetime]] = []
        self.filtered_notes: list[dict[str, str, str, datetime]] = []
        self.filter = filter_all_time
        self.path = path
        self._open()

    def _open(self):
        try:
            with open(self.path, 'r', encoding='UTF-8', newline='') as file:
                reader = csv.DictReader(file, delimiter=";")
                data = list(reader)
        except FileNotFoundError:
            data = []
        self.app_notes = []
        # print(data)
        for note in data:
            self.app_notes.append(note)
        self.filtered_notes = self.filter(self.app_notes)

    def _save(self):
        # data = []
        # for note in self.app_notes:
        #     note = ';'.join([value for value in note.values()])
        #     data.append(note)
        with open(self.path, 'w', encoding='UTF-8', newline='') as file:
            header = ["id", "title", "body", "timestamp"]
            writer = csv.DictWriter(file, delimiter=";", fieldnames=header)
            writer.writeheader()
            for note in self.app_notes:
                writer.writerow(note)
            # file.write('\n'.join(data))

    def add(self, note: dict[str, str, str, datetime]):
        note["id"] = str(uuid4())
        print(note)
        self.app_notes.append(note)
        self._save()
        return note.get('title')

    def load(self):
        return self.filter(self.app_notes)

    def dell_note(self, index: int):
        title = self.app_notes.pop(index - 1).get('title')
        self._save()
        return title

    def find_note(self, note: list[dict[str, str, datetime]], message: str, error):
        data: list[dict[str, str, str, datetime]] = []
        for note in self.app_notes:
            for value in note.values():
                if message.lower() in value.lower():
                    data.append(note)
                    return data

    def change_note(self, index: int, new_note: dict):
        id_ = self.filtered_notes[index-1]['id']
        for note in self.app_notes:
            if id_ == note.get('id'):
                note['title'] = new_note.get('title', note.get('title'))
                note['body'] = new_note.get('body', note.get('body'))
                note['timestamp'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                self._save()
                return note.get('title')

def filter_all_time(notes):
    return notes


def filter_today(notes):
    today = datetime.today()
    return [note for note in notes if note["timestamp"].date() == today.date()]


def filter_this_week(notes):
    today = datetime.today()
    return [note for note in notes if note["timestamp"].date() >= today - datetime.timedelta(days=7)]


def filter_this_month(notes):
    this_month = datetime.today().month
    return [note for note in notes if note["timestamp"].month == this_month]


def filter_input_dates(notes, start_date, end_date):
    # Filter notes for the given date range
    return [note for note in notes if start_date <= note["timestamp"] <= end_date]


def get_filter_function(filter_choice):
    filter_mapping = {
        1: filter_all_time,
        2: filter_today,
        3: filter_this_week,
        4: filter_this_month,
        5: lambda notes: filter_input_dates(notes, view.input_dates()),
    }
    return filter_mapping.get(filter_choice)


