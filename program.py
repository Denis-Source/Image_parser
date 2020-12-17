from interface_elements import Interface
from tkinter import filedialog as fd
from urllib.request import urlopen
from pars import Parser


class Program:
    def __init__(self):
        self.i = Interface()
        self.dir = ""
        self.elements = self.i.interface_elements_dict

    def pack_elements(self):
        for key in self.elements.keys():
            elem = self.elements[key]["element"]
            params = self.elements[key]["params"]
            elem.pack(**params)
            if "list" in key:
                list_params = self.elements[key]["list_params"]
                list_items = self.elements[key]["list_items"]
                for list_item in list_items:
                    elem.insert(0, list_item)
                elem.select_set(0)
                elem.configure(**list_params)

    def select_dir(self, event):
        self.dir = fd.askdirectory()

    def get_time(self, event):
        res = urlopen('http://just-the-time.appspot.com/')
        time = res.read().strip()
        self.elements["time_l"]["element"]["text"] = time.decode("utf-8")

    def start(self, event):
        p = Parser(
            self.elements["url_e"]["element"].get(),
            int(self.elements["depth_e"]["element"].get()),
            self.dir,
        ).find_all_links()
        p.save_images()

    def mainloop(self):
        self.elements["select_dir_b"]["element"].bind("<Button-1>", self.select_dir)
        self.elements["start_b"]["element"].bind("<Button-1>", self.start)
        self.elements["time_b"]["element"].bind("<Button-1>", self.get_time)
        self.pack_elements()
        self.i.root.mainloop()
