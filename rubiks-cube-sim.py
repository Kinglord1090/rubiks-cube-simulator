import time

class CUBE:
	up = [['⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜']]
	left = [['🟧', '🟧', '🟧'], ['🟧', '🟧', '🟧'], ['🟧', '🟧', '🟧']]
	front = [['🟩', '🟩', '🟩'], ['🟩', '🟩', '🟩'], ['🟩', '🟩', '🟩']]
	right = [['🟥', '🟥', '🟥'], ['🟥', '🟥', '🟥'], ['🟥', '🟥', '🟥']]
	back = [['🟦', '🟦', '🟦'], ['🟦', '🟦', '🟦'], ['🟦', '🟦', '🟦']]
	down = [['🟨', '🟨', '🟨'], ['🟨', '🟨', '🟨'], ['🟨', '🟨', '🟨']]

	def __init__(self, scramble=[]):
		if scramble:
			for move in scramble:
				self.turn(move)
	
	def turn(self, move, debug=False):
		def clockwise(side):
			side[0][0], side[0][2] = side[0][2], side[0][0]
			side[0][0], side[2][2] = side[2][2], side[0][0]
			side[0][0], side[2][0] = side[2][0], side[0][0]
			side[0][1], side[1][2] = side[1][2], side[0][1]
			side[0][1], side[2][1] = side[2][1], side[0][1]
			side[0][1], side[1][0] = side[1][0], side[0][1]
			return side

		match move:
			case "U" | "U'" | "U2":
				for _ in range(3 if "'" in move else 2 if "2" in move else 1):
					self.up = clockwise(self.up)
					self.left[0][0], self.front[0][0], self.right[0][0], self.back[0][0] = self.front[0][0], self.right[0][0], self.back[0][0], self.left[0][0]
					self.left[0][1], self.front[0][1], self.right[0][1], self.back[0][1] = self.front[0][1], self.right[0][1], self.back[0][1], self.left[0][1]
					self.left[0][2], self.front[0][2], self.right[0][2], self.back[0][2] = self.front[0][2], self.right[0][2], self.back[0][2], self.left[0][2]
			case "L" | "L'" | "L2":
				for _ in range(3 if "'" in move else 2 if "2" in move else 1):
					self.left = clockwise(self.left)
					self.up[0][0], self.front[0][0], self.down[2][2], self.back[2][2] = self.back[2][2], self.up[0][0], self.front[0][0], self.down[2][2]
					self.up[1][0], self.front[1][0], self.down[1][2], self.back[1][2] = self.back[1][2], self.up[1][0], self.front[1][0], self.down[1][2]
					self.up[2][0], self.front[2][0], self.down[0][2], self.back[0][2] = self.back[0][2], self.up[2][0], self.front[2][0], self.down[0][2]
			case "F" | "F'" | "F2":
				for _ in range(3 if "'" in move else 2 if "2" in move else 1):
					self.front = clockwise(self.front)
					self.up[2][0], self.left[2][2], self.right[0][0], self.down[2][0] = self.left[2][2], self.down[2][0], self.up[2][0], self.right[0][0]
					self.up[2][1], self.left[1][2], self.right[1][0], self.down[2][1] = self.left[1][2], self.down[2][1], self.up[2][1], self.right[1][0]
					self.up[2][2], self.left[0][2], self.right[2][0], self.down[2][2] = self.left[0][2], self.down[2][2], self.up[2][2], self.right[2][0]
			case "R" | "R'" | "R2":
				for _ in range(3 if "'" in move else 2 if "2" in move else 1):
					self.right = clockwise(self.right)
					self.up[0][2], self.front[0][2], self.down[2][0], self.back[2][0] = self.front[0][2], self.down[2][0], self.back[2][0], self.up[0][2]
					self.up[1][2], self.front[1][2], self.down[1][0], self.back[1][0] = self.front[1][2], self.down[1][0], self.back[1][0], self.up[1][2]
					self.up[2][2], self.front[2][2], self.down[0][0], self.back[0][0] = self.front[2][2], self.down[0][0], self.back[0][0], self.up[2][2]
			case "B" | "B'" | "B2":
				for _ in range(3 if "'" in move else 2 if "2" in move else 1):
					self.back = clockwise(self.back)
					self.up[0][0], self.left[2][0], self.right[0][2], self.down[0][0] = self.right[0][2], self.up[0][0], self.down[0][0], self.left[2][0]
					self.up[0][1], self.left[1][0], self.right[1][2], self.down[0][1] = self.right[1][2], self.up[0][1], self.down[0][1], self.left[1][0]
					self.up[0][2], self.left[0][0], self.right[2][2], self.down[0][2] = self.right[2][2], self.up[0][2], self.down[0][2], self.left[0][0]
			case "D" | "D'" | "D2":
				for _ in range(3 if "'" in move else 2 if "2" in move else 1):
					self.down = clockwise(self.down)
					self.left[2][0], self.front[2][0], self.right[2][0], self.back[2][0] = self.back[2][0], self.left[2][0], self.front[2][0], self.right[2][0]
					self.left[2][1], self.front[2][1], self.right[2][1], self.back[2][1] = self.back[2][1], self.left[2][1], self.front[2][1], self.right[2][1]
					self.left[2][2], self.front[2][2], self.right[2][2], self.back[2][2] = self.back[2][2], self.left[2][2], self.front[2][2], self.right[2][2]

		if debug:
			time.sleep(0.5)
			print(f"Move: {move}\n")
			self.pretty_print()

	def pretty_print(self):
		sides = [self.up, self.left, self.front, self.right, self.back, self.down]
		for side in sides:
			for i in range(3):
				for j in range(3):
					print(side[i][j], end=" ")
				print()
			print()
		print("=========\n")


if __name__ == "__main__":
	cube = CUBE()

	while True:
		move = input("Enter the move you wanna play (or type X to exit): ").upper()
		validMoves = ["U", "U'", "U2", "L", "L'", "L2", "F", "F'", "F2", "R", "R'", "R2", "B", "B'", "B2", "D", "D'", "D2"] 
		if move in validMoves:
			cube.turn(move, debug=True)
		elif move == "X":
			break
		else:
			print("Not a valid move! Try again.\n")
