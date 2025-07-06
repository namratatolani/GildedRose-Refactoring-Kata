class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        
        for item in self.items:
            # The Quality of an item is never more than 50
            # if item.quality < 50:
            # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
            # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
            # Quality drops to 0 after the concert
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 6:
                    item.quality += 3
                elif item.sell_in < 11:
                    item.quality += 2
                else:
                    item.quality += 1
                item.quality = min(item.quality, 50)
            # "Aged Brie" actually increases in Quality the older it gets
            elif item.name == "Aged Brie":
                item.quality += 1
            elif item.name != "Sulfuras, Hand of Ragnaros" and not item.name.startswith("Conjured"):
                item.quality -= 1
            # Once the sell by date has passed, Quality degrades twice as fast
            elif item.sell_in < 0 and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality -= 1
            
            # "Conjured" items degrade in Quality twice as fast as normal items
            if item.name.startswith("Conjured"):
                item.quality -= 2
            # if item.quality > 50:
            #     item.quality = 50
            # At the end of each day our system lowers both values for every item
            # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

        