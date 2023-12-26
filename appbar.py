import rumps
import psutil

class ConstantMenuBarApp(rumps.App):
    def __init__(self):
        super(ConstantMenuBarApp, self).__init__("", menu=[])
        self.set_up_timer()

    def set_up_timer(self):
        self.timer = rumps.Timer(self.on_tick, 2)
        self.timer.start()

    def on_tick(self, _):
        memory = psutil.virtual_memory()
        self.title = f"Mem: {memory.percent}% | Used: {memory.used / (1024**3):.2f} GB | Inactive Mem : {memory.inactive / (1024**3):.2f} GB"

if __name__ == "__main__":
    ConstantMenuBarApp().run()

