# anime_sub_switcher
To practise my cantonese, find cantonese dub videos, and replace the subs with english sub.

To get the file, I used youtube-dl and manually downloaded the video, in the future just extract the mu38 link from the url

For example for ktkkt top.
<iframe width="100%" height="100%" src="dplayer/dplayer.html?videourl=/play/13914-1-260.html,https://v4.szjal.cn/20200816/Pk8C9nha/index.m3u8,,13914,1,260" frameborder="0" border="0" marginwidth="0" marginheight="0" scrolling="no" allowfullscreen="allowfullscreen" mozallowfullscreen="mozallowfullscreen" msallowfullscreen="msallowfullscreen" oallowfullscreen="oallowfullscreen" webkitallowfullscreen="webkitallowfullscreen"></iframe>

To extract the audio stream without re-encoding:

ffmpeg -i input-video.avi -vn -acodec copy output-audio.aac

Then combine the old audio with the english sub

```bash
ffmpeg -i v.mp4 -i a.wav -c:v copy -map 0:v:0 -map 1:a:0 new.mp4
```