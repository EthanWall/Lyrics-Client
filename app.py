import toga
from toga.style.pack import COLUMN, Pack

import songs


class Client(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        self.lyric_view = toga.Label("None")

        box = toga.Box(
            children=[
                toga.ScrollContainer(
                    content=self.lyric_view,
                    style=Pack(
                        flex=1
                    ),
                    horizontal=False
                ),
                toga.Button("Reload", on_press=self.reload)
            ],
            style=Pack(
                direction=COLUMN
            )
        )

        self.main_window.content = box

        # Show the main window
        self.main_window.show()

        self.reload()

    def reload(self, widget=None):
        lyrics = songs.get_lyrics(songs.get_playing_track())
        self.lyric_view.text = lyrics


def main():
    return Client("Lyrics Client", "ethanwall.lyricsclient")


if __name__ == "__main__":
    main().main_loop()
