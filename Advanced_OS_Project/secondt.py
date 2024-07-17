def second_chance(pages, page_frames):
    digit_count = len(pages)
    page_faults = 0
    clock_hand = 0
    frames = [-1] * page_frames  # Initialize frames as empty (-1 represents an empty frame)
    frame_referenced = [False] * page_frames
    
    for page_num in pages:
        page_num = int(page_num)
        if page_num in frames:
            # Page already in frames, mark as referenced
            frame_index = frames.index(page_num)
            frame_referenced[frame_index] = True
        else:
            page_faults += 1
            while True:
                if not frame_referenced[clock_hand]:
                    # Replace page in this frame
                    frames[clock_hand] = page_num
                    frame_referenced[clock_hand] = True
                    clock_hand = (clock_hand + 1) % page_frames
                    break
                else:
                    # Give the page a second chance
                    frame_referenced[clock_hand] = False
                    clock_hand = (clock_hand + 1) % page_frames

    return digit_count - page_faults, page_faults
