section .data
	matrix1 dd 10,20,30
		dd 40,50,60
		dd 70,80,90
	
	matrix2 dd 90,80,70
		dd 60,50,40
		dd 30,20,10
	msg db "%d",10,0
section .bss
	matrix3 resd 9
section .text
global main
	extern printf
main:	mov edi,9
	;mov ebx,matrix2
	;mov esi,matrix1
	;mov edx,matrix3
	xor ecx,ecx
lp: 	mov eax,4
	mov esi,matrix1
	mov edx,matrix3
	push edx
	mul ecx
	;xor edx,edx
	pop edx
	mov ebx,matrix2
	add esi,eax
	add ebx,eax
	add edx,eax
	pusha
	mov ecx,dword[ebx]	
	;add ecx,dword[esi]
	sub ecx,dword[esi]
	mov dword[edx],ecx
	push dword[edx]
	push msg
	call printf
	add esp,8
	popa
	inc ecx
	dec edi
	cmp edi,0
	jnz lp
