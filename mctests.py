Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.postToChat
<bound method Minecraft.postToChat of <mcpi.minecraft.Minecraft object at 0x757059f0>>
>>> print
<built-in function print>
>>> cat = print
>>> cat (1,2,3,4)
1 2 3 4
>>> mc.postToChat("Hello, randomly-created minecraft world!")
>>> mc.player.getPos()
Vec3(10.942,9.0,32.164)
>>> pos = mc.player.getPos()
>>> pos.x
10.942
>>> type(pos)
<class 'mcpi.vec3.Vec3'>
>>> pos.y
9.0
>>> pos.z
32.164
>>> mc.player.setPos(pos.x, pos.y +100, pos.z)
>>> mc.player.setPos(pos.x +100, pos.y +10, pos.z -100)
>>> pos = mc.player.getPos()
>>> mc.setBlock(pos.x +1, pos.y, pos.z, 1)
>>> pos = mc.player.getPos()
>>> mc.setBlock(pos.x +1, pos.y, pos.z, 5)
>>> import time
>>> import random
>>> wool_block = 35
>>> while True:
	colour = random.randint(1, 15)
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y -1, pos.z, wool_block, color)
	time.sleep(0.1)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 4, in <module>
    mc.setBlock(pos.x, pos.y -1, pos.z, wool_block, color)
NameError: name 'color' is not defined
>>> while True:
	color = random.randint(1, 15)
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y -1, pos.z, wool_block, color)
	time.sleep(0.1)

	
Traceback (most recent call last):
  File "<pyshell#29>", line 5, in <module>
    time.sleep(0.1)
KeyboardInterrupt
>>> while True:
	color = random.randint(1, 15)
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y -1, pos.z, wool_block, color)
	time.sleep(0.1)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 5, in <module>
    time.sleep(0.1)
KeyboardInterrupt
>>> wool_block = 46
>>> while True:
	color = random.randint(1, 15)
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y -1, pos.z, wool_block, color)
	time.sleep(0.1)

	
Traceback (most recent call last):
  File "<pyshell#34>", line 5, in <module>
    time.sleep(0.1)
KeyboardInterrupt
>>> wool_block = 35
>>> while True:
	color = random.randint(1, 15)
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y -1, pos.z, 46, 1)
	time.sleep(0.1)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 3, in <module>
    pos = mc.player.getPos()
  File "/usr/lib/python3/dist-packages/mcpi/minecraft.py", line 66, in getPos
    return CmdPositioner.getPos(self, [])
  File "/usr/lib/python3/dist-packages/mcpi/minecraft.py", line 32, in getPos
    s = self.conn.sendReceive(self.pkg + ".getPos", id)
  File "/usr/lib/python3/dist-packages/mcpi/connection.py", line 50, in sendReceive
    return self.receive()
  File "/usr/lib/python3/dist-packages/mcpi/connection.py", line 42, in receive
    s = self.socket.makefile("r").readline().rstrip("\n")
  File "/usr/lib/python3.4/socket.py", line 371, in readinto
    return self._sock.recv_into(b)
KeyboardInterrupt
>>> 
