
if __name__ == '__main__':
    forward_distance = 0
    depth = 0

    with open('./sample.txt') as f:
        for line in f.readlines():
            direction, quantity = line.split(' ')
            quantity = int(quantity)

            if direction == 'forward':
                forward_distance += quantity
            elif direction == 'up':
                depth -= quantity
            elif direction == 'down':
                depth += quantity
        
        print(f"Final depth - {depth}")
        print(f"Final forward distance - {forward_distance}")
        print(f"Final computed result - {depth * forward_distance}")