import json
import os
from datetime import datetime
from config import NOTES_FILE


class NotesStorage:
    def __init__(self):
        self.notes = []
        self.load()

    def load(self):
        if os.path.exists(NOTES_FILE):
            try:
                with open(NOTES_FILE, "r", encoding="utf-8") as f:
                    self.notes = json.load(f)
            except:
                self.notes = []

    def save(self):
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def create(self, title, content):
        note = {
            "title": title,
            "content": content,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        self.notes.insert(0, note)
        self.save()
        return 0

    def update(self, index, title, content):
        if 0 <= index < len(self.notes):
            self.notes[index] = {
                "title": title,
                "content": content,
                "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            self.save()

    def delete(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self.save()

    def get(self, index):
        if 0 <= index < len(self.notes):
            return self.notes[index]
        return None