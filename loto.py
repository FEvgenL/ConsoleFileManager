import random


class Card:

    def __init__(self, name_card):
        self.name_card = name_card

    @staticmethod
    def gen_nums_lst(init_num: int, fin_num: int, lst_len: int, sort_lst=False) -> list:
        nums_lst = [num for num in range(init_num, fin_num)]
        nums_lst_selection = random.sample(nums_lst, lst_len)
        return sorted(nums_lst_selection) if sort_lst else nums_lst_selection

    @staticmethod
    def creating_card_header(name_card: str) -> str:
        if name_card == 'компьютер':
            name_part_1 = 'Карточка компьютера'
            name_part_2 = '-' * ((26 - len(name_part_1)) // 2)
            card_title = f'{name_part_2}{name_part_1}{name_part_2}'
        else:
            name_part_1 = 'Карточка игрока: '
            name_part_2 = '-' * ((26 - len(name_part_1) - len(name_card)) // 2)
            card_title = f'{name_part_2}{name_part_1}{name_card}{name_part_2}'
        return card_title

    def creating_nums_in_card(self):
        pos_nums_in_card = []
        nums_in_card = []
        count = 0

        # Генерация списка цифр для карты
        num_lst = self.gen_nums_lst(1, 91, 15)
        # Герерация списка с позициями цифр в карте
        pos_num = [self.gen_nums_lst(0, 9, 5, sort_lst=True) for _ in range(3)]

        # Позиции цифр в карте по строчкам
        for i in range(3):
            k = i * 9
            for item in pos_num[i]:
                pos_nums_in_card.append(item + k)

        # Список с цифрами карты
        for j in range(27):
            try:
                if pos_nums_in_card[count] == j:
                    nums_in_card.append(num_lst[count])
                    count += 1
                else:
                    nums_in_card.append(-1)
            except IndexError:
                nums_in_card.append(-1)

        return nums_in_card

    def drawing_card(self, nums):
        nums_str = []
        creating_card_header = self.creating_card_header(self.name_card)
        # Вывод на экран заголовка карты
        print(creating_card_header)
        # Преобразование списка из чисел в список из строк
        for i in range(len(nums)):
            if 0 < nums[i] < 10:
                nums_str.append(' ' + str(nums[i]))
            elif nums[i] == -1:
                nums_str.append('  ')
            elif nums[i] == -2:
                nums_str.append(' -')
            else:
                nums_str.append(str(nums[i]))
        # Вывод на экран срок с цифрами карты
        for i in range(3): print(' '.join(nums_str[i * 9: (i + 1) * 9]), sep='\n')
        print('-' * len(creating_card_header))

    def updating_nums(self, barrel: int, nums_in_card: list) -> list:
        index = nums_in_card.index(barrel)
        nums_in_card.pop(index)
        nums_in_card.insert(index, -2)
        return nums_in_card


if __name__ == '__main__':

    player_name = 'Евгений'
    barrels = [num for num in range(1, 91)]
    player_1 = Card('компьютер')
    player_2 = Card(player_name)
    nums_in_card_1 = player_1.creating_nums_in_card()
    nums_in_card_2 = player_2.creating_nums_in_card()

    while True:
        barrel = barrels.pop(random.randint(0, len(barrels) - 1))
        print(f'Новый бочонок: {barrel} (осталось {len(barrels)})')
        player_1.drawing_card(nums_in_card_1)
        player_2.drawing_card(nums_in_card_2)
        answer = input('Зачеркнуть цифру? (д/н): ')

        if barrel in nums_in_card_1:
            nums_in_card_1 = player_1.updating_nums(barrel, nums_in_card_1)

        if answer == 'д' and barrel in nums_in_card_2:
            nums_in_card_2 = player_2.updating_nums(barrel, nums_in_card_2)
        elif answer == 'н' and barrel not in nums_in_card_2:
            continue
        else:
            print(f'Игрок {player_name} проиграл')
            break

