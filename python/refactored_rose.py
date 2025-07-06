class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
# Your task is to add the new feature to our system so that 
# we can begin selling a new category of items
# First an introduction to our system:
# All items have a SellIn value which denotes the number of days we have to sell the items
# All items have a Quality value which denotes how valuable the item is
# At the end of each day our system lowers both values for every item
# Once the sell by date has passed, Quality degrades twice as fast
# The Quality of an item is never negative
# "Aged Brie" actually increases in Quality the older it gets
# The Quality of an item is never more than 50
# "Sulfuras", being a legendary item, never has to be sold or decreases in
# "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
# Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
# Quality drops to 0 after the concert
# We have recently signed a supplier of conjured items. This requires an update to our system:
# "Conjured" items degrade in Quality twice as fast as normal items
# Feel free to make any changes to the UpdateQuality method and add any new code as long as everything still works correctly. However, do not alter the Item class or Items property.
# doesn't believe in shared code ownership (you can make the UpdateQuality method and Items property static
# Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.
# testcases to validate the refactored code in pytest format:
def test_update_quality():
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert items[0].quality == 19
    assert items[1].quality == 1
    assert items[2].quality == 6
    assert items[3].quality == 80
    assert items[4].quality == 80
    assert items[5].quality == 21
    assert items[6].quality == 50
    assert items[7].quality == 50
    assert items[8].quality == 4

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        
        for item in self.items:
            item.sell_in -= 1
            item.quality -= 1


if __name__ == "__main__":
    test_update_quality()