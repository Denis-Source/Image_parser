import tkinter as tk

from int_sett import IntSett


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg=IntSett.bg_color)
        self.interface_elements_dict = {
            "main_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 24, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Image Parser"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "url_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Enter URL:"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "url_e": {
                "element":
                    tk.Entry(
                        self.root,
                        font=(IntSett.font, 20, "bold"),
                        fg=IntSett.text_color,
                        bg=IntSett.bg_color,
                        width=15
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "depth_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Enter depth:"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "depth_e": {
                "element":
                    tk.Entry(
                        self.root,
                        font=(IntSett.font, 20, "bold"),
                        fg=IntSett.text_color,
                        bg=IntSett.bg_color,
                        width=4
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "select_dir_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Select directory",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "start_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Start",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "info_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                    ),
                "params":
                    {
                        "padx": 10,
                        "pady": 10,
                    }
            },
            "time_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Get time",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "time_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                    ),
                "params":
                    {
                        "padx": 10,
                        "pady": 10,
                    }
            }
        }
