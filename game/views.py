from django.shortcuts import render

def index(request):
    board = [""] * 9
    current_player = "X"
    winner = ""

    if request.method == "POST":
        board = request.POST.getlist("board")
        current_player = request.POST.get("player")

        move = request.POST.get("move")
        if move is not None and board[int(move)] == "":
            board[int(move)] = current_player
            current_player = "O" if current_player == "X" else "X"

        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a, b, c in wins:
            if board[a] and board[a] == board[b] == board[c]:
                winner = board[a]

    return render(request, "game/index.html", {
        "board": board,
        "player": current_player,
        "winner": winner
    })
