import chess
import os


clear_word = "clear"

board = chess.Board()

def turn(board_to_process):
	board = chess.Board(board_to_process)
	board_fen = str(board.fen())

	def printboard(message=""):
		os.system(clear_word)
		for i in board_fen:
			if i == " ":
				print(board_fen[board_fen.index(i)+1]+" to move")
				break
		print(board)
		print(message)
	
	moved = False
	printboard()
	while not moved:

		move = input("Enter a move in SAN format: \n")
		try:
			board.push_san(move)
			board_fen = str(board.fen())
			printboard()
		except:
			printboard(f"Move: {move} is invalid")

	
turn(board.fen())