import tkinter as tk
from utils import image_util 
from utils import poker_util
from utils import compare_util
from tkinter import font

class Main_Page():
    def __init__(self, root):
        self.root = root
        self.ImageUtil = image_util.ImageUtil(root)
        self.timer_id = None

    def init_poker(self):
        # 初始化一些东西
        global hands
        init_poker = poker_util.PokerUtil()
        compare_hand = compare_util.CompareUtil()
        num_players = 10    
        hands= [[] for _ in range(num_players)]
        player_hands, community_cards = init_poker.deal_cards(num_players)
        self.hand_cards_show(player_hands)
        for i in range(len(player_hands)):
            seven_cards = community_cards + player_hands[i]
            cards = [compare_hand.parse_card(card) for card in seven_cards]
            best_hand = compare_hand.best_five_cards(cards)
            best_hand_rank = compare_hand.poker_hand_rank(best_hand)
            hands[i] = best_hand
        self.community_cards_show(community_cards)
    
    def community_cards_show(self, community_cards):
        i = 0
        for community_card in community_cards:
            # community_cards_coordinate = (community_cards_coordinates[i][0], community_cards_coordinates[i][1])
            self.poker_show(community_card, community_cards_coordinates[i])
            i+=1
    
    def hand_cards_show(self, player_hands):
        i = 0
        for player_hand in player_hands:
            seat_coordinate = seat_coordinates[i]
            offset = 37
            seat_coordinate_1 = (seat_coordinate[0], seat_coordinate[1])
            seat_coordinate_2 = (seat_coordinate[0] + offset, seat_coordinate[1])
            self.poker_show(player_hand[0], seat_coordinate_1)
            self.poker_show(player_hand[1], seat_coordinate_2)
            i+=1

    def poker_show(self, card, coordinate):
        suit = card[0]
        value = card[1]
        suit_size_dic = {
            "♥": (8, 8),
            "♠": (9, 9),
            "♦": (9, 9),
            "♣": (8, 8),
            "s": (34, 50)
        }
        suit_size = suit_size_dic.get(suit)
        value_size = 13
        suit_coordinate = (coordinate[0] + 6, coordinate[1] + 6)
        value_coordinate = (coordinate[0] + 11, coordinate[1] + 14)
        flip_coordinate = (coordinate[0] + 20, coordinate[1] + 35)
        image_path = "./icons/" + suit + ".png"
        self.ImageUtil.image_show("./icons/s.png", suit_size_dic.get("s"), suit+value+"_borders", coordinate)
        custom_font = font.Font(family="Helvetica", size=value_size, weight="bold", slant="italic")
        value_label = tk.Label(self.root, text=value, font=custom_font)
        value_label.place(x=value_coordinate[0], y=value_coordinate[1])
        self.ImageUtil.image_show(image_path, suit_size, suit+value, suit_coordinate)
        self.ImageUtil.image_show_flip(image_path, suit_size, suit+value+"_flip", flip_coordinate)

    def coordinates_init(self):
        # seat_coordinates_init
        global seat_coordinates
        seat_coordinates = [(160,290), (330,290), (530,290), (650,230), (650,90), (530,23), (330,23), (160,23), (10,90), (10,230)]
        
        # community_cards_coordinates_init
        x_index = 244; space = 52; y_index = 155
        global community_cards_coordinates
        community_cards_coordinates = [(x_index + i * space, y_index) for i in range(5)]

        # winner_hands_coordinates_init
        x_index = 244; space = 44; y_index_up = 110; y_index_down = 190
        global winner_hands_coordinates_up
        global winner_hands_coordinates_down
        winner_hands_coordinates_up = [(x_index + i * space, y_index) for i in range(5)]
        winner_hands_coordinates_down = [(x_index + i * space, y_index) for i in range(5)]

        # winner_coordinates_init
        global winner_coordinates
        x18 = 210; x26 = 350; x35 = 510; y123 = 236; x45 = 590; y40 = 200; y59 = 125; y678 = 86; x90 = 108
        winner_coordinates = [(x18,y123), (x26,y123), (x35,y123), (x45,y40), (x45,y59), (x35,y678), (x26,y678), (x18,y678), (x90,y59), (x90,y40)]

        # hands_power_init
        global hands_power_coordinates
        hands_power_coordinates = [(100, 100), (100, 200)]

    def hands_rank(self):
        global power_table
        compare_hand = compare_util.CompareUtil()
        power_table = compare_hand.hands_power(hands)
        rank_table = compare_hand.hands_rank(hands)
        winners = []
        for i in range(len(rank_table)):
            if rank_table[i] == 1:
                winners.append(i)
        for winner in winners:
            winner_image_path = "./icons/win.png"
            self.ImageUtil.image_show(winner_image_path, (35, 35), "winner", winner_coordinates[winner])
        self.winner_hands_show(winners)

    def winner_hands_show(self, winners):
        power_table
        power_dic = {
            "8": "同花顺",
            "7": "炸弹",
            "6": "葫芦",
            "5": "同花",
            "4": "顺子",
            "3": "三条",
            "2": "两对",
            "1": "一对",
            "0": "单张高牌",
        }
        if (len(winners)==1):
            winner_power = power_dic.get(power_table[winners[0]][0])
        else:
            winner_power = "玩家" + str(winners) + "平分"
        winner_hands = hands[winners[0]]
        value = winner_hands[0]


        custom_font = font.Font(family="Helvetica", size=13, weight="bold", slant="italic")
        value_label = tk.Label(self.root, text=value, font=custom_font)
        value_label.place(x=hands_power_coordinates[0][0], y=hands_power_coordinates[0][1])


        for winner_hand in winner_hands:
            poker_show(winner_hand, winner_hands_coordinates_up[i])
            poker_show(winner_hand, winner_hands_coordinates_down[i])

    def setup_auto_click(self, time, func):
        # 设置定时器，time秒后执行func函数(10000->10s)
        self.timer_id = self.root.after(time, func)

    def new_round(self):
        if self.timer_id is not None:
            self.root.after_cancel(timer_id)
        self.clear_labels()

    def clear_labels(self):
        # 遍历所有子Widget
        for widget in self.root.winfo_children():
            # 检查Widget是否为Label
            if isinstance(widget, tk.Label):
                # 使用pack_forget()或grid_forget()或place_forget()来隐藏Label
                # widget.pack_forget()  # 如果使用pack布局
                # widget.grid_forget()  # 如果使用grid布局
                # widget.place_forget()  # 如果使用place布局
                # 或者使用destroy()来完全删除Label
                if widget.winfo_name() == "background":
                    pass
                else:
                    widget.destroy()

    def toggle_hand():
        for widget in root.winfo_children():
        # 检查Widget是否为Label
            if isinstance(widget, tk.Label):
                if widget.winfo_name() == "background":
                    widget.destroy()
                    return
                # else:
        image_show_lower("./icons/background.jpg", None, "background", [-35, -215])

    def open_new_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.geometry("400x360")  # 设置窗口大小为300x200
        new_window.resizable(False, False)  # 禁止用户改变窗口的大小
        new_window.title("Bouns Time")
        label = tk.Label(new_window, text="这是一个新的窗口")
        new_window.pack()

    def ceshi(self):
        pass

    def table_ui_show(self):
        # init_something
        self.coordinates_init()

        self.ImageUtil.image_show("./icons/background.jpg", None, "background", [-35, -215])


        button0 = tk.Button(self.root, text="开牌", command=self.init_poker)
        button0.place(x=180, y=150)

        button1 = tk.Button(self.root, text="new window", command=self.open_new_window)
        button1.place(x=180, y=180)

        button2 = tk.Button(self.root, text="预留2", command=self.ceshi)
        button2.place(x=180, y=210)

        button3 = tk.Button(self.root, text="新的一局", command=self.new_round)
        button3.place(x=500, y=150)

        button4 = tk.Button(self.root, text="rank", command=self.hands_rank)
        button4.place(x=500, y=180)

        button5 = tk.Button(self.root, text="测试", command=self.ceshi)
        button5.place(x=500, y=210)