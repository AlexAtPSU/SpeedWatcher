# SpeedWatcher
This is a python script that speeds up the parts of the video that don't have any dialogue.


Using moviepy and pysrt, a video is then seperated by the times of the subtitles (assuming the subtitles have no wierd timing that messes it up) and then speeds up individual clips and combining it into one.

# How to Use
Running the speedwatcher.py, the next argument is either a folder of video files and subtitles followed by the multiplier for the speedup. The formats for file names are based on what I've seen and does not work for every wording. (usually S01E01 for season/episode)
For individual files or files that don't match the subtitle name: The first argument is the video, followed by the speed, and then the subtitle file. 

Note: 
This is before I looked into the python arguments parser library.
For now only .srt and maybe .ass files work as far as I know.

