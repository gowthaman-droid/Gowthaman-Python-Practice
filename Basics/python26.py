queue = []
while True:
    try:
        command = input().strip().split()
        if not command:
            continue
        if command[0] == "ENQUEUE":
            name = command[1]
            tickets = int(command[2])
            queue.append((name, tickets))
        elif command[0] == "DEQUEUE":
            if queue:
                name, tickets = queue.pop(0)
                print("Served:", name)
        elif command[0] == "DISPLAY":
            for name, tickets in queue:
                print(name, tickets)
        elif command[0] == "TOTAL_TICKETS":
            total = sum(tickets for name, tickets in queue)
            print("Total Tickets:", total)
    except EOFError:
        break