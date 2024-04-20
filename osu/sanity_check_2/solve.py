from pwn import *
import base64

context.log_level = 'DEBUG'

r = remote('chal.osugaming.lol', 7277)

with open('ra.osr', 'rb') as f:
	base = base64.b64encode(f.read())

r.recvuntil(b'base64 encoded: ')

r.sendline(base)

r.interactive()

# osu{s4n1ty_A_Pr3s3rv3d}
