# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

def update_items_on_range(days,items):
    # Generic reusable method to decrease amount of code required
    item_list = items
    for day in range(days):
        print("-------- day %s --------" % day)
        gilded_rose = GildedRose(item_list)
        gilded_rose.update_quality()
        # allows for easy transparency as the tests progress
        for item in item_list:
            print(item)

    return item_list

class GildedRoseTest(unittest.TestCase):
    def test_quality_cannot_decrease_past_0(self):
        items = [Item("Elixir of the Mongoose", 0, 0)]
        updated_items = update_items_on_range(5, items)
        self.assertEqual(0, updated_items[0].quality)

    def test_once_sellin_date_gone_quality_degrades_double(self):
        items = [Item("+5 Dexterity Vest", 1, 20)]
        updated_items = update_items_on_range(5, items)
            
        self.assertEqual(11, updated_items[0].quality) 

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        updated_items = update_items_on_range(3, items)

        self.assertEqual(4, updated_items[0].quality) 

    def test_sulfuras_doesnt_degrade(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 50)]
        updated_items = update_items_on_range(10, items)
            
        self.assertEqual(50, updated_items[0].quality) 

    def test_backstage_passes_increase_in_quality_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        updated_items = update_items_on_range(10, items)

        self.assertEqual(35, updated_items[0].quality)

    def test_backstage_passes_increase_in_quality_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        updated_items = update_items_on_range(13, items)

        self.assertEqual(44, updated_items[0].quality)

    def test_backstage_lose_quality_on_sellin_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        updated_items = update_items_on_range(16, items)

        self.assertEqual(0, updated_items[0].quality)

    def conjured_items_decrease_at_double_the_rate(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        updated_items = update_items_on_range(3, items)

        self.assertEqual(0, updated_items[0].quality)

    def test_quality_of_an_item_is_always_below_50(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Aged Brie", 2, 0),
            Item("Conjured Mana Cake", 3, 6)
        ]
        updated_items = update_items_on_range(60, items)


        for item in updated_items:
            self.assertLessEqual(item.quality, 50)
            print(item.name)
        
if __name__ == '__main__':
    unittest.main()