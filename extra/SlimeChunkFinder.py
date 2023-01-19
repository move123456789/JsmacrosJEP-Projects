# You must insert the seed in seed =
# V1.1 19.01.23 18:00
# You Need to Bind this script to a keybind for now(Will be updated to a service soon).
# Press The Keybind Every Time You Want To Check If A Chunk Is An Slime Chunk
if __name__ == "":
    from JsMacrosAC import *


# == DEBUG ==
debug = False
# == DEBUG ==

# == Post Chunk Cords ==
post_chunk_cords = False
# == Post Chunk Cords ==

overlay = Hud.createDraw2D()
center_x = overlay.getWidth() / 2
center_y = overlay.getHeight() / 2
times_x = center_x * 0.7
times_y = center_y * 0.8
int_x = int(times_x)
int_y = int(times_y)


def hud_post(ovly):
    ovly.addText("SlimeChunk Found", int_x, int_y, 0xFFAA00, True, 3, 0)


ChunkRandom = Reflection.getClass("net.minecraft.world.level.levelgen.WorldgenRandom")
seed = 3076348734128153433

x = int(Player.getPlayer().getChunkPos().getX())
z = int(Player.getPlayer().getChunkPos().getY())


def isSlimeChunk(x, z):
    is_slime_chunk = ChunkRandom.m_64685_(x, z, seed, 987234911).nextInt(10) == 0
    if debug:
        Chat.log(ChunkRandom.m_64685_(x, z, seed, 987234911).nextInt(10) == 0)
    if post_chunk_cords:
        Chat.log(Chat.createTextBuilder().append("X = ").withColor(0x6).append(x).withColor(0x7).append("  Z = ").withColor(0x6).append(z).withColor(0x7).build())
    if is_slime_chunk:
        Chat.log(Chat.createTextBuilder().append("SlimeChunk: ").withColor(0x3).append("X = ").withColor(0x6).append(x).withColor(0x7).append("  Z = ").withColor(0x6).append(z).withColor(0x7).build())
        overlay.setOnInit(JavaWrapper.methodToJavaAsync(hud_post))
        Hud.registerDraw2D(overlay)
        Time.sleep(1500)
        Hud.unregisterDraw2D(overlay)
        Hud.clearDraw2Ds()
        Time.sleep(1000)


isSlimeChunk(x, z)
