from collections import Counter


def track_og(bit_index, rows, max_bit_index=0):
    if len(rows) == 1:
        return rows[0]
    
    if bit_index == max_bit_index:
        return rows[0]
    

    bit_array = [line[bit_index] for line in rows]
    data = Counter(bit_array)
    results = data.most_common()
    highest_bit = results[0][0]
    highest_bit_count = results[0][1]
    lowest_bit_count = results[-1][1]
    if highest_bit_count == lowest_bit_count:
        # For Oxygen Generaor, we know we need to keep to keep all the ones with 1 to break the tie
        # Opposite for the CO2
        rows = [line for line in rows if line[bit_index] == '1']
    else:
        rows = [line for line in rows if line[bit_index] == highest_bit]
    bit_index += 1

    return track_og(bit_index, rows, max_bit_index=max_bit_index)


def track_co2(bit_index, rows, max_bit_index=0):
    if len(rows) == 1:
        return rows[0]
    
    if bit_index == max_bit_index:
        return rows[0]
    

    bit_array = [line[bit_index] for line in rows]
    data = Counter(bit_array)
    results = data.most_common()
    lowest_bit = results[1][0]
    highest_bit_count = results[0][1]
    lowest_bit_count = results[-1][1]
    if highest_bit_count == lowest_bit_count:
        # For C02 Scrubbing, we know we need to keep to keep all the ones with 0 to break the tie
        rows = [line for line in rows if line[bit_index] == '0']
    else:
        rows = [line for line in rows if line[bit_index] == lowest_bit]
    bit_index += 1

    return track_co2(bit_index, rows, max_bit_index=max_bit_index)



if __name__ == '__main__':

    with open('./sample.txt') as f:
        row_wise = [line.strip('\n') for line in f.readlines()]
        
        og = track_og(0, row_wise, max_bit_index=len(row_wise[0]))
        co2 = track_co2(0, row_wise, max_bit_index=len(row_wise[0]))

        # The second paramater in the int cast is the base- value you want, since we want base-2 for binary, this wil
        # cast it and evaluate it to the proper decimal value for the bit-string
        oxygen_generated = int(og, 2)
        co2_scrubbed = int(co2, 2)
        life_support = oxygen_generated * co2_scrubbed
        print(f"Life Support is - {life_support}")          
            