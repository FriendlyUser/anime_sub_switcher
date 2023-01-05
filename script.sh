ffmpeg -i inu_canton.mp4 -f mp3 -ab 192000 -vn audio.mp3
ffmpeg -i video.mp4 -i audio.mp3 -c copy -map 0:v:0 -map 1:a:0 -shortest new.mp4
ffmpeg -i new.mp4 -itsoffset 12.69 -i new.mp4 -map 0:v:0 -map 1:a:0 -c copy  inu_final_done.mp4