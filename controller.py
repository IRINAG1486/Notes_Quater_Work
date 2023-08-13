import model
import text
import view


def start():
    app_notes = model.Notes()
    filter_ = None
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                notes = app_notes.load()
                view.print_notes(notes, text.load_error, filter_)
                # view.print_message(text.load_successful)
            case 2:
                app_notes._save()
                view.print_message(text.full_save_successful)
            case 3:
                app_notes._open()
                notes = app_notes.load()
                index = view.input_index(text.index_open_note, notes, text.load_error)
                view.print_a_note(notes[index - 1], text.load_error)
            case 4:
                note = view.input_note(text.new_note, text.cancel_input)
                if note:
                    name = app_notes.add(note)
                    view.print_message(text.new_note_successful(name))
            case 5:
                notes = app_notes.load()
                index = view.input_index(text.index_del_note, notes, text.load_error)
                name = app_notes.dell_note(index)
                view.print_message(text.del_note(name))
            case 6:
                notes = app_notes.load()
                index = view.input_index(text.index_change_note, notes, text.load_error)
                if not index:
                    continue
                name = view.input_note(text.new_note, text.cancel_input)
                change_note = app_notes.change_note(index, name)
                view.print_message(text.change_note)
            case 7:
                notes = app_notes.load()
                info = view.input_find_note()
                search_note = app_notes.find_note(notes, info, text.find_note_error)
                view.print_notes(search_note, text.find_note_error)
            case 8:
                view.print_message(text.close_app_notes)
                break
