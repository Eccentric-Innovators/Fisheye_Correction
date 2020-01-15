import click

@click.group()
def cli():
	"""Capture images and videos and undistort fisheye images!"""
	pass

@cli.command()
@click.option('--src', help = 'Source of the video feed.', default = 0)
@click.option('--quality', help = 'Quality to use:\n\t-> 480p (default)\n\t-> 720p\n\t-> 1080p', default="480p")
@click.argument('dest', required = False, default = 'output_{}.png') #  help = 'File format and path to store the images in. {} will be incremented for each image.\nExample:\n\t\t./foldername/image_{}.png'
def capture(src, dest, quality):
	"""Capture images or videos"""
	from imgCapture import captureImg
	captureImg(src, dest, quality)

if __name__ == '__main__':
	cli()