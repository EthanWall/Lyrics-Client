import sys

import lyricsgenius

from subprocess import Popen, PIPE

genius = lyricsgenius.Genius(
    "5B99PPmNQQeH9v6_pjvXoaR7TyOvxT6NTnVl7rwB4EDlAAkGyDWXEO42o-jI4yDG")


def get_playing_track():
    track_info = ["Unknown", "Unknown"]

    if sys.platform == "darwin":
        script = '''
            tell application "System Events"
                tell process "TIDAL"
                    tell (1st window whose value of attribute "AXTitle" is not null)
                        return value of attribute "AXTitle"
                    end tell
                end tell
            end tell
            '''  # noqa: E501

        p = Popen(["osascript", "-"], stdin=PIPE, stdout=PIPE, stderr=PIPE,
                  universal_newlines=True)
        stdout, stderr = p.communicate(script)

        if " - " in stdout:
            # A track is playing
            track_info = stdout.rstrip().rsplit(" - ", 1)
        elif stdout == "TIDAL":
            # TIDAL is paused
            pass

    return track_info


def get_lyrics(info):
    track = genius.search_song(info[0], info[1])
    return track.lyrics
