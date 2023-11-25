import pyautogui
import gi

from scenarios.scenario_one import ScenarioOneData, run_scenario_one
from scenarios.scenario_two import ScenarioTwoData, run_scenario_two

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file("resources/window.ui")

        button = builder.get_object("button_begin_test_1")
        button.connect("clicked", self.begin_test_1)
        button = builder.get_object("button_begin_test_2")
        button.connect("clicked", self.begin_test_2)

        self.entry_manufacturer = builder.get_object("entry_manufacturer")
        self.entry_screen_size = builder.get_object("entry_screen_size")
        self.entry_screen_resolution = builder.get_object("entry_screen_resolution")

        self.win = builder.get_object("main_window")
        self.win.set_application(self)
        self.win.present()

    def begin_test_1(self, _button):
        print("tests firing")

        data: ScenarioOneData = ScenarioOneData(
            self.entry_manufacturer.get_text(),
            self.entry_screen_size.get_text(),
            self.entry_screen_resolution.get_text(),
        )

        if data.is_valid():
            run_scenario_one(data)
        else:
            print("Invalid data")

    def begin_test_2(self, _button):
        print("tests firing")

        data: ScenarioTwoData = ScenarioTwoData(
            self.entry_manufacturer.get_text(),
        )

        if data.is_valid():
            run_scenario_two(data)
        else:
            print("Invalid data")


if __name__ == '__main__':
    print(pyautogui.size())

    css_provider = Gtk.CssProvider()
    css_provider.load_from_path('resources/style.css')
    Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    app = MyApp(application_id="org.shiishiji.integration3")
    app.run(None)


