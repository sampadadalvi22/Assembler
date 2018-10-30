how to run

pucsd -$ ./sampadaassembler.py add.asm                       => Get Output of asm file
pucsd -$ ./sampadaassembler.py add.asm -s                    => display symbol table
pucsd -$ ./sampadaassembler.py add.asm -l                    => display literal table
pucsd -$ ./sampadaassembler.py add.asm -i                    => display Intermediate code
pucsd -$ ./sampadaassembler.py add.asm -lst                  => display lst file code
pucsd -$ ./sampadaassembler.py add.asm -o                    => display object code
pucsd -$ ./sampadaassembler.py add.asm -lst I anyfile.lst    => store lst file in enter anyfile.lst name
pucsd -$ ./sampadaassembler.py add.asm -o   I anyfile.txt    => store obj code in enter anyfile.txt name

MACRO
pucsd -$ ./sampadaassembler.py macro.asm                     => Get Output of macro_asm file
pucsd -$ ./sampadaassembler.py macro.asm -e                  => display macro expansion code
pucsd -$ ./sampadaassembler.py macro.asm -mt                 => display macro   table (MNT & MDT)
pucsd -$ ./sampadaassembler.py macro.asm -ms                 => display symbol  table
pucsd -$ ./sampadaassembler.py macro.asm -ml                 => display literal table
pucsd -$ ./sampadaassembler.py macro.asm -mi                 => display Intermediate code
pucsd -$ ./sampadaassembler.py macro.asm -mlst               => display lst file code
pucsd -$ ./sampadaassembler.py macro.asm -mo                 => display object code
pucsd -$ ./sampadaassembler.py macro.asm -mlst I anyfile.lst => store lst file in enter anyfile.lst name
pucsd -$ ./sampadaassembler.py macro.asm -mo I anyfile.txt   => store obj code in enter anyfile.txt name



##ZERO PASS (MACRO)

file name: macro.py
 -find MNT
 -find MNT
 -replacement 
 -find macro expansion code
 -find macro symbol table
 -find macro literal table
 -find macro intermediate code
 -find lst code
 -find object code
 


##ONE PASS

file name: symbiltable.py
 - error handaling
 - find all symbols
 - find symbol address 	
 
file name: literaltable.py
 - find all literal and its convert hex
 
file name: intermediatecode.py
 - handaling symbol and literl using symbol table and literal table
 - handaling all instrction in opcode table (Intermediate Code Instructions Set.pdf)
 - replacing all opcode in opcode table (Intermediate Code Instructions Set.pdf)
 


##TWO PASS

file name: finalLst.py
 - Finding  and handaling all data section addressing
 - Finding  and handaling all bss section addressing 
 - Finding  and handaling all txt section addressing in (ModRM AND Opcod Instructions Set.pdf)


file name: finalObj.py
 - handaling and display symbol table using pass I
 - handaling and display literal table using pass I
 - handaling and display all data section addressing using lst file
 - handaling and display all bss section addressing usuing lst file
 - Finding  and handaling all txt section addressing in (ModRM AND Opcod Instructions Set.pdf)


##SMACO

file name: smaco.py
 - read symbol table and literal table
 - also read object code 
 - using above table and object code get out-put of object code


##DEBUGGER

file name: debugger.py
 - read symbol table and literal table
 - also read object code 
 - using above table and object code debugging object code step by step
 -List of classes of commands:
	'h' or 'hlep'  --help for debugger instructions
	'ni' or 'next' --execute the next instruction
	'q' or 'quit'  --quit out of gdb 
	'list'         --display source code
	'info reg'     --display all register information
	'display $reg' --display always $reg  information
	'print/d $reg' --display $reg  values in decimal
	'print/h $reg' --display $reg  values in hexdecimal
	'print/b $reg' --display $reg  values in binary
	'run'          --start the debugging program 


 

##MAIN FILE

file name: sampadaassembler.py

SYNOPSIS 
 	 ./sampadaassembler.py asm_filename [options]	=> Get Outpuet asm file 

COMMAND LINE OPTIONS

	 -s 	=> Display Symbol Table

	 -l 	=> Display Literal Table

	 -i 	=> Display Intermediate Code

	 -lst   => Display lst Code

	 -o   	=> Display Object Code

	 -gdb   => Debugging Source Code

	 -lst I output_filename.lst 	=> Write lst Code

	 -o   I output_filename.txt 	=> Write Object Code


SYNOPSIS MACRO 
 		  ./sampadaassembler.py macro_asm_filename [options]	=> Get Output macro_asm file

COMMAND LINE OPTIONS MACRO

	 -e  	=> Display Macro Expansion Code

	 -mt 	=> Display Macro Table (MNT & MDT)

	 -ms 	=> Display Symbol Table

	 -ml 	=> Display Literal Table

	 -mi 	=> Display Intermediate Code

	 -mlst  => Display lst Code

	 -mo 	=> Display Object Code

	 -mgdb  => Debugging Source Code

	 -e    I output_filename.txt 	=> Write Macro Expansion Code

	 -eo   I output_filename.txt 	=> Write Object Code

	 -elst I output_filename.txt 	=> Write lst Code




 

