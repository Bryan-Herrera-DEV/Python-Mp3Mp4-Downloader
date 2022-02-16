from __future__ import unicode_literals
import youtube_dl

class Download(object):
    def __init__(self, url, save_path, quality, playlist=False):
        self.url = url
        self.save_path = save_path
        self.qualities = {"Best": "1411",
                        "Semi": "320",
                        "Worst": "128"}
        self.quality = self.qualities[quality]
        self.playlist = playlist


    def mp3_download(self):
        print(self.quality)
        # para m4 se usa 140 como calidad
        if self.quality == "140":
            print("Sera m4a")
            opts = {
                "verbose": True,
                "fixup"  : "detect_or_warn",
                "format" : "bestaudio[ext=m4a]",
                "postprocessors" : [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec"  : "m4a",
                    "preferredquality"  : self.quality
                }],
                "extractaudio": False,
                "outtmpl"     : self.save_path + "/%(title)s.%(ext)s",
                "noplaylist"  : self.playlist
            }
            download_object = youtube_dl.YoutubeDL(opts)
            download_object.download([self.url])
        else:
            opts = {
                "verbose": False,
                "fixup"  : "detect_or_warn",
                "format" : "bestaudio/best",
                "postprocessors" : [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec"  : "mp3",
                    "preferredquality": self.quality
                }],
                "extractaudio": True,
                "outtmpl"     : self.save_path + "/%(title)s.%(ext)s",
                "noplaylist"  : self.playlist
            }
            download_object = youtube_dl.YoutubeDL(opts)
            download_object.download([self.url])


    def mp4_download(self):
        opts = {
            "verbose": False,
            "fixup"  : "detect_or_warn",
            "format" : "bestaudio/best",
            "postprocessors" : [{
                "key": "FFmpegVideoConverter",
                "preferredcodec"  : "mp4",
            }],
            "outtmpl"     : self.save_path + "/%(title)s.%(ext)s",
            "noplaylist"  : self.playlist
        }
        download_object = youtube_dl.YoutubeDL(opts)
        download_object.download([self.url])