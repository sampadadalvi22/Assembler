 section .data
  a dd 10
  b dd 20
  msg db "result=",0,10
  
 section .bss
  c resd 1
  
 section .text
 global main
 extern printf
  
 main:
  mov esi,50
  mov edi,20
  mov eax,10
  mov ebx,20
  add ebx,eax
  push ebx
  push dword[msg2]
  call printf
  
