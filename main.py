import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "HeaderBar example"
        self.set_titlebar(hb)

        grid = Gtk.Grid()
        label = Gtk.Label("Open")
        arrow = Gtk.Arrow(Gtk.ArrowType.UP, Gtk.ShadowType.NONE)
        button = Gtk.Button()
        button.connect("clicked", self.open_file)
        grid.attach(arrow, 0, 0, 1, 1)
        grid.attach(label, 1, 0, 1, 1)
        grid.show_all()
        button.add(grid)
        hb.pack_end(button)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(button)

        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(button)

        hb.pack_start(box)
        self.main_grid()
        self.scrollable_treelist
        self.show_all()

    def main_grid(self):
        sample = [{"Hello", "World", "!"}]
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)
        store = Gtk.ListStore(str, str, str)
        self.add_items(sample, store)

        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(["test", "test", "test"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        self.buttons = list()
        for bottom_buttons in ["Java", "C", "C++", "Python", "None"]:
            button = Gtk.Button(bottom_buttons)
            self.buttons.append(button)

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)

        self.scrollable_treelist.add(self.treeview)


    def add_items(self, items, store):
        for item in items:
            store.append(list(item))
        self.current_filter_language = None
        self.language_filter = store.filter_new()
        self.language_filter.set_visible_func(self.language_filter_func)

    def language_filter_func(self, model, iter, data):
        """Tests if the language in the row is the one in the filter"""
        if self.current_filter_language is None or self.current_filter_language == "None":
            return True
        else:
            return model[iter][2] == self.current_filter_language

    def on_button_click(self, widget):
        print("Hello World")

    def open_file(self, widget):
        dialog = Gtk.FileChooserDialog("Select a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        else:
            print("cancel clicked")
        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
