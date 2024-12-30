import rumps
import subprocess
import threading
import time
import sys
import os


class PingStatusApp(rumps.App):
    def __init__(self):
        super(PingStatusApp, self).__init__("Ping Status", title="🔄")
        self.host = "8.8.8.8"  # Default to Google DNS
        self.menu = ["Settings", "Quit"]
        self.running = True
        self.start_ping_monitoring()

    def start_ping_monitoring(self):
        self.ping_thread = threading.Thread(target=self.monitor_ping)
        self.ping_thread.daemon = (
            True  # Make thread daemon so it exits when main thread exits
        )
        self.ping_thread.start()

    def monitor_ping(self):
        while self.running:
            try:
                # Run ping command and capture output
                output = subprocess.run(
                    ["ping", "-c", "1", self.host],
                    capture_output=True,
                    text=True,
                    timeout=2,
                )

                if output.returncode == 0:
                    # Extract ping time from output
                    time_str = output.stdout.split("time=")[1].split(" ")[0]
                    ping_time = float(time_str)

                    # Update icon based on ping time
                    if ping_time < 50:
                        self.title = f"✅ {ping_time:.1f}ms"
                    elif ping_time < 100:
                        self.title = f"🟡 {ping_time:.1f}ms"
                    else:
                        self.title = f"🔴 {ping_time:.1f}ms"
                else:
                    self.title = "❌ Error"
            except Exception as e:
                print(f"Error: {str(e)}")  # Add logging
                self.title = "❌ Error"

            time.sleep(5)

    @rumps.clicked("Settings")
    def settings(self, _):
        response = rumps.Window(
            "Enter host to ping (e.g., 8.8.8.8 or google.com)",
            "Settings",
            default_text=self.host,
        ).run()

        if response.clicked:
            self.host = response.text

    @rumps.clicked("Quit")
    def quit(self, _):
        self.running = False
        rumps.quit_application()


if __name__ == "__main__":
    try:
        PingStatusApp().run()
    except Exception as e:
        print(f"Application Error: {str(e)}")  # Add logging
