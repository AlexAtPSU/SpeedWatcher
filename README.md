# SpeedWatcher
This is a python script that speeds up the parts of the video that don't have any dialogue.<br>
Just a fun project for watching movies and series faster.<br>
Example: By speeding up the parts without plot using this script, I watched an <b>8 hour series in 2.5 hours.</b>
<br><br>
Using moviepy and pysrt, a video is then seperated by the times of the subtitles (assuming the subtitles have no wierd timing that messes it up) and then speeds up individual clips and combining it into one.
<br>
# How to Use
Running the speedwatcher.py, the next argument is either a folder of video files and subtitles followed by the multiplier for the speedup. The formats for file names are based on what I've seen and does not work for every wording. (usually S01E01 for season/episode)<br>
For individual files or files that don't match the subtitle name: The first argument is the video, followed by the speed, and then the subtitle file. 
<br><br>
Note: <br>
This is before I looked into the python arguments parser library.<br>
For now only .srt and maybe .ass files work as far as I know.<br>

