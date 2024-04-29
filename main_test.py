import unittest
from unittest.mock import patch, MagicMock
from main import ReadInputFile, Write_into_file, GetInfo, FourDiceMethod, DefaultStatsMethod, Health, Inventory, Runner


class TestReadInputFile(unittest.TestCase):
    def setUp(self):
        self.reader = ReadInputFile('test_input.csv')

    def test_read_object(self):
        self.reader._info = MagicMock()
        self.reader._info.__getitem__.return_value = ['Human', 'Elf', 'Dwarf']

        races = self.reader.read_object('Race')
        self.assertEqual(races, ['Human', 'Elf', 'Dwarf'])


class TestWriteIntoFile(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_write(self, mock_open):
        writer = Write_into_file('test_output.txt')
        writer.write("This is a test line.")

        mock_open.assert_called_once_with('test_output.txt', 'a')
        mock_open().write.assert_called_once_with("This is a test line.\n")


class TestGetInfo(unittest.TestCase):
    @patch('builtins.input', side_effect=['John', 'Warrior', '2', 'Human', 'Wizard'])
    def test_get_info(self, mock_input):
        input_reader = MagicMock()
        input_reader.read_object.side_effect = [['Human', 'Elf', 'Dwarf'], ['Fighter', 'Wizard', 'Rogue']]
        info = GetInfo(input_reader)

        self.assertEqual(info.player_name(), 'John')
        self.assertEqual(info.character_name(), 'Warrior')
        self.assertEqual(info.level(), 2)
        self.assertEqual(info.race(), 'Human')
        self.assertEqual(info.class_choice(), 'Wizard')


class TestFourDiceMethod(unittest.TestCase):
    @patch('random.randint', return_value=4)
    def test_method(self, mock_randint):
        method = FourDiceMethod(['Strength', 'Dexterity', 'Constitution'])
        result = method.method()
        self.assertEqual(result, 12)


class TestDefaultStatsMethod(unittest.TestCase):
    def setUp(self):
        self.method = DefaultStatsMethod(['Strength', 'Dexterity', 'Constitution'])

    @patch('builtins.input', side_effect=['15', '14', '13'])
    def test_insert_stats(self, mock_input):
        self.method.insert_stats()
        self.assertEqual(self.method._abilities, {'Strength': 15, 'Dexterity': 14, 'Constitution': 13})
        self.assertEqual(self.method._modifiers, {'Strength': 2, 'Dexterity': 2, 'Constitution': 1})


class TestHealth(unittest.TestCase):
    @patch('random.randint', return_value=6)
    def test_hit_dices(self, mock_randint):
        health = Health()
        self.assertEqual(health.hit_dices('wizard'), 6)

    @patch('random.randint', return_value=3)
    def test_hit_points(self, mock_randint):
        health = Health()
        self.assertEqual(health.hit_points('wizard', 1), 6)
        self.assertEqual(health.hit_points('wizard', 2), 9)
        self.assertEqual(health.hit_points('wizard', 3), 12)

class TestInventory(unittest.TestCase):
    def test_add_to_inventory(self):
        input_reader = MagicMock()
        input_reader.read_object.return_value = ['Helmet', 'Sword']
        inventory = Inventory(input_reader)
        inventory.add_to_inventory('Shield')
        self.assertEqual(inventory._inventory_items, ['Helmet', 'Sword', 'Shield'])


class TestRunner(unittest.TestCase):
    @patch('builtins.input', side_effect=['Make', 'Exit'])
    def test_run_program(self, mock_input):
        runner = Runner()
        runner.run_program()



    unittest.main()