# More Info Soon
# This is steel_loot combined with whitelist
# You can create white_list with items_to_list.py or use /steal add "minecraft id"
# V1.6 19.01.23 23:20
# Created by SmokyAce
if __name__ == "":
    from JsMacrosAC import *

import ast

# == DEBUG ==
debug = False
# == DEBUG ==
# If Quark is installed Set Quark to True == Sorts The Inventory
quark = True

Chat.unregisterCommand("steal")  # Unregisters Old Command

Chat.log(Chat.createTextBuilder().append("[").withColor(0x7)
             .append("SmokyAce").withColor(0x6)
             .append("]").withColor(0x7)
             .append(" Steel Loot -").withColor(0xd)
             .append(" Enabled").withColor(0xc).build())

# ALL LOOT DROPS AVAILABLE FROM CHESTS ARE IN white_lst BELOW
# Items in list
white_lst = ['minecraft:torch', 'minecraft:scaffolding', 'minecraft:bread', 'minecraft:book', 'minecraft:coal', 'minecraft:arrow', 'minecraft:paper', 'minecraft:experience_bottle', 'minecraft:obsidian', 'minecraft:pointed_dripstone', 'minecraft:golden_carrot', 'minecraft:emerald', 'the_vault:driftwood', 'the_vault:carbon_nugget', 'the_vault:diamond_nugget', 'the_vault:vault_dust', 'the_vault:magic_silk', 'the_vault:raw_chromatic_iron', 'the_vault:magnetite', 'the_vault:vault_plating', 'quark:blank_rune', 'minecraft:shulker_shell', 'minecraft:netherite_scrap', 'the_vault:vault_essence', 'the_vault:vault_apple', 'the_vault:wild_focus', 'the_vault:knowledge_star_essence', 'the_vault:vault_diamond', 'the_vault:wooden_chest_scroll', 'minecraft:bone', 'minecraft:rotten_flesh', 'minecraft:string', 'minecraft:dead_brain_coral', 'minecraft:gunpowder', 'minecraft:cobweb', 'minecraft:prismarine_shard', 'architects_palette:entwine_rod', 'architects_palette:nether_brass_ingot', 'minecraft:ender_eye', 'the_vault:idol_benevolent', 'the_vault:idol_omniscient', 'the_vault:idol_timekeeper', 'the_vault:idol_malevolence', 'the_vault:gem_echo', 'the_vault:soul_flame', 'the_vault:vault_bronze', 'the_vault:vault_silver', 'the_vault:vault_gold', 'the_vault:altar_chest_scroll', 'minecraft:gold_ingot', 'minecraft:copper_ingot', 'minecraft:amethyst_shard', 'architects_palette:unobtanium', 'the_vault:regret_nugget', 'the_vault:silver_scrap', 'the_vault:relic_booster_pack', 'the_vault:mystery_box', 'the_vault:key_piece', 'the_vault:gilded_chest_scroll', 'the_vault:amplifying_focus', 'the_vault:vault_meat', 'the_vault:carbon', 'the_vault:regret_chunk', 'the_vault:skill_essence', 'minecraft:netherite_ingot', 'minecraft:diamond', 'the_vault:vault_nugget', 'the_vault:sword', 'the_vault:axe', 'the_vault:helmet', 'the_vault:chestplate', 'the_vault:leggings', 'the_vault:boots', 'the_vault:shield', 'the_vault:unidentified_relic_fragment', 'the_vault:fundamental_focus', 'the_vault:memory_shard', 'the_vault:mote_clarity', 'the_vault:crystal_seal_empty', 'the_vault:eternal_soul', 'the_vault:mote_purity', 'the_vault:bitter_lemon', 'the_vault:trinket', 'the_vault:vault_alloy', 'the_vault:mystery_egg', 'the_vault:dreamstone', 'the_vault:phoenix_dust', 'the_vault:chromatic_iron_ingot', 'the_vault:mod_box', 'minecraft:redstone', 'minecraft:lapis_lazuli', 'minecraft:quartz', 'minecraft:enchanted_book', 'minecraft:bell', 'minecraft:elytra', 'minecraft:budding_amethyst', 'the_vault:crystal_budding', 'architects_palette:withered_bone', 'architects_palette:algal_brick', 'architects_palette:algal_blend', 'the_vault:burger_patty', 'the_vault:burger_bun', 'the_vault:empty_flask', 'the_vault:sweet_kiwi', 'the_vault:hunter_eye', 'the_vault:cooked_vault_steak', 'the_vault:poisonous_mushroom', 'the_vault:living_chest_scroll', 'the_vault:burger_cheese', 'the_vault:hearty_apple', 'the_vault:burger_tomato', 'the_vault:burger_lettuce', 'minecraft:potion', 'minecraft:ender_pearl', 'minecraft:blaze_rod', 'minecraft:golden_apple', 'architects_palette:sunmetal_brick', 'minecraft:iron_ingot', 'the_vault:chromatic_iron_nugget', 'the_vault:chromatic_steel_nugget', 'the_vault:ornate_chest_scroll', 'the_vault:nullifying_focus', 'the_vault:vault_ingot', 'the_vault:acceleration_chip', 'the_vault:black_chromatic_steel_ingot', 'the_vault:regret_orb', 'the_vault:knowledge_star_shard', 'the_vault:skill_shard', 'compressium:redstone_2', 'compressium:iron_2', 'compressium:gold_2', 'compressium:copper_2', 'the_vault:extraordinary_larimar', 'the_vault:extraordinary_benitoite', 'the_vault:extraordinary_wutodie', 'the_vault:extraordinary_painite', 'waystones:waystone', 'easy_villagers:trader', 'torchmaster:megatorch', 'trashcans:item_trash_can', 'ironfurnaces:diamond_furnace', 'irongenerators:gold_generator', 'the_vault:eye_of_avarice', 'the_vault:pandoras_box', 'the_vault:black_chromatic_pickaxe', 'quark:pickarang', 'sophisticatedbackpacks:backpack', 'the_vault:phoenix_feather', 'the_vault:resilient_focus', 'the_vault:skill_orb', 'the_vault:knowledge_star', 'compressium:emerald_2', 'compressium:diamond_2', 'sophisticatedbackpacks:iron_backpack', 'cagerium:terrarium', 'the_vault:aura_scroll', 'the_vault:mote_sanctity', 'compressium:netherite_1', 'buildinggadgets:gadget_building', 'mininggadgets:mininggadget_simple', 'mekanismgenerators:wind_generator', 'the_vault:treasure_chest_scroll', 'the_vault:gem_larimar', 'the_vault:gem_benitoite', 'the_vault:gem_wutodie', 'the_vault:gem_painite', 'the_vault:gem_black_opal', 'the_vault:gem_alexandrite', 'the_vault:gem_iskallium', 'the_vault:gem_gorginite', 'the_vault:gem_sparkletine', 'the_vault:gem_ashium', 'the_vault:gem_bomignite', 'the_vault:gem_petzanite', 'the_vault:gem_tubium', 'the_vault:gem_upaline', 'the_vault:gem_xenium', 'the_vault:gem_pog', 'the_vault:unidentified_treasure_key']
lst = len(white_lst)
click_lst = []
active_lst = []
btn_clicked_one = 0
btn_clicked_two = 0

