
(1) Download and extract the folder
(2) The sub folder named 'source Code' contains all files needed for execution
    'Source Code' contains 4 variants of the code (in terms of subfolders):
	alpha_beta:
		opening.py
		game.py
	black_moves:
		opening.py
		game.py
	heuristic1:
		opening.py
		game.py
	heuristic2:
		opening.py
		game.py

	opening.py and game.py are the python codes corresponding to the version given by the folder 		name.


(3) Steps to run any file : 
	Navigate to the required sub directory:

	python <filename> <input_file_path> <output_file_path> depth
	
	e.g. python opening.py board1.txt board2.txt 1
		OR
	     python game.py board1.txt board2.txt 1
	
	'Board1.txt' contains the input string.Please do not write in it.
