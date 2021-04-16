from __future__ import unicode_literals
import os
import sys
from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx
import pysrt
from progress import progress
import pygame
# desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


class SpeedSilBySubs:
    def __init__ (self, speedfactor):
        # self.videofile = videofile
        # self.subtitlefile = subtitlefile
        self.speedfactor = float(speedfactor)

    def speed(self, videofile, subtitlefile):
        video = VideoFileClip(videofile)
        audioclip = video.audio
        subs = pysrt.open(subtitlefile)
        def getsec(time):
            return ((time.hour * 60 + time.minute) * 60 + time.second) + (time.microsecond /(1000 * 1000))

        # print(subs)
        times = []
        new_subs = pysrt.SubRipFile()
        for sub in subs:
            times.append(getsec(sub.start.to_time()))
            times.append(getsec(sub.end.to_time()))
        finalclip = None
        clips = []
        l = len(times)
        bul = True
        while bul == True:
            bul = False
            for ind,obj in enumerate(times):
                if ind + 1 < 2:
                    if obj >= times[ind + 1]:
                        times.pop(ind + 1)
                        if times[ind] > times[ind+1]:
                            times.pop(ind + 1)
                        else:
                            times.pop(ind)
                        l = l -2
                        bul = True
        times.insert(0, 0)
        duration_change = 0
        times.append(video.duration)
        for ind,obj in enumerate(times):
            progress(ind +1, len(times), status="Speeding clips x" + str(self.speedfactor))
            if ind + 1 < len(times):
                if video.duration >= times[ind +1] and video.duration >= obj and obj >= 0 and obj >= 0 and obj < times[ind+1]:
                    clip = video.subclip(obj,times[ind+1])
                    if ind % 2 == 0 and obj != times[ind+1]:
                        clips.append(vfx.speedx(clip, factor=self.speedfactor).fx(afx.volumex, 0.4))
                        duration_change = duration_change + (clip.duration - clips[-1].duration)
                    else:
                        clips.append(clip)
                        part = subs.slice(starts_after={'milliseconds':(obj * 1000) -10}, ends_before={'milliseconds':(times[ind + 1] *1000) +10})
                        part.shift(seconds=(-1 * duration_change))
                        for sub in part:
                            new_subs.append(sub)
                    # clips[-1].preview()
                        # print(part)

        print("\nConcatenation")
        finalclip = concatenate_videoclips(clips)
        print("New Length: ", finalclip.duration)
        new_subs.save(videofile[:-4]+"-"+str(self.speedfactor)+"x-speeded.srt", encoding='utf-8')
        finalclip.write_videofile(videofile[:-4]+"-"+str(self.speedfactor)+"x-speeded.mp4")
        return (video.duration, finalclip.duration)
