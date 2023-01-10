if __name__ == "":
    from JsMacrosAC import *

health_of_player_float = event.health
health_of_player_int = int(health_of_player_float)


max_slots = 9  # Slot in Backpack
max_slots_range = range(-1, max_slots)

def throw_potion():
    Chat.log("In throw")


def check_potion():
    Player.openInventory()
    if Player.openInventory().getSlot(42).getItemId() == "minecraft:splash_potion":
        Chat.log("Potion in Hotbar 6")
        Player.openInventory().setSelectedHotbarSlotIndex(6)
        Player.openInventory().closeAndDrop()
        Time.sleep(100)
        check = Player.getPlayer().getMainHand().getItemId()
        if check == "minecraft:splash_potion":
            throw_potion()



if health_of_player_int < 19:
    Chat.log(health_of_player_int)
    # Player.openInventory().openGui()
    inv = Player.openInventory()
    Player.openInventory()
    for i in max_slots_range:
        i = i + 1
        item = inv.getSlot(i).getItemId()
        if item == "minecraft:splash_potion":
            Chat.log("Potion Found, moving")
            inv.swapHotbar(i, 6)
            JsMacros.waitForEvent("HeldItemChange").context.releaseLock()
            inv.closeAndDrop()
            break
    check_potion()

