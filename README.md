# anime_sub_switcher
To practise my cantonese, find cantonese dub videos, and replace the subs with english sub.

To get the file, I used youtube-dl and manually downloaded the video, in the future just extract the mu38 link from the url

For example for ktkkt top.

<iframe width="100%" height="100%" src="dplayer/dplayer.html?videourl=/play/13914-1-260.html,https://v4.szjal.cn/20200816/Pk8C9nha/index.m3u8,,13914,1,260" frameborder="0" border="0" marginwidth="0" marginheight="0" scrolling="no" allowfullscreen="allowfullscreen" mozallowfullscreen="mozallowfullscreen" msallowfullscreen="msallowfullscreen" oallowfullscreen="oallowfullscreen" webkitallowfullscreen="webkitallowfullscreen"></iframe>


To ensure the two video streams match.

```bash
python calculator.py
```

To ensure calculate the correct time ratio
```
ffmpeg -i sample.mp4 -filter:v "setpts=PTS*1.0176067318263677" good.mp4
```

To extract the audio stream without re-encoding:

ffmpeg -i input-video.avi -vn -acodec copy output-audio.aac

Then combine the old audio with the english sub

```bash
ffmpeg -i v.mp4 -i a.wav -c:v copy -map 0:v:0 -map 1:a:0 new.mp4
```

To add video offset
```bash
ffmpeg -i "new.mp4" -itsoffset 25.351 -i "new.mp4" -map 0:v -map 1:a -c copy "movie-audio-delayed.mp4"
```

Do an animated movie https://www.ktkkt.top/play/15560-0-0.html

demon slayer the infinity train

# https://nyaa.si/view/1382745


Slow down/ speed up video

https://trac.ffmpeg.org/wiki/How%20to%20speed%20up%20/%20slow%20down%20a%20video

https://dubdb.fandom.com/wiki/%E8%9C%98%E8%9B%9B%E4%BF%A0%EF%BC%9A%E9%A3%9B%E8%BA%8D%E8%9C%98%E8%9B%9B%E5%AE%87%E5%AE%99

To sync audio think I need to do counting, if it gets out of sync, then I need to adjust the time offset. Time its just a certain part of the ending getting sped up disproportionately.


Cant scale this, not sure what the site is doing, think one part is sped up.

For demon slayer kktkk at

3.8 seconds

gogoanime anime stream at
32.1 seconds

to remove audio from video

ffmpeg -i tft_gapped_by_yuumi.mp4 -vcodec copy -an  tft_gapped_by_yuumi_no_audio.mp4
