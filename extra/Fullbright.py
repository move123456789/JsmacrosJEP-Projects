# Fullbright V1.1
# Made By SmokyAce
# Toggle It on or off With command /fb
if __name__ == "":
    from JsMacrosAC import *

overlay = Hud.createDraw2D()
screen = Hud.getOpenScreen()
center_x = overlay.getWidth() / 2
center_y = overlay.getHeight() / 2
times_x = center_x * 0.97
times_y = center_y * 0.8
int_x = int(times_x)
int_y = int(times_y)


def add_hud_fb_off(ovly):
    ovly.addText("FB OFF", int_x, int_y, 0xFFAA00, True)


def add_hud_fb_on(ovly):
    ovly.addText("FB ON", int_x, int_y, 0xFFAA00, True)


def full_b_off(ctx):
    Chat.unregisterCommand('fb')
    Chat.log(Chat.createTextBuilder().append("[").withColor(0x7)
             .append("Utils").withColor(0x6)
             .append("]").withColor(0x7)
             .append(" FullBright").withColor(0xd)
             .append(" disabled").withColor(0xc).build())
    Client.getGameOptions().setGamma(1)
    overlay.setOnInit(JavaWrapper.methodToJava(add_hud_fb_off))
    Hud.registerDraw2D(overlay)
    Time.sleep(1000)
    Hud.unregisterDraw2D(overlay)
    Hud.clearDraw2Ds()
    Time.sleep(1000)
    Chat.createCommandBuilder('fb').executes(JavaWrapper.methodToJavaAsync(full_b_on)).register()


def full_b_on(ctx):
    Chat.unregisterCommand('fb')
    Chat.log(Chat.createTextBuilder().append("[").withColor(0x7)
             .append("Utils").withColor(0x6)
             .append("]").withColor(0x7)
             .append(" FullBright").withColor(0xd)
             .append(" enabled").withColor(0xa).build())
    Client.getGameOptions().setGamma(16.0)
    overlay.setOnInit(JavaWrapper.methodToJava(add_hud_fb_on))
    Hud.registerDraw2D(overlay)
    Time.sleep(1000)
    Hud.unregisterDraw2D(overlay)
    Hud.clearDraw2Ds()
    Time.sleep(1000)
    Chat.createCommandBuilder('fb').executes(JavaWrapper.methodToJavaAsync(full_b_off)).register()


# Startup
Chat.createCommandBuilder('fb').executes(JavaWrapper.methodToJavaAsync(full_b_on)).register()
Chat.log(Chat.createTextBuilder().append("[").withColor(0x7)
         .append("Smokyace_Dev").withColor(0x6)
         .append("]").withColor(0x7)
         .append(" Loaded").withColor(0xd)
         .append(" script").withColor(0xa).build())








