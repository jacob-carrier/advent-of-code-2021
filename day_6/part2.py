

if __name__ == '__main__':
    with open('./sample.txt') as f:
        fishlist = [int(fish) for fish in f.readline().split(',')]
        fish_count = len(fishlist)

        states = {
            0: fishlist.count(0),
            1: fishlist.count(1),
            2: fishlist.count(2),
            3: fishlist.count(3),
            4: fishlist.count(4),
            5: fishlist.count(5),
            6: fishlist.count(6),
            7: fishlist.count(7),
            8: fishlist.count(8)
        }
        
        observable_days = 256
        for day in range(observable_days):
            # Shift the days - 1
            next_states = {
                0: states[1],
                1: states[2],
                2: states[3],
                3: states[4],
                4: states[5],
                5: states[6],
                6: states[7],
                7: states[8],
                8: states[0]
            }

            if states[0] > 0:
                next_states[6] += states[0]

            states = next_states
            next_states = {}
                
        result = sum(values for values in states.values())
        print(f"Number of lantern fish - {result}")