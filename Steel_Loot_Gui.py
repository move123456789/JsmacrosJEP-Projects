# More Info Soon
# This is steel_loot combined with whitelist
# You can create white_list with items_to_list.py
if __name__ == "":
    from JsMacrosAC import *

import ast

white_lst = ['the_vault:faceted_focus', 'the_vault:fundamental_focus', 'the_vault:resilient_focus',
             'the_vault:opportunistic_focus', 'the_vault:nullifying_focus', 'the_vault:amplifying_focus',
             'the_vault:wild_focus']
lst = len(white_lst)
click_lst = []
active_lst = []
btn_clicked_one = 0
btn_clicked_two = 0

screen = Hud.createScreen("Whitelist WIP", False)


def close(m1, m2):
    screen.close()


def callback(btn, ctx):
    global btn_clicked_two
    if btn_clicked_two == 0:
        btn.setLabel("X")
        btn_clicked_two = 1
        Chat.log('Selected')
        return btn_clicked_two
    if btn_clicked_two == 1:
        btn.setLabel("")
        btn_clicked_two = 0
        Chat.log('Unselected')
        return btn_clicked_two


def callback_two(btn, ctx):
    global btn_clicked_one
    if btn_clicked_one == 0:
        btn.setLabel("X")
        btn_clicked_one = 1
        Chat.log('Selected')
        return btn_clicked_one
    if btn_clicked_one == 1:
        btn.setLabel("")
        btn_clicked_one = 0
        Chat.log('Unselected')
        return btn_clicked_one


def print_str(str):
    if str in click_lst:
        return
    else:
        click_lst.append(str)
        Chat.log(click_lst)


def cls_lst(a1, a2):
    click_lst.clear()
    Chat.log(click_lst)
    Chat.log("Cleared Marked Items")
    screen.reload()


def set_active_lst(a3, a4):
    global active_lst
    active_lst.clear()
    active_lst = click_lst.copy()
    Chat.log("Active List")
    Chat.log(active_lst)
    return active_lst


def cls_active_lst(a5, a6):
    active_lst.clear()
    Chat.log("Cleared Whitelist")


def save_lst(a7, a8):
    with open(r'C:/Users/Julian/PycharmProjects/Minecraft jsMacros/Linked/config_whitelist.txt', 'w') as fp:
        fp.write(str(active_lst))
        fp.close()
    Chat.log("Whitelist Saved")


def load_lst(a9, a10):
    try:
        with open("C:/Users/Julian/PycharmProjects/Minecraft jsMacros/Linked/config_whitelist.txt") as f:
            saved_list_str = f.read()
            f.close()
            saved_list = ast.literal_eval(saved_list_str)
        Chat.log("Loaded Whitelist")
        Chat.log(saved_list)
    except FileNotFoundError:
        Chat.log("Filed Doesnt Exist")


def screen_init(screen):
    cen_x = int(Hud.getOpenScreen().getWidth() * 0.5)
    cen_y = int(Hud.getOpenScreen().getHeight() * 0.5)
    y_close = int(cen_y * 1.8)
    x_close = int(cen_x * 0.885)
    y_cls_lst = int(cen_y * 1.7)
    screen.addButton(20, 20, 100, 20, "Add item to Whitelist", JavaWrapper.methodToJava(set_active_lst))
    screen.addButton(20, 45, 100, 20, "Check Whitelist", JavaWrapper.methodToJava(lambda a5, a6: Chat.log(active_lst)))
    screen.addButton(20, 70, 100, 20, "Clear Whitelist", JavaWrapper.methodToJava(cls_active_lst))
    screen.addButton(20, 95, 100, 20, "Load Whitelist", JavaWrapper.methodToJava(load_lst))
    screen.addButton(20, 120, 100, 20, "Save Whitelist", JavaWrapper.methodToJava(save_lst))
    screen.addButton(x_close, y_close, 100, 20, "Close", JavaWrapper.methodToJava(close))
    screen.addButton(x_close, y_cls_lst, 100, 20, "Clear Marked Items", JavaWrapper.methodToJava(cls_lst))
    for index, value in enumerate(white_lst):
        index = 20 + index * 20
        screen.addItem(140, index, value, screen)
        screen.addButton(160, index, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))


def rm(ctx): # If using Command
    screen.setOnInit(JavaWrapper.methodToJava(screen_init))
    Hud.openScreen(screen)


Chat.createCommandBuilder('ov').executes(JavaWrapper.methodToJavaAsync(rm)).register()
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

def screen_init_from_chest(sceen):
    Hud.getOpenScreen().close()
    screen.setOnInit(JavaWrapper.methodToJava(screen_init))
    Hud.openScreen(screen)
    screen_init(screen)


def chest(ybtn, ybtn_wl):
    screen = Hud.getOpenScreen()
    x_btn = int(Hud.getOpenScreen().getWidth() * 0.47)
    y_btn = int(Hud.getOpenScreen().getHeight() / 2 * ybtn)
    x_btn_wl = int(Hud.getOpenScreen().getWidth() * 0.555)
    y_btn_wl = int(Hud.getOpenScreen().getHeight() / 2 * ybtn_wl)
    screen.addButton(x_btn, y_btn, 50, 12, 150, txt, JavaWrapper.methodToJava(on_click))
    screen.addButton(x_btn_wl, y_btn_wl, 10, 10, 150, "X", JavaWrapper.methodToJava(lambda btn, tt: screen_init_from_chest(screen)))
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





