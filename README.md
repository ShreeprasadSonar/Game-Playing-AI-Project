# AI Project - Morris-Variant Game

This project implements the Morris-Variant game using Python programming language and explores the use of Minimax and Alpha-Beta algorithms for game-playing agents.

## Game Rules
The game is played on a board consisting of 23 positions connected by lines. Each player has nine pieces and takes turns to place them on the board. Once all pieces have been placed, players take turns to move their pieces to an adjacent position along a line. Whenever a player forms a straight line of three pieces, they may remove one of their opponent's pieces. The game ends when a player has only two pieces left or is unable to make a legal move.

## Part I: Minimax
Two programs are implemented in this part. The first program, `MiniMaxOpening`, plays a move in the opening phase of the game, while the second program, `MiniMaxGame`, plays in the midgame/endgame phase. Both programs take two file names as input for the input and output board positions, and the depth of the tree that needs to be searched. The output is the board position after White plays its best move, as determined by a Minimax search tree of the given depth and the static estimation function given in the Morris-Variant handout. That board position is also written into the output file. The programs also print the number of positions evaluated by the static estimation function and the Minimax estimate for that move.

## Part II: Alpha-Beta
This part is similar to Part I, but the Alpha-Beta pruning algorithm is used instead of Minimax. Two programs, `ABOpening` and `ABGame`, are implemented using Alpha-Beta algorithm. These programs behave exactly the same as the programs of Part I, but return the exact same estimate values as the programs of Part I, with the main difference in the number of nodes that were evaluated.

## Part III: Play a Game for Black
Two programs, `MiniMaxOpeningBlack` and `MiniMaxGameBlack`, are implemented in this part to play a game for Black instead of White.

## Part IV: Static Estimation
An improved static estimation function is implemented in this part. The new function is better than the one suggested in the handout. The programs of Part I are rewritten with this improved static estimation function. The programs are named `MiniMaxOpeningImproved` and `MiniMaxGameImproved`.

Please refer to the Morris-Variant handout for additional information on the game and program inputs.