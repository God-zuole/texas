import random

class PokerUtil():
    def __init__(self):
        # 定义牌的花色和数值
        self.suits = ['♥', '♦', '♠', '♣']  # Hearts, Diamonds, Clubs, Spades
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']  # 2 to Ace

        # 创建一副完整的牌
        self.deck = [f"{suit}{rank}" for suit in self.suits for rank in self.ranks]

    def deal_cards(self, num_players):
        """随机发牌给n个玩家，每个玩家两张牌，并发五张公共牌"""
        random.shuffle(self.deck)  # 打乱牌堆
        hands = []
        for _ in range(num_players):
            hand = [self.deck.pop() for _ in range(2)]  # 每个玩家发两张牌
            hands.append(hand)
        community_cards = [self.deck.pop() for _ in range(5)]  # 发五张公共牌
        return hands, community_cards

# # 示例：给4个玩家发牌
# num_players = 23
# player_hands, community_cards = deal_cards(num_players)

# # 打印结果
# for i, hand in enumerate(player_hands):
#     print(f"Player {i+1}: {hand}")
# print(f"Community Cards: {community_cards}")
