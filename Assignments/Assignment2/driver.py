from toy import *
from candy import *
from stuffed_animal import *
from inventory import Inventory
from item_factory import *


def main():
    test_items()
    test_factories()



def test_items():
    inventory = Inventory()

    robot_bunny = RobotBunny(product_id="123ABC", name="Robot Bunny", desc="This is a robot bunny.", quantity=5, min_age=1, num_sfx=2, color_str="pink")
    rc_spider = RCSpider(product_id="456DEF", name="RC Spider", desc="This is a remote controlled spider.", quantity=9, min_age=12, speed=30, jump_height=20, has_glow=False, spider_type_str="tarantula")
    santas_workshop = SantasWorkshop(product_id="789GHI", name="Santa's Workshop", desc="This is a doll house.", quantity=15, min_age=6, width=10, height=15, num_rooms=8)

    easter_bunny = EasterBunny(product_id="321CBA", name="Easter Bunny", desc="This is an easter bunny.", quantity=25, size_str="small", color_str="white")
    dancing_skeleton = DancingSkeleton(product_id="654FEC", name="Dancing Skeleton", desc="This is a dancing skeleton.", quantity=17, size_str="medium")
    reindeer = Reindeer(product_id="987IHG", name="Reindeer", desc="This is a reindeer.", quantity=4, size_str="large")

    creme_eggs = CremeEggs(product_id="111AAA", name="Creme Eggs", desc="These are chocolate eggs.", quantity=100, pack_size=5)
    pumpkin_caramel_toffee = PumpkinCaramelToffee(product_id="222BBB", name="Pumpkin Caramel Toffee", desc="This is a pumpkin caramel toffee.", quantity=50, flavor_str="sea salt")
    candy_canes = CandyCanes(product_id="333CCC", name="Candy Canes", desc="These are candy canes.", quantity=28, stripe_color_str="red")

    items = [robot_bunny, rc_spider, santas_workshop, easter_bunny, dancing_skeleton, reindeer, creme_eggs, pumpkin_caramel_toffee, candy_canes]
    for i in items:
        inventory._item_dict[i.product_id] = i
    inventory.check_inventory()


def test_factories():
    easter_factory = ItemFactoryType.get_factory("easter")
    halloween_factory = ItemFactoryType.get_factory("halloween")
    christmas_factory = ItemFactoryType.get_factory("christmas")
    factories = [easter_factory, halloween_factory, christmas_factory]
    for factory in factories:
        factory.create_toy()
        factory.create_candy()
        factory.create_stuffed_animal()


if __name__ == '__main__':
    main()