from pwn import *
import base64

context.log_level = 'DEBUG'

r = remote('chal.osugaming.lol', 7278)

with open('ra.osr', 'rb') as f:
	base = base64.b64encode(f.read())

r.recvuntil(b'proof of work:')
r.recvline()

cmd = r.recvline().decode().strip()
test = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
output = test.communicate()[0]
r.sendafter(b'solution: ', output)

r.recvuntil(b'base64 encoded: ')
r.sendline(base)

r.interactive()

# osu{this_wont_work_on_bancho}