screen = Hud.createScreen("Whitelist WIP", False)


def close(m1, m2):
    screen.close()
    if debug:
        Chat.log("Closed Screen")


def callback(btn, ctx):
    global btn_clicked_two
    if btn_clicked_two == 0:
        btn.setLabel("X")
        btn_clicked_two = 1
        if debug:
            Chat.log('Selected')
        return btn_clicked_two
    if btn_clicked_two == 1:
        btn.setLabel("")
        btn_clicked_two = 0
        if debug:
            Chat.log('Unselected')
        return btn_clicked_two


def callback_two(btn, ctx):
    global btn_clicked_one
    if btn_clicked_one == 0:
        btn.setLabel("X")
        btn_clicked_one = 1
        if debug:
            Chat.log('Selected')
        return btn_clicked_one
    if btn_clicked_one == 1:
        btn.setLabel("")
        btn_clicked_one = 0
        if debug:
            Chat.log('Unselected')
        return btn_clicked_one


def print_str(str):
    if str in click_lst:
        return
    else:
        click_lst.append(str)
        if debug:
            Chat.log("click_lst from print_str")
            Chat.log(click_lst)


def cls_lst(a1, a2):
    click_lst.clear()
    if debug:
        Chat.log("click_lst from def cls_lst")
        Chat.log(click_lst)
    Chat.log("Cleared Marked Items")
    screen.reload()


