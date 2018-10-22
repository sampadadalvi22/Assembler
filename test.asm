section .data
	msg  db "sampada dalvi",0,10
	num1 dd 10
	num2 dd 20,25
	num4 dw 20,25
	num5 dq 20,25
	num6 dt 20,25

section .bss

	str2 resd 10
	str3 resb 10
	
section .text  
	global main  
	extern printf
main:
	
	mov eax,10
	mov ebx,10
	mov eax,dword[num1]
	add eax,eax
	mov eax,dword[num1]
	mov word[num1],ax
	mov dword[num1],eax
	mov byte[num1],al	
	mov eax,eax
	mov edi,ebx
	add eax,10
	add eax,dword[num1]
