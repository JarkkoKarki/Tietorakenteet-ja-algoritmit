def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    result = []

    for num in numbers:
        if num % 2 == 0:  # parillinen
            if len(odd_queue) > 0:  # pariton jonossa
                odd_num = odd_queue.dequeue() #poistetaan pariton
                result.append((num, odd_num)) #tehdään pari
            else: # ei jonossa
                even_queue.enqueue(num) # lisätään parillinen jonoon
        else:  # pariton
            if len(even_queue) > 0:  # parillinen jonossa
                even_num = even_queue.dequeue() # poistetaan parillinen
                result.append((even_num, num)) # tehdään pari
            else: # ei jonossa
                odd_queue.enqueue(num) # lisätään jonoon

    return result