def set_active_lst(a3, a4):
    global active_lst
    active_lst.clear()
    active_lst = click_lst.copy()
    Chat.log("Active List")
    if debug:
        Chat.log("active_lst from set_active_lst")
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
    global active_lst
    try:
        with open("C:/Users/Julian/PycharmProjects/Minecraft jsMacros/Linked/config_whitelist.txt") as f:
            saved_list_str = f.read()
            f.close()
            active_lst = ast.literal_eval(saved_list_str)
        Chat.log("Loaded Whitelist")
        if debug:
            Chat.log(active_lst)
        return active_lst
    except FileNotFoundError:
        Chat.log("File Doesnt Exist")


def add_all_to_lst(a12, a13):
    global active_lst
    active_lst.clear()
    active_lst = white_lst.copy()
    Chat.log("Added All items To Whitelist")
    if debug:
        Chat.log("active_lst from set_active_lst")
        Chat.log(active_lst)
    return active_lst


def items_to_list_from_cmd(ctx):
    global active_lst
    items_from_cmd = ctx.getArg("itemNameToGive").getItemId()
    Chat.log(Chat.createTextBuilder().append("Added: ").withColor(0x6).append(items_from_cmd).withColor(0x7).build())
    if items_from_cmd in active_lst:
        return
    else:
        active_lst.append(items_from_cmd)


