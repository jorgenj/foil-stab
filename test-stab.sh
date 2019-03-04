for KP in GFTT BRISK DENSE FAST HARRIS MSER ORB STAR SIFT SURF; do
	python3 -m vidstab --input iGP020067.avi --output stable_video-$KP.avi -k $KP -m 500
done
