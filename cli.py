from argparse import ArgumentParser


parser = ArgumentParser(description="An adder program")
parser.add_argument("x", type=int, help="The first number to add")
parser.add_argument("y", type=int, help="The second number to add.")

args = parser.parse_args()

z = args.x + args.y
print(f"{args.x} + {args.y} = {z}")