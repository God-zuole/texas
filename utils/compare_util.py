class CompareUtil():
    def __init__(self):
        self.suit = "suit"

    def parse_card(self, card):
        """解析一张牌，返回数值和花色"""
        suit, value = card[:-1], card[-1]
        return {'value': {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[value], 'suit': suit}

    def poker_hand_rank(self, hand):
        """识别并返回牌型和牌的数值"""
        if hand == 0:
            return (-1, -1)
        
        values = [card['value'] for card in hand]
        suits = [card['suit'] for card in hand]
        is_straight = len(set(values)) == 5 and max(values) - min(values) == 4
        is_flush = len(set(suits)) == 1
        value_counts = {v: values.count(v) for v in set(values)}
        is_four_of_a_kind = 4 in value_counts.values()
        is_full_house = 3 in value_counts.values() and 2 in value_counts.values()
        is_three_of_a_kind = 3 in value_counts.values()
        is_two_pair = list(value_counts.values()).count(2) == 2
        is_pair = 2 in value_counts.values()
        is_fold = max(values) == 0

        if is_flush and is_straight:
            return (8, max(values))
        elif is_four_of_a_kind:
            quadruple = [v for v, count in value_counts.items() if count == 4]
            single = [v for v, count in value_counts.items() if count == 1]
            ans = quadruple + single
            return (7, ans)
        elif is_full_house:
            triple = [v for v, count in value_counts.items() if count == 3]
            pairs = [v for v, count in value_counts.items() if count == 2]
            ans = triple + pairs
            return (6, ans)
        elif is_flush:
            return (5, sorted(values, reverse=True))
        elif is_straight:
            return (4, max(values))
        elif is_three_of_a_kind:
            triple = [v for v, count in value_counts.items() if count == 3]
            single = [v for v, count in value_counts.items() if count == 1]
            ans = triple + sorted(single, reverse=True)
            return (3, ans)
        elif is_two_pair:
            pairs = [v for v, count in value_counts.items() if count == 2]
            single = [v for v, count in value_counts.items() if count == 1]
            ans = sorted(pairs, reverse=True) + single
            return (2, ans)
        elif is_pair:
            pairs = [v for v, count in value_counts.items() if count == 2]
            single = [v for v, count in value_counts.items() if count == 1]
            ans = pairs + sorted(single, reverse=True)
            return (1, ans)
        else:
            return (0, sorted(values, reverse=True))

    def poker_hand_type(self, hand):
        """识别并返回牌型和牌的数值"""
        hand_type = hand[0]
        if hand_type == 8:
            return "同花顺"
        elif hand_type == 7:
            return "炸弹"
        elif hand_type == 6:
            return "葫芦"
        elif hand_type == 5:
            return "同花"
        elif hand_type == 4:
            return "顺子"
        elif hand_type == 3:
            return "三条"
        elif hand_type == 2:
            return "两对"
        elif hand_type == 1:
            return "一对"
        elif hand_type == 0:
            return "单张高牌"
        else:
            return "错的牌型"

    def hands_power(self, hands):
        """返回每组牌的牌力大小"""
        power_table = []
        for hand in hands:
            poker_power = self.poker_hand_rank(hand)
            power_table.append(poker_power)
        return power_table

    def get_sorted_positions(self, arr):
        # 创建一个索引列表，与原数组长度相同
        index_list = list(range(len(arr)))

        # 根据数组的值对索引列表进行排序，reverse=True表示从大到小排序
        sorted_indices = sorted(index_list, key=lambda i: arr[i], reverse=True)

        # 创建一个字典，键是原数组的元素，值是排序后的位置
        sorted_positions = {}
        for new_pos, index in enumerate(sorted_indices):
            sorted_positions[arr[index]] = new_pos

        return sorted_positions


    def hands_pk(self, hand1, hand2):
        poker_power1 = self.poker_hand_rank(hand1)
        poker_power2 = self.poker_hand_rank(hand2)
        if poker_power1 > poker_power2:
            return 1
        elif poker_power1 == poker_power2:
            return 0
        else:
            return -1

    def hands_rank(self, hands):
        """比较多组牌，返回牌力排名: 例如 [1, 6, 5, 3, 2, 4]"""
        rank_num = 1
        hands_copy = hands.copy()
        rank_table = [0 for _ in range(len(hands_copy))]
        for i in range(len(hands_copy)):
            if self.check_hands_all_zero(hands_copy):
                break
            max_hand_tmp = max(hands_copy, key=self.poker_hand_rank)
            indices = self.find_all_indices(hands_copy, max_hand_tmp)
            for index in indices:
                rank_table[index] = rank_num
                hands_copy[index] = 0
            rank_num += 1
        return rank_table
    
    def check_hands_all_zero(self, hands):
        for hand in hands:
            if hand != 0:
                return False
        return True
        

    def find_all_indices(self, lst, target):
        indices = []
        for i, value in enumerate(lst):
            if value == target:
                indices.append(i)
        return indices                                                                                                                                                                                           


    def compare_hands(self, hands):
        """比较多组牌，返回牌最大的一组"""
        return max(hands, key=self.poker_hand_rank)


    def best_five_cards(self, seven_cards):
        """从七张牌中选出最好的五张牌组合"""
        best_rank = (-1,)
        best_hand = None
        best_hand_value = []
        for i in range(7):
            for j in range(i+1, 7):
                for k in range(j+1, 7):
                    for l in range(k+1, 7):
                        for m in range(l+1, 7):
                            hand = [seven_cards[i], seven_cards[j], seven_cards[k], seven_cards[l], seven_cards[m]]
                            hand_value =sorted([e["value"] for e in hand])
                            rank = self.poker_hand_rank(hand)
                            if rank > best_rank:
                                best_rank = rank
                                best_hand = hand
                                best_hand_value = hand_value
                            elif rank == best_rank and hand_value > best_hand_value:
                                best_hand = hand
                                best_hand_value = hand_value
        return best_hand

# # 示例
# cards = [parse_card(card) for card in ['♣6', '♥Q', '♥4', '♦3', '♠7', '♦4', '♣8']]
# best_hand = best_five_cards(cards)
# best_hand_rank = poker_hand_rank(best_hand)

# for card in best_hand:
#     print(f"{card['value']}{card['suit']}")



# # 示例
#   = [
#     [parse_card(card) for card in ["Ah", "Kh", "Qh", "Jh", "Th"]],
#     [parse_card(card) for card in ["2s", "3s", "4s", "5s", "6s"]],
#     [parse_card(card) for card in ["2c", "2d", "2h", "2s", "Ac"]],
#     [parse_card(card) for card in ["2c", "3c", "4c", "5c", "6c"]],
#     [parse_card(card) for card in ["2c", "3c", "4c", "5c", "6c"]],
# ]

# best_hand = compare_hands(hands)
# best_hand_rank = poker_hand_rank(best_hand)
# print(f"Best hand: {best_hand}, Rank: {best_hand_rank}")