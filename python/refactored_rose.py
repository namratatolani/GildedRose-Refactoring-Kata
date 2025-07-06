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
            # At the end of each day our system lowers both values for every item
            item.sell_in -= 1
            item.quality -= 1
            # Once the sell by date has passed, Quality degrades twice as fast
            if item.sell_in < 0:
                item.quality -= 1
            

        