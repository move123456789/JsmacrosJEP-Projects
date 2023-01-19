# You must insert the seed in seed =
# V1.0 19.01.23 17:31
if __name__ == "":
    from JsMacrosAC import *

ChunkRandom = Reflection.getClass("net.minecraft.world.level.levelgen.WorldgenRandom")
seed = 3076348734128153433

x = int(Player.getPlayer().getChunkPos().getX())
z = int(Player.getPlayer().getChunkPos().getY())


def isSlimeChunk(x, z):
    Chat.log(ChunkRandom.m_64685_(x, z, seed, 987234911).nextInt(10) == 0)


isSlimeChunk(x, z)
