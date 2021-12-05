from collections import Counter


if __name__ == '__main__':

    with open('./sample.txt') as f:
        row_wise = [line.strip('\n') for line in f.readlines()]
        # column_wise = []
        gamma_bit = ''
        epsilon_bit = ''
        sample_length = len(row_wise)
        bit_range = len(row_wise[0])
        for index in range(bit_range):
            column_wise = [int(line[index]) for line in row_wise]
            data = Counter(column_wise)
            most_common = data.most_common()
            gamma = most_common[0][0]
            gamma_bit = f"{gamma_bit}{gamma}"
            epsilon = most_common[-1][0] 
            epsilon_bit = f"{epsilon_bit}{epsilon}"

        # The second paramater in the int cast is the base- value you want, since we want base-2 for binary, this wil
        # cast it and evaluate it to the proper decimal value for the bit-string
        epsilon = int(epsilon_bit, 2)
        gamma = int(gamma_bit, 2)
        power_consumption = epsilon * gamma
        print(f"Power consumption is - {power_consumption}")          
            