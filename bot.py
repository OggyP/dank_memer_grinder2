# import win32gui
import asyncio

import yaml
from yaml.loader import SafeLoader


class Bot:
    def __init__(self):
        self.focused = False
        self.config = self.parse_config()

        self.loop = asyncio.get_event_loop()

        # self.loop.create_task(self.check_discord_window())
        for command_data in self.config['commands']:
            self.loop.create_task(self.run_command(command_data))

        self.loop.run_forever()
        

    @staticmethod
    def parse_config():
        with open('config.yml') as f:
            config = yaml.load(f, Loader=SafeLoader)
            print(config)
        return config

    # async def check_discord_window(self):
    #     while True:
    #         w = win32gui

    #         active_window = str(w.GetWindowText(w.GetForegroundWindow()))
    #         active_window = active_window.split(" ")
    #         if active_window[-1] == "Discord":
    #             self.focused = True
    #         else:
    #             self.focused = False

    #         await asyncio.sleep(0.5)

    async def run_command(self, command_data):
        while True:
            # if self.focused:
            print(command_data.keys())
