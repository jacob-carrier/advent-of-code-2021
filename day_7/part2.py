positions_to_fuel = {}

if __name__ == '__main__':
    with open('./test.sample.txt') as f:
        positions = [int(position) for position in f.readline().split(',')]
        maximum = len(positions) - 1

        for index, position in enumerate(positions):
            if position not in positions_to_fuel:
                positions_to_fuel[position] = 0

                next = min(index + 1, maximum)
                left = positions[:index]
                right = positions[next:]

                left_fuel = 0
                for item in left:
                    for i in range(abs(item - position)):
                        left_fuel += i + 1
                positions_to_fuel[position] += left_fuel
                

                right_fuel = 0
                for item in right:
                    for i in range(abs(item - position)):
                        right_fuel += i + 1
                positions_to_fuel[position] += right_fuel
        
        least_fuel = min(positions_to_fuel.values())
        print(f"The least amount of fuel used was - {least_fuel}")