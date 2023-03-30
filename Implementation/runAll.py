import os

file_names = ["MiniMaxOpening.py", "MiniMaxGame.py", "ABOpening.py", "ABGame.py", 
              "MiniMaxOpeningBlack.py", "MiniMaxGameBlack.py"]
# , "MiniMaxOpeningImproved.py", "MiniMaxGameImproved.py"
board1_file = "board1.txt"
board2_file = "board2.txt"
num = "1"

for file_name in file_names:
    os.system(f"python {file_name} {board1_file} {board2_file} {num}")