def save_cmd(ctx):
    with open(r'C:/Users/Julian/PycharmProjects/Minecraft jsMacros/Linked/config_whitelist.txt', 'w') as fp:
        fp.write(str(active_lst))
        fp.close()
    Chat.log("Whitelist Saved")


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
    screen.addButton(20, 145, 100, 20, "Add All To Whitelist", JavaWrapper.methodToJava(add_all_to_lst))
    screen.addButton(x_close, y_close, 100, 20, "Close", JavaWrapper.methodToJava(close))
    screen.addButton(x_close, y_cls_lst, 100, 20, "Clear Choices", JavaWrapper.methodToJava(cls_lst))
    # ALL LOOT DROPS AVAILABLE FROM CHESTS ARE IN LOOPS BELOW
    for index, value in enumerate(white_lst[:22]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(140, index, value, screen)
        screen.addButton(160, index + 2, 10, 10, "", JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    for index, value in enumerate(white_lst[22:44]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(180, index, value, screen)
        screen.addButton(200, index + 2, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    for index, value in enumerate(white_lst[44:66]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(220, index, value, screen)
        screen.addButton(240, index + 2, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    for index, value in enumerate(white_lst[66:88]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(260, index, value, screen)
        screen.addButton(280, index + 2, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    for index, value in enumerate(white_lst[88:110]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(300, index, value, screen)
        screen.addButton(320, index + 2, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    for index, value in enumerate(white_lst[110:132]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(340, index, value, screen)
        screen.addButton(360, index + 2, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    for index, value in enumerate(white_lst[132:150]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(380, index, value, screen)
        screen.addButton(400, index + 2, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    for index, value in enumerate(white_lst[150:168]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(420, index, value, screen)
        screen.addButton(440, index + 2, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    for index, value in enumerate(white_lst[168:179]):  # Max Rows on Screen == 22
        index = 20 + index * 20
        screen.addItem(460, index, value, screen)
        screen.addButton(480, index + 2, 10, 10, "",
                         JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    # EXTRAS
    # for index, value in enumerate(white_lst[186:208]):  # Max Rows on Screen == 22
    #     index = 20 + index * 20
    #     screen.addItem(500, index, value, screen)
    #     screen.addButton(520, index + 2, 10, 10, "",
    #                      JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))
    # for index, value in enumerate(white_lst[208:230]):  # Max Rows on Screen == 22
    #     index = 20 + index * 20
    #     screen.addItem(540, index, value, screen)
    #     screen.addButton(560, index + 2, 10, 10, "",
    #                      JavaWrapper.methodToJava(lambda btn, ctx, str=value: btn.setLabel("X") and print_str(str)))


#  ADD ITEMS TO WHITELIST WITH /addWL. Does Not Save The List
Chat.createCommandBuilder('steal')\
    .literalArg('add')\
        .itemArg('itemNameToGive')\
            .executes(JavaWrapper.methodToJavaAsync(items_to_list_from_cmd))\
            .otherwise()\
        .otherwise()\
    .literalArg('save')\
        .executes(JavaWrapper.methodToJavaAsync(save_cmd))\
        .otherwise()\
    .literalArg('gui')\
        .executes(JavaWrapper.methodToJavaAsync(lambda gui1: screen.setOnInit(JavaWrapper.methodToJava(screen_init)) and Hud.openScreen(screen)))\
.register()

vanilla_inventory_slots = 46


def on_click(ctx, btn):
    if Hud.getOpenScreenName() is not None:
        if quark:
            Hud.getOpenScreen().getButtonWidgets()[2].click()  # [2] Is the Sort Inventory Button From Quark(May Vary)
        else:
            pass
    Hud.getOpenScreen().getButtonWidgets()[0].setActive(False)  # Disables the Steal Button After Click in def chest()
    context.releaseLock()  # Takes off the main thread, else i cant use Client.waitTick
    if quark:
        Client.waitTick(10)
    else:
        Client.waitTick(2)
    chest_slots = int(Player.openInventory().getTotalSlots() - vanilla_inventory_slots)
    if debug:
        Chat.log(chest_slots)
        Chat.log("on_click def")
    for i in range(chest_slots):
        i = + i
        if Player.openInventory().getSlot(i).getItemId() != "minecraft:air":
            if Player.openInventory().getSlot(i).getItemId() in active_lst:
                Player.openInventory().quickAll(i)
            if debug:
                Chat.log(Player.openInventory().getSlot(i).getItemId())

    pass


def screen_init_from_chest(sceen):
    Hud.getOpenScreen().close()
    screen.setOnInit(JavaWrapper.methodToJava(screen_init))
    Hud.openScreen(screen)


def chest(ybtn, ybtn_wl):
    Time.sleep(10)
    screen_chest = Hud.getOpenScreen()
    x_btn = int(Hud.getOpenScreen().getWidth() * 0.47)
    y_btn = int(Hud.getOpenScreen().getHeight() / 2 * ybtn)
    x_btn_wl = int(Hud.getOpenScreen().getWidth() * 0.555)
    y_btn_wl = int(Hud.getOpenScreen().getHeight() / 2 * ybtn_wl)
    screen_chest.addButton(x_btn, y_btn, 50, 12, 150, "Steal", JavaWrapper.methodToJavaAsync(on_click))
    screen_chest.addButton(x_btn_wl, y_btn_wl, 10, 10, 150, "X", JavaWrapper.methodToJava(lambda btn, tt: screen_init_from_chest(screen)))
    # Uncomment This Line To Check What The Key You Want To Bind is. Mine is 67 as you see below
    # screen_chest.setOnKeyPressed(JavaWrapper.methodToJavaAsync(lambda key, modifier: Chat.log(key) and Chat.log(modifier)))
    screen_chest.setOnKeyPressed(JavaWrapper.methodToJavaAsync(lambda key, modifier, ctx=None, btn=None: on_click(ctx, btn) if(key == 67) else None))
    if debug:
        Chat.log("Opened Chest")
        Chat.log(screen_chest)


def check_chest():
    if "Chest" in Hud.getOpenScreenName():
        if "6" in Hud.getOpenScreenName():
            ybtn = 1.059
            ybtn_wl = 0.54
            chest(ybtn, ybtn_wl)
        elif "5" in Hud.getOpenScreenName():
            ybtn = 1.02
            ybtn_wl = 0.576
            chest(ybtn, ybtn_wl)
        elif "4" in Hud.getOpenScreenName():
            ybtn = 0.982
            ybtn_wl = 0.618
            chest(ybtn, ybtn_wl)
        elif "3" in Hud.getOpenScreenName():
            ybtn = 0.945
            ybtn_wl = 0.655
            chest(ybtn, ybtn_wl)


JsMacros.on("OpenScreen", JavaWrapper.methodToJavaAsync(lambda a11, a12: check_chest() if(Hud.getOpenScreenName() is not None) else None))




