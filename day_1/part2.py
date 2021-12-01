

if __name__ == '__main__':
    with open('./sample.txt') as samples:
        sample_depths = [int(depth) for depth in samples]
        three_sampled_depths = []
        index_length = len(sample_depths)

        for index in range(index_length):
            sliding_window = sample_depths[index:index+3]
            if len(sliding_window) < 3:
                continue
            three_sample_window = sum(sliding_window)
            three_sampled_depths.append(three_sample_window)

        sample_depth = three_sampled_depths[0]
        num_depth_increase = 0

        for depth in three_sampled_depths[1:]:
            if depth > sample_depth:
                num_depth_increase = num_depth_increase + 1
            
            sample_depth = depth;
        

        print(f"Number of depth increase - {num_depth_increase}")