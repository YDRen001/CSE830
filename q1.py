import time
import random
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import math

def ms_v2(sequence):
    if len(sequence) <= 1:
        return sequence

    middle = len(sequence) // 2
    left_seq = ms_v2(sequence[:middle])
    right_seq = ms_v2(sequence[middle:])

    return merge_v2(left_seq, right_seq)

def merge_v2(left_seq, right_seq):
    merged_seq = []
    left_idx = right_idx = 0

    while left_idx < len(left_seq) and right_idx < len(right_seq):
        if left_seq[left_idx] <= right_seq[right_idx]:
            merged_seq.append(left_seq[left_idx])
            left_idx += 1
        else:
            merged_seq.append(right_seq[right_idx])
            right_idx += 1

    merged_seq.extend(left_seq[left_idx:])
    merged_seq.extend(right_seq[right_idx:])

    return merged_seq

def is_v2(sequence):
    for idx in range(1, len(sequence)):
        value = sequence[idx]
        position = idx - 1
        while position >= 0 and value < sequence[position]:
            sequence[position + 1] = sequence[position]
            position -= 1
        sequence[position + 1] = value

def t_merge(input_seq, num_epochs):
    avg_time = 0
    for _ in range(num_epochs):
        merge_seq = input_seq[:]
        start_time = time.time()
        ms_v2(merge_seq)
        avg_time += time.time() - start_time
    return avg_time / num_epochs

def t_insert(input_seq, num_epochs):
    avg_time = 0
    for _ in range(num_epochs):
        insert_seq = input_seq[:]
        start_time = time.time()
        is_v2(insert_seq)
        avg_time += time.time() - start_time
    return avg_time / num_epochs

if __name__ == "__main__":
    merge_times = []
    insert_times = []
    #sizes = list(range(5, 105, 5))
    sizes = [10,100, 1000, 2000, 3000, 5000, 8000, 11000, 14000, 17000, 20000]
    print(sizes)
    for size in sizes:
        seq = list(map(int, range(size)))
        random.shuffle(seq)
        num_epochs = int(10 ** (4 - math.log10(size)))
        merge_time = t_merge(seq,num_epochs)
        insert_time = t_insert(seq,num_epochs)
        merge_times.append(merge_time)
        insert_times.append(insert_time)

    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 14
    plt.figure(figsize=(10, 6))
    plt.style.use('ggplot')
    plt.plot(sizes, merge_times, 'o-', color='steelblue', label='Merge Sort')
    plt.plot(sizes, insert_times, 's-', color='indianred', label='Insertion Sort')
    plt.xlabel("List Size", fontsize=16)
    plt.ylabel("Running Time (seconds)", fontsize=16)
    plt.title("Sorting Algorithm Comparison", fontsize=20, fontweight='bold')
    plt.legend(loc="best", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks
    plt.savefig("q1.pdf")
    plt.show()

