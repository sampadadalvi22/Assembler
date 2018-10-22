section .data

	msg2 db "Sampada Dalvi",0,10
	len equ $-msg2
	msg1 db "I like sports",0,10
	msg3 db "syspro",0,10
	num1 dd 10,20,30
	num2 dw 8,10
	num3 dq 8,10
	msg5 db "Department of computer science",0,10


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

main:
	
	mov eax,eax
	mov eax,ebx
	mov ebx,edx
	mov edi,eax
	mov ax,ax
	mov ax,bx
	mov bx,ax
	mov al,al
	mov bl,al	


	mov eax,dword[msg2]
	mov ecx,dword[num1]
	mov edx,dword[str1]
	mov ebx,dword[num1]
	mov esp,dword[num1]
	mov esi,dword[str2]

		
	mov ax,word[num1]
	mov bx,word[num1]

	
	mov al,byte[num1]
	mov bl,byte[num1]	
    	
	
	mov eax,10
	mov edi,20
	mov ax,10
	mov si,10
	mov al,10
	mov dl,10
	
	
	mov dword[str2],eax
	mov dword[str2],edx

	mov word[str1],ax
	mov word[str1],bx

	
	mov byte[str1],al
	mov byte[str1],bl

	
	mov dword[str2],10
	mov word[str1],10
	mov byte[str1],10
	add eax,eax


