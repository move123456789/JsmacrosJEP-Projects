if __name__ == "":
    from JsMacrosAC import *

lst = []
vanilla_inventory_slots = 46
txt = "Btn Text"


def make_lst():
    with open(r'C:/Users/Julian/PycharmProjects/Minecraft jsMacros/Linked/output.txt', 'w') as fp:
        fp.write(str(lst))


def on_click(ctx, btn):
    Chat.log("Mjau")
    chest_slots = int(Player.openInventory().getTotalSlots() - vanilla_inventory_slots)
    Chat.log(chest_slots)
    for i in range(chest_slots):
        i = + i
        if Player.openInventory().getSlot(i).getItemId() != "minecraft:air":
            items = Player.openInventory().getSlot(i).getItemId()
            lst.append(items)
    make_lst()


def check_chest_name():
    if "Chest" in Hud.getOpenScreenName():
        screen = Hud.getOpenScreen()
        x_btn = int(screen.getHeight() / 2 * 1.05)
        y_btn = int(screen.getWidth() / 2)
        Chat.log("Opened Chest")
        screen.addButton(y_btn, x_btn, 80, 12, 150, txt, JavaWrapper.methodToJava(on_click))


if Hud.getOpenScreenName() is not None:
    check_chest_name()

