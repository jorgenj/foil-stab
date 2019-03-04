import ffmpy
ff = ffmpy.FFmpeg(
    inputs={'GP020067.MP4': None},
    outputs={'iGP020067.avi': None}
)
ff.run()
