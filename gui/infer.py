import PySimpleGUI as sg


class Window:

    def __init__(self, size:tuple=(640, 480)):

        self.size = size
        self.font = "courier 10 pitch"

        # Creates the window
        self.create_window()

        # Enter infinite loop
        self._loop()

    def create_window(self):
        
        # Organize window layout
        self.layout = [
        [sg.Text(
            text="INFERENCE WITH YOLOV7",
            pad=((120, 0), (0, 70)),
            size=21, 
            text_color="black", 
            background_color="white", 
            justification="center",
            font=(self.font, 20, "bold"),
        )],
        [sg.Checkbox(
            text="Show output",
            pad=((5, 5), (0, 25)),
            background_color="white",
            font=(self.font, 12),
            key="show_output",
            text_color="black"),
        sg.Checkbox(
            text="Save output",
            pad=((5, 5), (0, 25)),
            background_color="white",
            font=(self.font, 12),
            key="save_output",
            text_color="black"),
        sg.Checkbox(
            text="Show FPS on video",
            pad=((5, 5), (0, 25)),
            background_color="white",
            font=(self.font, 12),
            key="show_fps",
            text_color="black")
        ],
        [sg.Text(
            text="Config. File", 
            background_color="white",
            text_color="black",
            pad=((0, 0), (0, 0)),
            font=(self.font, 12)), 
        sg.Input(
            default_text="",
            background_color="white",
            size=(35, 10),
            pad=((15, 5), (0, 0)),
            font=(self.font, 12),
            text_color="black",
            key="config_file",
            ),
        sg.FileBrowse(
            button_text="Browse",
            file_types=(("ALL Files", "*.yaml"),),
            button_color="black",
            font=(self.font, 12))],
        [sg.Text(
            text="Weights File", 
            background_color="white",
            pad=((0, 0), (15, 0)),
            text_color="black", 
            font=(self.font, 12)),
        sg.Input(
            default_text="",
            background_color="white",
            size=(35, 10),
            pad=((15, 10), (15, 0)),
            font=(self.font, 12),
            key="weights_file",
            text_color="black",
            ),
        sg.FileBrowse(
            button_text="Browse",
            file_types=(("ALL Files", "*.pth"),),
            button_color="black",
            pad=((0, 0), (15, 0)),
            font=(self.font, 12))],
        [sg.Text(
            text="Images/Video", 
            background_color="white",
            pad=((0, 0), (15, 0)),
            text_color="black",
            font=(self.font, 12)), 
        sg.Input(
            default_text="",
            background_color="white",
            size=(35, 10),
            pad=((15, 10), (15, 0)),
            font=(self.font, 12),
            key="input",
            text_color="black",
            ),
        sg.FileBrowse(
            button_text="Browse",
            file_types=(("ALL Files", "*.pth"),),
            button_color="black",
            pad=((0, 0), (15, 0)),
            font=(self.font, 12))],
        [sg.Button(
            button_text="RUN",
            size=(6, 2),
            pad=((250, 0), (70, 0)),
            font=(self.font, 18),
            button_color="green")]
        ]

        # Create window
        self.window = sg.Window(
            title="Yolov7 - Inferência",
            layout=self.layout,
            size=self.size,
            background_color="white",
        )

    def _loop(self):
        """Keeps the window opened 'till user closes it"""
        
        while True:
            event, values = self.window.read()
            if event is sg.WIN_CLOSED:
                break

            elif event == "RUN":
                print(dir(sg.popup_ok()))
                if not(values["config_file"]) or not(values["weights_file"]) or not(values["input"]):
                    sg.popup_ok(
                        "Cannot infer without config/weights/input data",
                        title="Error",
                        background_color="white",
                        text_color="black",
                        button_color="black",
                        keep_on_top=True,
                        font=(self.font, 12))
                    continue
                else:
                    pass


if __name__ == "__main__":
    window = Window()
