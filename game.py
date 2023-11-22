from random import randint


class WrongTypeValue(Exception):
    pass


class WrongCountValue(Exception):
    pass


def generate_unique_numbers(count, min_bound, max_bound):
    if count > max_bound - min_bound + 1:
        raise ValueError('Incorrect input parameters')
    ret = []
    while len(ret) < count:
        new = randint(min_bound, max_bound)
        if new not in ret:
            ret.append(new)
    return ret


class Card:

    def __init__(self):
        self._line_len = 26
        self._rows = 3
        self._cols = 9
        self._nums_in_row = 5
        self._data = None
        self._empty_num = 0
        self._crossed_num = -1

        uniques_count = self._nums_in_row * self._rows
        uniques = generate_unique_numbers(uniques_count, 1, 90)

        self._data = []
        for i in range(0, self._rows):
            tmp = sorted(uniques[self._nums_in_row * i: self._nums_in_row * (i + 1)])
            empty_nums_count = self._cols - self._nums_in_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self._empty_num)
            self._data += tmp

    def __str__(self):
        delimiter = '-' * self._line_len
        ret = delimiter + '\n'
        for index, num in enumerate(self._data):
            if num == self._empty_num:
                ret += '  '
            elif num == self._crossed_num:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self._cols == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter

    def __contains__(self, item):
        return item in self._data

    def cross_num(self, num):
        for index, item in enumerate(self._data):
            if item == num:
                self._data[index] = self._crossed_num
                return
        raise ValueError(f'Number not in card: {num}')

    def closed(self) -> bool:
        return set(self._data) == {self._empty_num, self._crossed_num}


class Game:

    def __init__(self):
        self._num_kegs = 90
        self._game_over = False
        self._line_len = 26
        self._gamers = None
        self._current = None
        self._counts = None
        self._kegs = generate_unique_numbers(self._num_kegs, 1, 90)
        self._current_keg = None

        self.run_game()

    @property
    def counts(self):
        if self._counts is None:
            self._counts = 0
        return self._counts

    @counts.setter
    def counts(self, count):
        if count.isdigit() and int(count) > 1:
            self._counts = int(count)
        else:
            raise WrongCountValue

    @property
    def new_gamer(self):
        if self._gamers is None:
            self._gamers = {}
        return self._gamers[self._current]

    @new_gamer.setter
    def new_gamer(self, user: dict):
        if self._gamers is None:
            self._gamers = {}
        if user['type'].isdigit() and 0 <= int(user['type']) <= 1:
            user['type'] = int(user['type'])
            self._gamers[len(self._gamers)] = user
        else:
            raise WrongTypeValue

    def add_gamers(self) -> None:
        self.counts = input('Введите количество игроков: ').strip()

        for num in range(self.counts):
            self.new_gamer = {
                'name': input(f'Введите имя {num + 1}-го игрока: ').strip(),
                'type': input(f'Выберите тип {num + 1}-го игрока (игрок/компьютер) (1/0): ').strip(),
                'card': Card(),
                'status': 0
            }
        print()

    def view_card(self):
        print(f'Новый бочонок: {self._current_keg} (осталось {len(self._kegs)})\n')
        for num in range(self.counts):
            self._current = num
            if self.new_gamer["status"] == 0:
                name = f' Карточка {self.new_gamer["name"]} '
                if not (len(name)/2).is_integer():
                    name += '-'
                line = f'{"-" * (int((self._line_len - len(name))/2))}'
                print(
                    f'{line}{name}{line}\n'
                    f'{self.new_gamer["card"]}\n'
                )

    def play_round(self) -> int:
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - user lose
        """
        self._current_keg = self._kegs.pop()
        self.view_card()
        for num in range(self.counts):
            self._current = num

            if self.new_gamer["status"] == 0:
                # print(f'type: {type(self.new_gamer["type"])}')
                if self.new_gamer["type"] == 1:
                    user_answer = input(f'Игрок: {self.new_gamer["name"]}. Зачеркнуть цифру? (y/n)').lower().strip()
                    if (
                            (user_answer == 'y' and not self._current_keg in self.new_gamer["card"])
                            or (user_answer != 'y' and self._current_keg in self.new_gamer["card"])
                    ):
                        self.new_gamer["status"] = 2
                        continue

                if self._current_keg in self.new_gamer["card"]:
                    self.new_gamer["card"].cross_num(self._current_keg)
                    if self.new_gamer["card"].closed():
                        self.new_gamer["status"] = 1
                        return 1

                self.new_gamer["status"] = 0

    def run_game(self):
        self.add_gamers()
        while True:
            result = self.play_round()
            if result == 1:
                print(f'User {self.new_gamer["name"]} - wins!!!')
                break


if __name__ == '__main__':
    Game()

