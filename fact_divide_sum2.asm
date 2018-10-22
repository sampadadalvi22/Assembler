section .data
	msg1 db "%f",10,0
	msg db "%d",0
section .bss
	sqr resd 1
	n resd 1
	fact resd 1
	sum resq 1
	x resd 1
section .text
global main
	extern scanf,printf
main:
	fldz
	fstp qword[sum]
	push n
	push msg
	call scanf
	add esp,8
	push x
	push msg
	call scanf
	add esp,8
	xor edi,edi
	xor ebx,ebx
	mov edi,dword[n]
	mov ebx,dword[x]
pqr:	xor eax,eax
	xor edx,edx
	mov esi,edi
	mov eax,ebx
aa1:	cmp esi,1
	jnz aa
	mul ebx
	dec esi
	loop aa1
aa:	mov dword[sqr],eax
	mov ecx,ebx
	mov eax,1
abc:	xor edx,edx
	mul ecx
	loop abc
	mov dword[fact],eax
	fild dword[fact]
	fild dword[sqr]
	fdiv st1
	fadd qword[sum]
	fstp qword[sum]
	dec edi
	cmp edi,0
	jnz pqr
	fld qword[sum]
	sub esp,8
	fstp qword[esp]
	push msg1
	call printf
	add esp,12
