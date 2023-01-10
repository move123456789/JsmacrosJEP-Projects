if __name__ == "": from JsMacrosAC import *

fish_sound = "minecraft:entity.player.splash"


def on_sound(event):
    if event.sound == "minecraft:entity.player.splash":
        Chat.log("Wrapper")


JsMacros.waitForEvent("Sound", JavaWrapper.methodToJava(on_sound))


# def on_lyd(event):
#     if event.sound == fish_sound:
#         Chat.log("on_lyd")
#     else:
#         Chat.log("In def else")
#
# JsMacros.waitForEvent("Sound", JavaWrapper.methodToJava(lambda event: event.sound == fish_sound and Chat.log("on_lyd")).overrideThread())