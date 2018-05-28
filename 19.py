from random import randint, randrange
from abc import ABCMeta, abstractmethod

class Fighter(object, metaclass = ABCMeta):
    """战斗者"""

    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法

        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return (self._name)

    @property
    def hp(self):
        return (self._hp)

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return (self._hp > 0)

    @abstractmethod
    def attack(self, other):
        """
        攻击

        :param other: 被攻击的对象
        """
        pass


class bloodthirster():
    """饮血剑"""

    __slots__ = ('_name', '_attributes')

    def __init__(self):
        self._name = 'bloodthirster'
        self._attributes = 40

    def specail_attributes(self,other):
        other._hp += randint(0, 40) * 0.3

class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp', '_eq')

    def __init__(self, name, hp, mp, eq):
        """
        初始化方法

        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        :param eq: 装备
        """
        super().__init__(name, hp)
        self._mp = mp
        self._eq = eq

    def attack(self, other):
        other.hp -= (randint(15, 25) + self._eq._attributes)
        try:
            self._eq.specail_attributes(self)
        except:
            pass

    def huge_attack(self, other):
        """
        究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击

        :param others: 被攻击的群体

        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp

class Boss(Fighter):
    """大怪兽"""

    __slots__ = ('_name','_hp')

    def attack(self, other):
        other._hp -= randint(30,40)

    def heavy_attack(self, other):
        if self._hp <= 50:
            injury = randint(50,100)
            self._hp -= 5
            other._hp -= injury
        else:
            other._hp -= randint(30, 40)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp

e1 = bloodthirster()
c1 = Ultraman('ZXJ', 1000, 500, e1)
c2 = Boss('ZEL', 1500)
c1.attack(c2)
print(c1._hp,c2._hp)