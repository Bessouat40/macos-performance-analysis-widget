# import rumps
# import psutil

# class SystemStatsApp(rumps.App):
#     def __init__(self):
#         super(SystemStatsApp, self).__init__("System Stats")
#         self.menu = ["CPU Usage", "Memory Usage", "Disk Usage", "Network Stats", "Battery"]

#     @rumps.timer(2)  # Met à jour toutes les 2 secondes
#     def update_stats(self, _):
#         # Mise à jour de l'utilisation du CPU
#         self.menu["CPU Usage"].title = f"CPU Usage: {psutil.cpu_percent()}%"

#         # Mise à jour de l'utilisation de la mémoire
#         memory = psutil.virtual_memory()
#         self.menu["Memory Usage"].title = f"Memory Usage: {memory.percent}% (Used: {memory.used / (1024**3):.2f} GB, Free: {memory.free / (1024**3):.2f} GB)"

#         # Mise à jour de l'utilisation du disque (ajustez le chemin si nécessaire)
#         disk_usage = psutil.disk_usage('/')
#         self.menu["Disk Usage"].title = f"Disk Usage: {disk_usage.percent}% (Used: {disk_usage.used / (1024**3):.2f} GB, Free: {disk_usage.free / (1024**3):.2f} GB)"

#         # Mise à jour des statistiques réseau
#         net_io = psutil.net_io_counters()
#         self.menu["Network Stats"].title = f"Network: Sent {net_io.bytes_sent / (1024**3):.2f} GB - Recv {net_io.bytes_recv / (1024**3):.2f} GB"

#         # Mise à jour de l'état de la batterie (peut ne pas fonctionner sur tous les Mac)
#         if hasattr(psutil, "sensors_battery"):
#             battery = psutil.sensors_battery()
#             if battery:
#                 self.menu["Battery"].title = f"Battery: {battery.percent}% Charged"

# if __name__ == "__main__":
#     SystemStatsApp().run()

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

