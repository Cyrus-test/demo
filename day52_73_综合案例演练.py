class Game(object):

    top_score = 0

    def __init__(self, play_name):
        self.play_name = play_name


    @staticmethod
    def play_help():
        print("游戏帮助：请充值10000无敌")

    @classmethod
    def show_top(cls):
        print("历史最高纪录： %d " % cls.top_score)

    def star_game(self):
        print("%s 游戏开始了 " % self.play_name)

# 1.查看游戏帮助信息
Game.play_help()

# 2.查看历史最高分
Game.show_top()

# 3.创建游戏对象
game = Game("小明")
game.star_game()



