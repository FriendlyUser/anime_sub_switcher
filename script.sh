ffmpeg -i dsm_canton.mp4 -f mp3 -ab 192000 -vn audio.mp3
ffmpeg -i dsm_en.mp4 -i audio.mp3 -c copy -map 0:v:0 -map 1:a:0 -shortest new.mp4
ffmpeg -i new.mp4 -itsoffset 28.35 -i new.mp4 -map 0:v:0 -map 1:a:0 -c copy  dsm_en_final.mp4