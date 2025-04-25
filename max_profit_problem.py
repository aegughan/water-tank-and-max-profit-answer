# Theatre takes 5 unit of time to build. Earnings per unit time = $1500
# Pub takes 4 unit of time to build. Earnings per unit time = $1000
# Commercial Park takes 10 unit of time to build. Earnings per unit time = $3000

def get_max_earnings_and_sequence(unit_time):
    land_covers = [
        ("T", 5, 1500),
        ("P", 4, 1000),
        ("C", 10, 3000),
    ]
    if unit_time <= 4:
        print("Unit of time given is not sufficient to build anything")
        return [0,[]]
    
    result = [([[]], 0) for _ in range(unit_time + 1)]
    for time in range(unit_time-3):
        sequence, earnings = result[time]
        for land_type, time_needed, earning_per_unit in land_covers:
            next_time = time + time_needed
            if next_time <= unit_time:
                new_earnings = earnings + (unit_time - next_time) * earning_per_unit 
                existing_seqs, existing_earning = result[next_time]
                if new_earnings > existing_earning:
                    result[next_time] = ([seq + [land_type] for seq in sequence], new_earnings)
                elif new_earnings == existing_earning:
                    result[next_time][0].extend(seq + [land_type] for seq in sequence)
    max_earning = 0
    best_sequences = []
    for sequences, earning in result:
        if earning > max_earning:
            max_earning = earning
            best_sequences = sequences
        elif earning == max_earning:
            best_sequences.extend(sequences)
    return [max_earning, best_sequences]

total_time_unit = int(input("Time Unit: "))
max_earnings, max_earnings_seq = get_max_earnings_and_sequence(total_time_unit)
print(f"Earnings: ${max_earnings:,d}")
idx = 0
if len(max_earnings_seq) > 0:
    print("Solutions")
    for seq in max_earnings_seq:
        idx += 1
        t_count = seq.count('T')
        p_count = seq.count('P')
        c_count = seq.count('C')
        print(f"{idx}. T:{t_count} P:{p_count} C:{c_count}")
