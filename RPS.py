# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, ophist=[], seqd = {}):
    prevval = 4

    if prev_play!='':
        ophist.append(prev_play)
    
    if len(ophist) <= prevval:
        return "S"
    
    if len(ophist) > prevval + 1:
        ophist.pop(0)
    
    sq = "".join(ophist)
    seqd[sq] = seqd.get(sq,0) + 1

    sq = ''.join(ophist[-prevval:])
    pred = max([sq+"R", sq+"S", sq+"P"], key=lambda k: seqd.get(k,0))[-1]

    if pred == "R":
        return 'P'
    if pred == 'P':
        return 'S'
    return 'R'