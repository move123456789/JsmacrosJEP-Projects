# Get_keyBinds V1.0 15.01.23 17:22
# Made By SmokyAce
# To use create a .txt file in a directory
# Copy the directory and paste it on line 15
# Activate Scipt as Keys and then press the Key you selected and then enter the command /save_keybinds in chat
if __name__ == "":
    from JsMacrosAC import *

# DEBUG #
debug = True
# DEBUG #


def rm(ctx):
    lst = KeyBind.getKeyBindings()
    with open(r'C:/Users/Julian/PycharmProjects/Minecraft jsMacros/Linked/keybinds.txt', 'w') as fp:
        fp.write(str(lst))
        fp.close()
        Chat.log("Saved")
    if debug:
        Chat.log(KeyBind.getKeyBindings())


Chat.createCommandBuilder('save_keybinds').executes(JavaWrapper.methodToJavaAsync(rm)).register()