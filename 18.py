from abc import ABCMeta, abstractmethod
from random import randint, randrange


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


class Equipment(object, metaclass = ABCMeta):
    """装备"""
    __slots__ = ('_name', '_attributes')

    def __init__(self,_name, _attributes):
        self._name = _name
        self._attributes = _attributes

    @abstractmethod
    def specail_attributes(self):
        pass


class B_F_Sword(Equipment):
    """ 暴风大剑"""

    __slots__ = ('_name', '_attributes')

    def __init__(self):
        self._name = 'B_F_Sword'
        self._attributes = 10


class bloodthirster(Equipment):
    """饮血剑"""

    __slots__ = ('_name', '_attributes')

    def __init__(self):
        self._name = 'bloodthirster'
        self._attributes = 40

    def specail_attributes(self,other):
        other._hp += randint(0, 40) * 0.3


class abyssal_scepter(Equipment):
    """虚空之杖"""

    __slots__ = ('_name', '_attributes')

    def __init__(self):
        self._name = 'abyssal_scepter'
        self._attributes = 0.2


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
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = (injury * self._eq._attributes)if injury >= 50 else (50 * self._eq._attributes)
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


class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp', '_eq')

    def __init__(self, name, hp, eq):
        """
        初始化方法

        :param name: 名字
        :param hp: 生命值
        :param eq: 装备
        """
        super().__init__(name, hp)
        self._eq = eq

    def attack(self, other):
        other.hp -= (randint(10, 20) + self._eq._attributes)
        try:
            self._eq.specail_attributes(self)
        except:
            pass

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


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


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('舒小玲', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)   # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()