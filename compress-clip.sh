ffmpeg -i "/Users/jorgenj/Pictures/GoPro/2015-01-01/HERO5 Session 1/GP020067.MP4" \
	 -s 640x480 \
	-b:v 1024k \
	-vcodec mpeg1video \
	-ss 30 \
	-t 60 \
	-acodec copy short-GP020067.avi
