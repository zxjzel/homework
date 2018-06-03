import logging


logger = logging.getLogger('logger')
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
file_handler = logging.FileHandler('rectangle_log.txt',encoding='utf-8')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.formatter = formatter
console_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


class CanNotRectangle(Exception):
    pass


class CanNotSquare(Exception):
    pass


class Rectangle:
    def __init__(self):
        while True:
            try:
                self.x1 = float(input('输入X1:'))
                self.y1 = float(input('输入Y1:'))
                self.x2 = float(input('输入X2:'))
                self.y2 = float(input('输入Y2:'))
                logger.debug('(' + str(self.x1) + ',' + str(self.y1) + ')' + ' and ' + '(' + str(self.x2) + ',' + str(self.y2) + ')')
                if self.x1 == self.x2 or self.y1 == self.y2:
                    raise CanNotRectangle()
                else:
                    break
            except(CanNotRectangle):
                logger.error('X1不能等于X2 或 Y1不能等于Y2')

    def width(self):
        return (abs(self.x1 - self.x2))

    def height(self):
        return (abs(self.y2 - self.y1))

    def area(self):
        return (self.width() * self.height())

    def circumference(self):
        return (2 * (self.height() + self.width()))


class Square(Rectangle):
    def __init__(self):
        self.x1 = float(input('输入X1:'))
        self.y1 = float(input('输入Y1:'))
        self.x2 = float(input('输入X2:'))
        self.y2 = float(input('输入Y2:'))
        logger.debug('(' + str(self.x1) + ',' + str(self.y1) + ')' + ' and ' + '(' + str(self.x2) + ',' + str(self.y2) + ')')

    def Judge_Square(self):
        if self.width() != self.height():
            try:
                raise CanNotSquare
            except(CanNotSquare):
                logger.info('不能构成正方形')
                return False
        else:
            return True


r1 = Rectangle()
print()
logger.info('r1的长和宽分别为：{},{}'.format(r1.width(), r1.height()))
r2 = Rectangle()
print()
logger.info('r2的长和宽分别为：{},{}'.format(r2.width(), r2.height()))
while True:
    s1 = Square()
    if s1.Judge_Square():
        break
logger.info('s1的边长为：{}'.format(s1.width()))
logger.info('s1的周长为：{}'.format(s1.circumference()))
logger.info('s2的面积为：{}'.format(s1.area()))
while True:
    s2 = Square()
    if s2.Judge_Square():
        break
print()
logger.info('s2的边长为：{}'.format(s2.width()))
logger.info('s2的周长为：{}'.format(s2.circumference()))
logger.info('s2的面积为：{}'.format(s2.area()))