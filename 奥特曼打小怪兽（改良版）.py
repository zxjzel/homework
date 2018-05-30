from abc import ABCMeta, abstractmethod
from random import randint, randrange
import logging


"""
改良版：
        新建了一个装备抽象类；
        增加了装备，有的装备带有特殊属性
        增加了一个Boss，带有重击技能，
        游戏开始时给奥特曼和大怪兽分别随机选择一件装备
        奥特曼先与小怪兽战斗，等到小怪兽死后再与Boss决斗
"""


class Fighter(object, metaclass=ABCMeta):
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
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

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
                    temp.hp -= (randint(10, 15) * (1 + self._eq._attributes))
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
            '魔法值: %d\n' % self._mp +\
            '装备了：{}\n'.format(self._eq._name)


class Boss(Fighter):
    """大怪兽"""

    __slots__ = ('_name','_hp' ,'_eq')

    def __init__(self, name, hp, eq):
        super().__init__(name, hp)
        self._eq = eq

    def attack(self, other):
        other._hp -= (randint(30,40) + self._eq._attributes)

    def heavy_attack(self, other):
        if self._hp <= 50:
            injury = randint(50,100)
            self._hp -= 5
            other._hp -= injury
        else:
            other._hp -= randint(30, 40)

    def __str__(self):
        if __name__ == '__main__':
            return '~~~%s大怪兽~~~\n' % self._name + \
                '生命值: %d\n' % self._hp + \
                '装备了：{}\n' .format(self._eq._name)


class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


class B_F_Sword(Equipment):
    """暴风大剑"""

    __slots__ = ('_name', '_attributes')

    def __init__(self):
        self._name = '暴风大剑'
        self._attributes = 10

    def specail_attributes(self,other):
        pass


class bloodthirster(Equipment):
    """饮血剑"""

    __slots__ = ('_name', '_attributes')

    def __init__(self):
        self._name = '饮血剑'
        self._attributes = 40

    def specail_attributes(self,other):
        restore = randint(0, 40) * 0.3
        other._hp += restore
        print('%s触发了装备的特殊技能.' % (other._name))
        print('{}恢复了{}hp'.format(other._name, restore))


class abyssal_scepter(Equipment):
    """虚空之杖"""

    __slots__ = ('_name', '_attributes')

    def __init__(self):
        self._name = '虚空之杖'
        self._attributes = 0.2

    def specail_attributes(self, other, another):
        pass


class archangels_staff(Equipment):
    """大天使之杖"""

    __slots__ = ('_name', '_attributes')

    def __init__(self):
        self._name = '大天使之杖'
        self._attributes = 0.3

    def specail_attributes(self, other, another):
        another._hp = 0
        print('%s触发了装备的特殊技能.' % (other._name))
        print('{}使用大天使之杖秒杀了{}'.format(other._name, another._name))


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


def display_info(ultraman, monsters, boss):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')
    print(boss)


def choose_equipments(eqs):
    """随机选择一件装备"""
    a = randint(1, len(eqs))
    if a == 1:
        return (eqs[0])
    else:
        return (eqs[1])


def main():
    p_eqs = [bloodthirster(), B_F_Sword()]
    m_eqs = [abyssal_scepter(), archangels_staff()]
    eq1 = choose_equipments(m_eqs)
    eq2 = choose_equipments(p_eqs)
    u = Ultraman('张新健', 2500, 120, eq1)
    m1 = Monster('舒小玲', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    b = Boss('失了智', 1000, eq2)
    ms = [m1, m2, m3]
    ms1 = [m1, m2, m3, b]
    fight_round = 1
    while u.alive and is_any_alive(ms1):
        print('========第%02d回合========' % fight_round)
        if is_any_alive(ms):
            m = select_alive_one(ms)  # 选中一只小怪兽
        else:
            m = b
        skill = randint(1, 11)   # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        elif skill == 10:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        else:
            u._eq.specail_attributes(u, m)
        if m.alive > 0 and m in ms:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        elif b.hp > 0:
            skill = randint(1, 10)
            if skill <= 5:
                print('%s普通攻击攻击打了%s.' % (b.name, u.name))
                b.attack(u)
            elif 5 < skill <= 8:
                print('%s举起武器重击了%s.' % (b.name, u.name))
                b.heavy_attack(u)
            else:
                b.attack(u)
                b._eq.specail_attributes(b)

        display_info(u, ms, b)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('怪兽们胜利!')


if __name__ == '__main__':
    main()