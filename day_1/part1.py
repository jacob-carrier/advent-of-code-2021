if __name__ == "__main__":
    num_depth_increase = 0

    with open('./sample.txt') as samples:
        sample_depths = [int(depth) for depth in samples]

        sample_depth = sample_depths[0]

        for depth in sample_depths[1:]:
            if depth > sample_depth:
                num_depth_increase = num_depth_increase + 1
            
            sample_depth = depth;
        

        print(f"Number of depth increase - {num_depth_increase}")
