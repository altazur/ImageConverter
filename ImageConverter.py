import argparse

from PIL import Image

parser = argparse.ArgumentParser(description="Convert, resize image")
parser.add_argument("-C", type=str)  # Convert to what format
parser.add_argument("-F", type=str)  # File input name
parser.add_argument("-O", type=str)  # File output name
parser.add_argument("-R", type=str)  # Resize to what size
args = parser.parse_args()

if args.C:
    with Image.open(f"./{args.F}", "r") as input_image:
        output_image = input_image.copy()
        output_image.save(f"./{args.O}", format=args.C.upper())

if args.R:
    with Image.open(f"./{args.F}", "r") as input_image:
        output_image = input_image.copy()
        size = tuple([int(x) for x in args.R.split(",")])
        output_image.thumbnail(size)
        output_image.save(f"./{args.O}")
