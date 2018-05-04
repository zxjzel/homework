#! /usr/bin/env python
# -*- coding:utf-8 -*-



"""
This is a sample text-only game that demonstrates the use of functions.
The game is called "Mudball" and the players take turns lobbing mudballs
at each other until someone gets hit.

http://programarcadegames.com/index.php?chapter=functions
"""

import math
import random
import logging
# 导入模块


class inputError(Exception):
    def raise_intutError(self):
        print('inputError : Type must be int')


logger = logging.getLogger('logger')
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
file_handler = logging.FileHandler('Mud_log.txt')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def print_instructions():
    """ This function prints the instructions. """

    # You can use the triple-quote string in a print statement to
    # print multiple lines.
    print("""
Welcome to Mudball! The idea is to hit the other player with a mudball.
Enter your angle (in degrees) and the amount of PSI to charge your gun
with.
        """)


def calculate_distance(psi, angle_in_degrees):
    """ Calculate the distance the mudball flies. """
    angle_in_radians = math.radians(angle_in_degrees)
    # 调用radians函数返回弧度制
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    # 计算距离

    return distance


def get_user_input(name):
    """ Get the user input for psi and angle. Return as a list of two
    numbers. """
    # Later on in the 'exceptions' chapter, we will learn how to modify
    # this code to not crash the game if the user types in something that
    # isn't a valid number.
    global psi
    global angle
    global str_psi
    while True:
        A = False
        try:
            str_psi = input(name + " charge the gun with how many psi? ")
            psi = float(str_psi)
            str_angle = input(name + " move the gun at what angle? ")
            angle = float(str_angle)
            logger.info(name + " charge the gun with how many psi? " + str_psi)
            logger.info(name + " move the gun at what angle? " + str_angle)
            A = True
        except(ValueError):
            IE = inputError()
            IE.raise_intutError()
            logger.error(name + " charge the gun with how many psi? " + str_psi)
            print()
            logger.error('inputError : Type must be int')
            print()
        if A:
            return psi, angle


def get_player_names():
    """ Get a list of names from the players. """
    print("Enter player names. Enter as many players as you like.")
    done = False
    players = []# 新建一个空列表
    while not done:
        player = input("Enter player (hit enter to quit): ")
        if len(player) > 0:
            players.append(player)# 如果输入的字符串不为空则加入列表中
        else:
            done = True #否则结束循环
    print()
    return players # 返回玩家名字的list


def process_player_turn(player_name, distance_apart):
    """ The code runs the turn for each player.
    If it returns False, keep going with the game.
    If it returns True, someone has won, so stop. """
    psi, angle = get_user_input(player_name)#序列解包等价于 psi = angel = get_user_input(player_name),调用get_user_input函数得到用户输入的psi 和 angel

    distance_mudball = calculate_distance(psi, angle)# 计算距离
    difference = distance_mudball - distance_apart # 计算用户输入的点和目标的差

    # By looking ahead to the chapter on print formatting, these
    # lines could be made to print the numbers is a nice formatted
    # manner.
    if difference > 1:
        logger.info('You went ' + str(difference) + ' yards too far!')
        print ('You went ' + str(difference) + ' yards too far!')

    elif difference < -1:
        logger.info("You were " + str(difference * -1) + ' yards too short!')
        print ("You were " + str(difference * -1) + ' yards too short!')

    else:
        logger.info('Hit!' + str(player_name) + 'wins!')
        print ('Hit!' + str(player_name) + 'wins!')
        return True

    print()
    return False


def main():
    """ Main program. """
    logger.info('---------------------Program is start-------------------------')
    print_instructions()
    player_names = get_player_names()
    logger.info('This is player_names' + str(player_names))
    distance_apart = random.randrange(50, 150) # 从（50，150）间随机返回一个值
    logger.info('distance_apart is ' + str(distance_apart))
    # Keep looking until someone wins
    done = False
    while not done:
        # Loop for each player
        for player_name in player_names:
            # Process their turn
            done = process_player_turn(player_name, distance_apart)
            # If someone won, 'break' out of this loop and end the game.
            if done:
                break
    logger.info('----------------------------end-------------------------------')


if __name__ == "__main__":
    main()