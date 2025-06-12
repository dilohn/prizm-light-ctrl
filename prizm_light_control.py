import requests

class PrizmLightingController:
    def __init__(self, controller_ip):
        self.base_url = f"http://{controller_ip}"

    def send_command(self, endpoint, params=None):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()
            print(f"Command sent: {response.url}")
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error sending command: {e}")
            return None

    def set_led_state(self, location, state):
        return self.send_command("_led", {"location": location, "state": state})

    def set_all_leds(self, state):
        return self.send_command("_allled", {"state": state})

    def set_color(self, location, hex_color):
        return self.send_command("_color", {"location": location, "color": hex_color})

    def set_brightness(self, location, increments):
        return self.send_command("_bright", {"location": location, "increments": increments})

    def dim_brightness(self, location, increments):
        return self.send_command("_dim", {"location": location, "increments": increments})

    def pulse_color(self, location, hex_color=None):
        params = {"location": location}
        if hex_color:
            params["color"] = hex_color
        return self.send_command("_color_pulse", params)

    def apply_mood(self, mood_name):
        return self.send_command("_mood", {"mood": mood_name})

    def trigger_startup_event(self):
        return self.send_command("_trigger_startup_event")

    def refresh_config(self):
        return self.send_command("_refresh_config")

# Example usage
if __name__ == "__main__":
    controller_ip = "172.20.10.42"  # Replace with your controller IP
    prizm = PrizmLightingController(controller_ip)

    # Control examples
    prizm.set_led_state("vip", "on")
    prizm.set_color("group1", "FFAA00FF")  # Orange with white
    prizm.set_brightness("floor", 3)
    prizm.pulse_color("group1", "00FF00FF")  # Green pulse
    prizm.apply_mood("relax")
    prizm.refresh_config()
