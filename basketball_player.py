# -*- coding: utf-8 -*-
class PlayerStatistics:
    def __init__(self):
        self.ptspergame = 0
        self.count = 0
    def calculate_pointspergame(self, three_pointers, two_pointers):
        self.ptspergame = three_pointers + two_pointers
        print(f"The total points per game is {self.ptspergame}")
    def achieved_triple_double(self, assists, blocks, rebounds, steals):
        self.stats_list = [self.ptspergame, assists, blocks, rebounds, steals]
        for stat in self.stats_list:
            if stat >= 10:
                self.count += 1
        if self.count >= 3:
            print(f"Achieved Triple Double")
class BasketBallPlayer:
    def __init__(self, first_name, last_name, number):
        # automatically called when creating object of BasketBall Player class
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.game_stats = PlayerStatistics()
        self.greatest_player_of_all_time = ['Kobe Bryant', 'Lebron James', 
                                            'Michael Jordan','Stephen Curry']
    def greeting(self):
        print(f"My name is {self.first_name} {self.last_name} \
               My jersey number is {self.number}")
    def is_great_player(self):
        self.full_name = self.first_name + ' ' + self.last_name
        if self.full_name in self.greatest_player_of_all_time:
            print('You are a GOAT!!!')



Baller = BasketBallPlayer('Kobe', 'Bryant', 24)
Baller.game_stats.calculate_pointspergame(4,6)
Baller.is_great_player()
Baller.game_stats.achieved_triple_double(12, 5, 10, 4)