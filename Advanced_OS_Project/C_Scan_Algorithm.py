import matplotlib.pyplot as plt
def C_Scan(arr, head, direction, cylinders_number):
    print(head)
    total_head_movement = 0
    distance = 0
    cur_track = 0
    size = len(arr)

    left = []
    right = []
    order_of_disks_served = []

    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    if direction == 'right':
        
        right.append(int(cylinders_number)-1)
        left.append(0)
        left.sort()
        right.sort()
        tracks = right + left
    else:
        left.append(0)
        right.append(int(cylinders_number)-1)
        left.sort(reverse=True)
        right.sort(reverse=True)
        tracks = left + right

    order_of_disks_served.append(head)
    for track in tracks:
        cur_track = track
        distance = abs(cur_track - head)
        # if distance != int(cylinders_number)-1:
        print("distance",distance)
        total_head_movement += distance
        head = cur_track
        order_of_disks_served.append(cur_track)
        
        
    
    #Elgraphhh
    tracks = order_of_disks_served
    order = range(len(tracks))
    plt.plot(tracks, order, marker='o', label='Data Points')
    for i, x in enumerate(tracks):
        plt.text(x, order[i] + 0.1, str(x), ha='center', va='bottom')  
    text = "Total Head Movement: " + str(total_head_movement)
    plt.text(max(tracks), max(order), text, ha='right', va='top')    
    plt.xlabel("Track Number")
    plt.ylabel("Order Served")
    plt.title("Order of Disks Served by C-SCAN Algorithm")
    plt.gca().invert_yaxis()
    plt.show()

    return total_head_movement , order_of_disks_served

    
'''
    print("total head movement =", total_head_movement)
    print("order of disks served", order_of_disks_served)
    tracks = order_of_disks_served
    order = range(len(tracks))
    plt.plot(tracks, order, marker='o', label='Data Points')
    for i, x in enumerate(tracks):
        plt.text(x, order[i] + 0.1, str(x), ha='center', va='bottom')
    plt.xlabel("Track Number")
    plt.ylabel("Order Served")
    plt.title("Order of Disks Served by C-LOOK Algorithm")
    plt.show()

# Driver code

arr = [95, 180, 34, 119, 11, 123, 62, 64]
head = 50
direction = input("Enter the direction (left or right): ").lower()

CLOOK(arr, head, direction)

'''