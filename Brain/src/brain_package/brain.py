def initialize() :
    Orders = [
        [0, "stop"],
        [1, "start"],
        [2, "test"],
        [3, "check"],
        [4, "pick"]
    ]

def ask_voc_reco_for_order() :


    response = 0

    return response

def get_all_pieces_from_cam():
    response = [
        ['shape', 'color', 'x_cam', 'y_cam', 'z_cam', 'id']
    ]
    return response

def verify_pos_cam(piece) :

    response = 0
    if type(response) == list : # response = [x_cam, y_cam, z_cam]
        piece[2] = response[0]
        piece[3] = response[1]
        piece[4] = response[2]
    elif response == 0 :
        piece = 0
    return piece
    
def compute_real_coordinates

def start() :
    pieces = get_all_pieces_from_cam()
    for piece in pieces :
        piece = verify_pos_cam(piece)
        if piece == 0 :
            continue
        piece_coordinates = compute_real_coordinates(piece[2], piece[3], piece[4])

initialize()
while True :
    order = ask_voc_reco_for_order()
    if order == 0 :
        break
    elif order == 1 :
        start()
    elif order == 2 :
        test()
    elif order == 3 :
        check()
    elif order == 4 :
        pick()
    else :
        break