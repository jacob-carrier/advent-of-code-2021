
if __name__ == '__main__':
    with open('./sample.txt') as f:
        fishlist = [int(fish) for fish in f.readline().split(',')]
        fish_count = len(fishlist)
        
        observable_days = 80
        new_fish_count = 0
        new_fish_list = []
        for day in range(observable_days):
            if new_fish_count:
                new_fish_list = [8 for _ in range(new_fish_count)]
            
            # fishlist = [(day - 1) % 6 if day != 8 and day - 1 >= 0 else 6 for day in fishlist]
            for index, day in enumerate(fishlist):
                updated_day = 0
                if day <= 6:
                    if day - 1 < 0:
                        updated_day = 6
                    else:
                        updated_day = (day - 1) % 6
                else:
                    updated_day = (day - 1) % 8
                
                fishlist[index] = updated_day
            # updated_new_fish = [(day - 1) % 8 for day in fishlist if day > 6]
            if new_fish_list:
                fishlist = fishlist + new_fish_list
                new_fish_list = []
            
            new_fish_count = len([day for day in fishlist if day == 0])
        print(f"Number of lantern fish - {len(fishlist)}")