from loto import Card

class TestCard:

    def test_name_card(self):
        player_1 = Card('компьютер')
        player_2 = Card('Евгений')
        assert player_1.name_card == 'компьютер'
        assert player_2.name_card == 'Евгений'

    def test_creating_nums_in_card(self):
        player = Card('компьютер')
        assert type(player.creating_nums_in_card()) == list
        assert len(player.creating_nums_in_card()) == 27
        assert type(player.creating_nums_in_card()[0]) == int