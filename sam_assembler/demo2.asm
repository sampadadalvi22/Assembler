section .data

	msg2 db "my name is sampada",0,10
	len equ $-msg2
	msg1 db "pucsd is pune",0,10
	msg3 db "sampada",0,10
	num1 dd 10,20,30
	num2 dw 8,10
	num3 dq 8,10
	msg5 db "Pune University Pucsd sampada",0,10


section .bss

	str2 resd 1
	str6 resd 2
	str1 resw 1
	str7 resw 2
	str3 resb 10
	str8 resb 2
	str4 resq 1
	str9 resq 2
	str5 rest 1
	str10 rest 2

section .text 
	global main
	extern printf
	extern abc

main:
	
	add eax,eax
	add eax,ebx
	add ebx,edx
	add edi,eax
	add ax,ax
	add ax,bx
	add bx,ax
	add al,al
	add bl,al	


	add eax,dword[msg2]
	add ecx,dword[num1]
	add edx,dword[str1]
	add ebx,dword[num1]
	add esp,dword[num1]
	add esi,dword[str2]
		
	add ax,word[num1]
	add bx,word[num1]

	
	add al,byte[num1]
	add bl,byte[num1]	
    	
	
	add eax,10
	add edi,20
	add ax,10
	add si,10
	add al,10
	add dl,10
	
	
	add dword[str2],eax
	add dword[str2],edx

	add word[str1],ax
	add word[str1],bx	

	
	add byte[str1],al
	add byte[str1],bl

	
	add dword[str2],10
	add word[str1],10
	add byte[str1],10
	add eax,eax

	push 10
	push 100
	push dword[num1]
	push word[num1]
	push eax
	push ebx
	push ax
	push bx
	
	pop dword[num1]
	pop word[num1]
	pop eax
	pop ebx
	pop ax
	pop bx
	

	call printf
	push eax
xxx:	push ebx
yyy:	call abc
zzz:	push dword[num1]
	call abc

	jmp xxx
	jmp yyy
	jmp zzz
