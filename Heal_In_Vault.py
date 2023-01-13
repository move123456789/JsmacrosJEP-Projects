# Auto-Heal With potions
# How to use: Install JsMacros mc mod and install the jep extension
# To enable --> set Event as Damage

if __name__ == "":
    from JsMacrosAC import *

health_of_player_float = event.health
health_of_player_int = int(health_of_player_float)

new_range = range(8, 17)  # Range in 9 top slots in inventory URL: https://wiki.vg/images/1/13/Inventory-slots.png
# Python starts with 0, so we need to use ^8 instead of 9


def throw_potion():
    Chat.log("In throw")
    get_in = Player.getCurrentPlayerInput().yaw
    get_in_pitch = Player.getCurrentPlayerInput().pitch
    Player.getPlayer().lookAt(get_in, 64)
    Player.getPlayer().interact()
    Time.sleep(200)
    Player.getPlayer().lookAt(get_in, get_in_pitch)
    Player.openInventory().setSelectedHotbarSlotIndex(item_in_hand)


def check_potion():
    Player.openInventory()
    if Player.openInventory().getSlot(42).getItemId() == "minecraft:splash_potion":
        Chat.log("Potion in Hotbar 6")  # ^^^^ Checks if potion is in correct hot bar slot
        Player.openInventory().setSelectedHotbarSlotIndex(6)  # Selects HotbarSlot 6
        Player.openInventory().closeAndDrop()  # Closes inv
        Time.sleep(100)  # Waits 100ms / 0.1s
        check = Player.getPlayer().getMainHand().getItemId()  # Checks if potion HotbarSlot 6 is selected
        if check == "minecraft:splash_potion":
            throw_potion()  # Continues in Throw function
        else:
            Time.sleep(50)
            check_potion()  # Else repeat check_potion()


if health_of_player_int < 8:
    Chat.log(health_of_player_int)
    inv = Player.openInventory()
    item_in_hand = inv.getSelectedHotbarSlotIndex()
    for i in new_range:
        i = i + 1
        item = inv.getSlot(i).getItemId()
        if item == "minecraft:splash_potion":
            Chat.log("Potion Found, moving")
            inv.swapHotbar(i, 6)
            # JsMacros.waitForEvent("HeldItemChange").context.releaseLock()
            inv.closeAndDrop()
            break
    check_potion()
