import customtkinter as ctk
from config import *


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, storage, on_new, on_edit, on_delete):
        super().__init__(parent, width=260, fg_color=purple_frame)
        self.storage = storage
        self.on_new = on_new
        self.on_edit = on_edit
        self.on_delete = on_delete
        self.active_note = None

        self.grid_propagate(False)

        ctk.CTkLabel(self, 
            text="Main Character Notes", font=ctk.CTkFont(size=20, weight="bold"),
            text_color=purple_text).pack(pady=(15, 10))

        ctk.CTkButton(self, 
            text="+ New note", font=ctk.CTkFont(size=13), height=35, fg_color=purple_accent, hover_color=purple_hov_sel,
            command=self.on_new).pack(fill="x", padx=12, pady=(0, 10))

        self.list_container = ctk.CTkScrollableFrame(self, fg_color=purple_frame)
        self.list_container.pack(fill="both", expand=True, padx=10, pady=5)

        self.render()

    def render(self):
        for w in self.list_container.winfo_children():
            w.destroy()

        notes = self.storage.notes

        if not notes:
            ctk.CTkLabel(self.list_container,
                text="No saved notes.\n Click 'New note' to create one.",
                text_color="#a688c5", font=ctk.CTkFont(size=12)).pack(pady=40)
            return

        for i, note in enumerate(notes):
            frame = ctk.CTkFrame(self.list_container, fg_color=purple_frame)
            frame.pack(fill="x", pady=4, padx=5)

            if i == self.active_note:
                frame.configure(fg_color=purple_hov_sel, border_width=2, border_color=purple_bright)

            frame.bind("<Button-1>", lambda e, idx=i: self._select(idx))

            title = note["title"].strip() or "Untitled"
            lbl = ctk.CTkLabel(frame, text=title, font=ctk.CTkFont(size=13, weight="bold"), anchor="w", text_color="white")
            lbl.pack(fill="x", padx=10, pady=(8, 2))
            lbl.bind("<Button-1>", lambda e, idx=i: self._select(idx))

            preview = note["content"].replace("\n", " ")[:35]
            if len(note["content"]) > 35:
                preview += "..."

            sub = ctk.CTkLabel(frame, text=preview or " ", font=ctk.CTkFont(size=11), text_color="#a688c5", anchor="w")
            sub.pack(fill="x", padx=10, pady=(0, 2))
            sub.bind("<Button-1>", lambda e, idx=i: self._select(idx))

            bottom = ctk.CTkFrame(frame, fg_color="transparent")
            bottom.pack(fill="x", padx=10, pady=(0, 6))

            ctk.CTkLabel(bottom, 
                text=note.get("date", ""), font=ctk.CTkFont(size=10), 
                text_color="#7a5c94").pack(side="left")

            ctk.CTkButton(bottom, 
                text="🗑", width=28, height=22, fg_color="transparent", hover_color="#8B0000",
                font=ctk.CTkFont(size=12), command=lambda idx=i: self.on_delete(idx)).pack(side="right")

    def _select(self, index):
        self.active_note = index
        self.render()
        self.on_edit(index)

    def set_active(self, index):
        self.active_note = index
        self.render()

    def clear_active(self):
        self.active_note = None
        self.render()