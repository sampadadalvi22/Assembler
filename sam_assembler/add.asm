section .data
	msg2 db "sum is =",0,10
	num1 dd 18
	num2 dd 20

section .bss

	res resd 1

section .text 
	global main
	extern printf

main:
	mov eax,50
	mov ebx,10
	add eax,ebx
	
	push eax
	push dword[msg2]
	call printf

