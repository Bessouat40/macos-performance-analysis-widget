
import psutil
import rumps

memory = psutil.virtual_memory()
print('memory : ', memory)
print('memory : ', [mem / 1024 ** 3 for mem in memory])

@rumps.timer(2)
def update_stats(self, _):
    memory = psutil.virtual_memory()
    self.menu["Memory Usage"].title = f"Memory Usage: {memory.percent}% (Used: {memory.used / (1024**3):.2f} GB, Free: {memory.free / (1024**3):.2f} GB)"