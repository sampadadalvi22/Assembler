%macro add1 2
	mov eax,%1
	mov ebx,%2
	add1 eax,eax
	pudh eax
	call printf
%endmacro

section .data
	a   dd 10
	b   dd 20
	msg db "result=%d",0,10

section .bss
	c resd 1

section .text
	global main
	extern printf
main:
	mov eax,dword[a]
	mov ebx,dword[b]
	add1 20,30
