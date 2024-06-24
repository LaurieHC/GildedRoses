# -*- coding: utf-8 -*-

class ItemAger(object):

    def standard_item(item):
        if item.sell_in > 0:
            item.quality = max((item.quality - 1), 0)
        else:
            item.quality = max((item.quality - 2), 0)
        item.sell_in += -1

    def aged_brie(item):
        if item.sell_in > 0:
            item.quality = min((item.quality + 1), 50)
        else:
            item.quality = min((item.quality + 2), 50)
        item.sell_in += -1 

    def backstage_passes(item):

        if item.sell_in > 10:
            item.quality = min((item.quality + 1), 50)

        elif item.sell_in > 5:
            item.quality = min((item.quality + 2), 50)

        elif item.sell_in > 0:
            item.quality = min((item.quality + 3), 50)

        else:
            item.quality = 0
        item.sell_in += -1 

    def conjured_item(item):
        if item.sell_in > 0:
            item.quality = max((item.quality - 2), 0)
        else:
            item.quality = max((item.quality - 4), 0)
        item.sell_in += -1

    def legendary_item(item):
        pass

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name == "Aged Brie":
                ItemAger.aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                ItemAger.backstage_passes(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                """
                unlike other items which are specific for what they are Sulfuras is specific in the specifications due
                to being a legendary item and so uses a legendary item method.
                """
                ItemAger.legendary_item(item)
            elif item.name == "Conjured Mana Cake":
                ItemAger.conjured_item(item)
            else:
                ItemAger.standard_item(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)