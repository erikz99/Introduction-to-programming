import random


class Player:
    dices = []
    current_level_necessary = 1
    current_level_combinations = 1
    points = 0

    def __init__(self, name):
        self.name = name

    def combination_summator_necessary(self):

        print("Заровенте на", self.name, "са:")
        print(self.dices)

        counter = 0
        for number in self.dices:
            if number == self.current_level_necessary:
                counter += 1
        self.points += (counter - 3)*self.current_level_necessary

        print("Текущо ниво:", self.current_level_necessary)
        print("Точките на", self.name, "са", self.points)
        self.current_level_necessary += 1

    def combination_summator_combinations(self):

        print("Заровенте на", self.name, "са:")
        print(self.dices)


        if self.current_level_combinations == 1 or self.current_level_combinations == 3 or self.current_level_combinations == 4:
            needed_count_equals = self.current_level_combinations
            if self.current_level_combinations == 1:
                needed_count_equals = 2
            for number in self.dices:
                if self.dices.count(number) >= needed_count_equals:
                    self.points += (needed_count_equals)*number
                    break

        elif self.current_level_combinations == 2:
            numbers = []
            counter = 0
            for number in self.dices:
                if self.dices.count(number) == self.current_level_combinations:
                    counter+=1
                    numbers.append(number)
            if counter==4:
                numbers = list(set(numbers))
                self.points += 2*(numbers[0]) + 2*(numbers[1])

        elif self.current_level_combinations == 5:
            duo_number = 0;
            trio_number = 0;
            for number in self.dices:
                if self.dices.count(number)==2:
                    duo_number = number
                if self.dices.count(number) == 3:
                    trio_number=number
            if duo_number > 0 and trio_number > 0:
                self.points += 2*duo_number + 3*trio_number

        elif self.current_level_combinations == 6:
            if 1 and 2 and 3 and 4 and 5 in self.dices:
                self.points+=15

        elif self.current_level_combinations == 7:
            if 2 and 3 and 4 and 5 and 6 in self.dices:
                self.points+=20

        elif self.current_level_combinations == 8:
            for number in self.dices:
                self.points += number

        else:
            for number in self.dices:
                self.points += number
            self.points +=50

        print("Текущо ниво комбинации :", self.current_level_combinations)
        print("Точките на", self.name, "са", self.points)
        self.current_level_combinations += 1

    def roll(self):
        self.dices = []
        for x in range(1, 6):
            self.dices.append(random.randint(1, 6))


class User(Player):
    def rollNecessary(self):

        super().roll()

        for y in range(1, 3):
            print(self.dices)
            new_dice_index = input("Изберете позиция на заровете, които искате да хвърлите отново разделени с интервал. Ако искате да запазите заровете въведете 0")
            if new_dice_index != "0":
                new_dice_index = new_dice_index.replace(" ", "")

                for dice_index in new_dice_index:
                    real_index = int(dice_index) - 1
                    if real_index in range(0, 5):
                        self.dices[real_index] = random.randint(1, 6)
            else:
                break

        self.combination_summator_necessary()

    def rollCombinations(self):

        super().roll()

        for y in range(1, 3):
            print(self.dices)
            new_dice_index = input("Изберете позиция на заровете, които искате да хвърлите отново разделени с интервал. Ако искате да запазите заровете въведете 0")
            if new_dice_index != "0":
                new_dice_index = new_dice_index.replace(" ", "")

                for dice_index in new_dice_index:
                    real_index = int(dice_index) - 1
                    if real_index in range(0, 5):
                        self.dices[real_index] = random.randint(1, 6)
            else:
                break

        self.combination_summator_combinations()

class Computer(Player):
    def rollNecessary(self):

        super().roll()
        for y in range(1, 3):
            print(self.dices)
            for index, dice in enumerate(self.dices):
                if dice != self.current_level_necessary:
                    self.dices[index] = random.randint(1, 6)

        self.combination_summator_necessary()

    def rollCombinations(self):

        super().roll()
        if self.current_level_combinations <= 4:
            needed_count_equals = self.current_level_combinations
            if self.current_level_combinations == 1:
                needed_count_equals = 2
            for y in range(1, 3):
                for index, dice in enumerate(self.dices):
                    if self.dices.count(dice) == needed_count_equals:
                        pass
                    else:
                        self.dices[index] = random.randint(1, 6)

        elif self.current_level_combinations == 5:
            for y in range(1, 3):
                for index, dice in enumerate(self.dices):
                    if self.dices.count(dice) == 2 or self.dices.count(dice) == 3:
                        pass
                    else:
                        self.dices[index] = random.randint(1, 6)

        elif self.current_level_combinations >=8:
            pass

        else:
            for y in range(1, 3):
                for index, dice in enumerate(self.dices):
                    if dice == 6 - self.current_level_combinations % 6:
                        self.dices[index] = random.randint(1, 6)
                    elif self.dices.count(dice) == 1:
                        pass
                    else:
                        self.dices[index] = random.randint(1, 6)

        self.combination_summator_combinations()


class Board:

    players = []
    a = 0
    b = 0

    def add_player(self, player):
        self.players.append(player)

    def start(self):
        while not self.is_necessary_finished():
            for player in self.players:
                player.rollNecessary()

        max_points = -100
        winners = []
        for player in self.players:
            if player.points > max_points:
                winners = []
                max_points = player.points
                winners.append(player.name)
            elif player.points == max_points:
                winners.append(player.name)

        if len(winners) == 1:
            print("Победителят в задължителната част е", winners[0])
        else:
            print ("Победителите в задължителната част са:", ",".join(winners))

        while not self.is_game_finished():
            for player in self.players:
                player.rollCombinations()

        max_points = -100
        winners = []
        for player in self.players:
            if player.points > max_points:
                winners = []
                max_points = player.points
                winners.append(player.name)
            elif player.points == max_points:
                winners.append(player.name)

        if len(winners) == 1:
            print("Победителят е", winners[0])
        else:
            print("Победителите са:", ",".join(winners))


    def is_necessary_finished(self):
        self.a += 1
        return self.a == 7

    def is_game_finished(self):
        self.b +=1
        return self.b == 10



player1 = User('Иванчо')
player2 = Computer('Компютър1')
player3 = Computer('Компютър2')
board = Board()
board.add_player(player1)
board.add_player(player2)
board.add_player(player3)
board.start()
