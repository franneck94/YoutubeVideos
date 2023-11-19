import argparse
import random
import time

random.seed(int(time.time()))

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--number_users', type=int, required=True)
    parser.add_argument('--message', type=str, required=False, default="Dice roll")
    args = parser.parse_args()
    number_users = args.number_users
    message = args.message
    dice_roll = random.randint(1, number_users)
    print("{}: {}".format(message, dice_roll))

if __name__ == "__main__":
    main()
