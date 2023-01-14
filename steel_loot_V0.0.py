import whitelist

if __name__ == "":
    from JsMacrosAC import *
    from whitelist import *

vanilla_inventory_slots = 46
txt = "Steal"

white_list = ["minecraft:stone", "minecraft:grass_block", "minecraft:oak_planks"]


def on_click(ctx, btn):
    Chat.log("Mjau")
    chest_slots = int(Player.openInventory().getTotalSlots() - vanilla_inventory_slots)
    Chat.log(chest_slots)
    for i in range(chest_slots):
        i = + i
        if Player.openInventory().getSlot(i).getItemId() != "minecraft:air":
            Chat.log(Player.openInventory().getSlot(i).getItemId())
            if Player.openInventory().getSlot(i).getItemId() in white_list:
                Player.openInventory().quickAll(i)
    pass


def chest(ybtn, ybtn_wl):
    screen = Hud.getOpenScreen()
    x_btn = int(Hud.getOpenScreen().getWidth() * 0.47)
    y_btn = int(Hud.getOpenScreen().getHeight() / 2 * ybtn)
    x_btn_wl = int(Hud.getOpenScreen().getWidth() * 0.555)
    y_btn_wl = int(Hud.getOpenScreen().getHeight() / 2 * ybtn_wl)
    screen.addButton(x_btn, y_btn, 50, 12, 150, txt, JavaWrapper.methodToJava(on_click))
    screen.addButton(x_btn_wl, y_btn_wl, 10, 10, 150, "X", JavaWrapper.methodToJava(lambda btn, tt: init_screen()))
    # Chat.log("Opened Chest")


def check_chest():
    sceen_name = Hud.getOpenScreenName()
    if "Chest" in sceen_name:
        if "6" in sceen_name:
            ybtn = 1.059
            ybtn_wl = 0.54
            chest(ybtn, ybtn_wl)
        elif "5" in sceen_name:
            ybtn = 1.02
            ybtn_wl = 0.576
            chest(ybtn, ybtn_wl)
        elif "4" in sceen_name:
            ybtn = 0.982
            ybtn_wl = 0.618
            chest(ybtn, ybtn_wl)
        elif "3" in sceen_name:
            ybtn = 0.945
            ybtn_wl = 0.655
            chest(ybtn, ybtn_wl)


if Hud.getOpenScreenName() is not None:
    check_chest()





