if __name__ == "":
    from JsMacrosAC import *

# Take Fishing Rod into Hand
# Add this script as Event Sound
# Thow rod first time and you are set

fish = "minecraft:entity.fishing_bobber.splash"


if event.sound == fish:
    Player.getPlayer().interact()
    Chat.log("[Fish]")
    Time.sleep(500)
    Player.getPlayer().interact()





