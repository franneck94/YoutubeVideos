import argparse
import random
import time

random.seed(int(time.time()))

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--number_users', type=int, required=True)
    args = parser.parse_args()
    number_users = args.number_users
    dice_roll = random.randint(1, number_users)
    print(dice_roll)

if __name__ == "__main__":
    main()
