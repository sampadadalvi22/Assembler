section .data
	first db "first string",0
	f_len equ $-first
	second db "second string",0
	s_len equ $-second
section .bss
	third resb f_len
	fourth resb s_len
section .text
	global main
	extern puts
main:
	mov esi,first
	mov edi,third
	mov ecx,f_len
rep movsb
	push third
	call puts
	add esp,4
