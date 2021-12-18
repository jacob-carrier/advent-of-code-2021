
positions_to_fuel = {}

if __name__ == '__main__':
    with open('./sample.txt') as f:
        positions = [int(position) for position in f.readline().split(',')]
        maximum = len(positions) - 1

        for index, position in enumerate(positions):
            if position not in positions_to_fuel:
                next = min(index + 1, maximum)
                left = positions[:index]
                right = positions[next:]
                
                positions_to_fuel[position] = sum(abs(position - pos) for pos in left) + sum(abs(position - pos) for pos in right)
        
        least_fuel = min(positions_to_fuel.values())
        print(f"The least amount of fuel used was - {least_fuel}")