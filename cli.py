from argparse import ArgumentParser
from app import App


parser = ArgumentParser(description="An Image Sharpener Program")
parser.add_argument("image")

args = parser.parse_args()

app = App()
app.load_image_from_path(args.image)
app.save_sharpened_image("sharpened.png")
