from refactored_rose import GildedRose, Item

tests = [
    ["normal", "before sell date", 5, 10, 4, 9],
    ["normal", "on sell date", 0, 10, -1, 8],
    ["normal", "after sell date", -10, 10, -11, 8],
    ["normal", "of zero quality", 5, 0, 4, 0],
    ["Aged Brie", "before sell date with max quality", 5, 50, 4, 50],
    ["Aged Brie", "on sell date", 0, 10, -1, 12],
    ["Aged Brie", "on sell date near max quality", 0, 49, -1, 50],
    ["Aged Brie", "on sell date with max quality", 0, 50, -1, 50],
    ["Aged Brie", "after sell date", -10, 10, -11, 12],
    ["Aged Brie", "after sell date with max quality", -10, 50, -11, 50],
    ["Sulfuras, Hand of Ragnaros", "before sell date", 5, 80, 5, 80],
    ["Sulfuras, Hand of Ragnaros", "on sell date", 0, 80, 0, 80],
    ["Sulfuras, Hand of Ragnaros", "after sell date", -10, 80, -10, 80],
    ["Backstage passes to a TAFKAL80ETC concert", "long before sell date", 11, 10, 10, 11],
    ["Backstage passes to a TAFKAL80ETC concert", "long before sell date at max quality", 11, 50, 10, 50],
    ["Backstage passes to a TAFKAL80ETC concert", "medium close to sell date (upper bound)", 10, 10, 9, 12],
    ["Backstage passes to a TAFKAL80ETC concert", "medium close to sell date (upper bound) at max quality", 10, 50, 9, 50],
    ["Backstage passes to a TAFKAL80ETC concert", "medium close to sell date (lower bound)", 6, 10, 5, 12],
    ["Backstage passes to a TAFKAL80ETC concert", "medium close to sell date (lower bound) at max quality", 6, 50, 5, 50],
    ["Backstage passes to a TAFKAL80ETC concert", "very close to sell date (upper bound)", 5, 10, 4, 13],
    ["Backstage passes to a TAFKAL80ETC concert", "very close to sell date (upper bound) at max quality", 5, 50, 4, 50],
    ["Backstage passes to a TAFKAL80ETC concert", "very close to sell date (lower bound)", 1, 10, 0, 13],
    ["Backstage passes to a TAFKAL80ETC concert", "very close to sell date (lower bound) at max quality", 1, 50, 0, 50],
    ["Backstage passes to a TAFKAL80ETC concert", "on sell date", 0, 10, -1, 0],
    ["Backstage passes to a TAFKAL80ETC concert", "after sell date", -10, 10, -11, 0],
    ["Conjured Mana Cake", "before sell date", 5, 10, 4, 8],
    ["Conjured Mana Cake", "before sell date at zero quality", 5, 0, 4, 0],
    ["Conjured Mana Cake", "on sell date", 0, 10, -1, 6],
    ["Conjured Mana Cake", "on sell date at zero quality", 0, 0, -1, 0],
    ["Conjured Mana Cake", "after sell date", -10, 10, -11, 6],
    ["Conjured Mana Cake", "after sell date at zero quality", -10, 0, -11, 0],
]
def test_update_quality():
    for item_name, condition, sell_in, quality, expected_sell_in, expected_quality in tests:
        items = [Item(name=item_name, sell_in=sell_in, quality=quality)]
        print(items)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(f"Testing {item_name} with condition '{condition}'")
        print("Items post update: ", items)
        assert items[0].sell_in == expected_sell_in, f"Failed for {item_name} ({condition})"
        assert items[0].quality == expected_quality, f"Failed for {item_name} ({condition})"