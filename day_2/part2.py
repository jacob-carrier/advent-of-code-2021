
if __name__ == '__main__':
    forward_distance = 0
    depth = 0
    aim = 0

    with open('./sample.txt') as f:
        for line in f.readlines():
            direction, quantity = line.split(' ')
            quantity = int(quantity)

            if direction == 'forward':
                forward_distance += quantity
                depth += aim * quantity
            elif direction == 'up':
                aim -= quantity
            elif direction == 'down':
                aim += quantity
        
        print(f"Final depth - {depth}")
        print(f"Final forward distance - {forward_distance}")
        print(f"Final computed result - {depth * forward_distance}")