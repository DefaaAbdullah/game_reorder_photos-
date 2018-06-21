import webbrowser
"""You got it! When we create the instance brad, the init function inside the class Turtle gets called."""
class PHOTOS():
	def __init__(udacity,  STRING_PHOTOS):
		udacity.STRING_PHOTOS = STRING_PHOTOS
	def show_trialer(udacity):
		webbrowser.open(udacity.STRING_PHOTOS)