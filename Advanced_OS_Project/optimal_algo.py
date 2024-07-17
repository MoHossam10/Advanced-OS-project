def optimal_page_replacement(pages, frame_size):
    page_faults = 0
    page_hits = 0
    frames = [-1] * frame_size
    for i, page in enumerate(pages):

        if page in frames:
            page_hits += 1
        elif -1 in frames:
            free_index = frames.index(-1)
            frames[free_index] = page
            page_faults += 1
        else:
            future_refs = {}
            for j, frame in enumerate(frames):
                if frame in pages[i:]:
                    future_refs[frame] = pages[i:].index(frame)
                else:
                    future_refs[frame] = float('inf') 
            
            furthest_page = max(future_refs, key=future_refs.get)
            furthest_index = frames.index(furthest_page)
            frames[furthest_index] = page
            page_faults += 1

    return page_hits, page_faults