import threading
from prettytable import PrettyTable

pe_ade_data = [
    [1, 21610005, "Advance Database Engineering"],
    [2, 21610009, "Advance Database Engineering"],
    [3, 21610010, "Advance Database Engineering"],
    [4, 21610011, "Advance Database Engineering"],
    [5, 21610013, "Advance Database Engineering"],
    [6, 21610014, "Advance Database Engineering"],
    [7, 21610017, "Advance Database Engineering"],
    [8, 21610018, "Advance Database Engineering"],
    [9, 21610019, "Advance Database Engineering"],
    [10, 21610022, "Advance Database Engineering"],
    [11, 21610024, "Advance Database Engineering"],
    [12, 21610025, "Advance Database Engineering"],
    [13, 21610028, "Advance Database Engineering"],
    [14, 21610035, "Advance Database Engineering"],
    [15, 21610036, "Advance Database Engineering"],
    [16, 21610038, "Advance Database Engineering"],
    [17, 21610040, "Advance Database Engineering"],
    [18, 21610048, "Advance Database Engineering"],
    [19, 21610051, "Advance Database Engineering"],
    [20, 21610052, "Advance Database Engineering"],
    [21, 21610056, "Advance Database Engineering"],
    [22, 21610057, "Advance Database Engineering"],
    [23, 21610060, "Advance Database Engineering"],
    [24, 21610061, "Advance Database Engineering"],
    [25, 21610062, "Advance Database Engineering"],
    [26, 21610063, "Advance Database Engineering"],
    [27, 21610064, "Advance Database Engineering"],
    [28, 21610067, "Advance Database Engineering"],
    [29, 21610068, "Advance Database Engineering"],
    [30, 21610069, "Advance Database Engineering"],
    [31, 21610070, "Advance Database Engineering"],
    [32, 21610072, "Advance Database Engineering"],
    [33, 21610073, "Advance Database Engineering"],
    [34, 21610074, "Advance Database Engineering"],
    [35, 21610076, "Advance Database Engineering"],
    [36, 22620010, "Advance Database Engineering"],
    [37, 22620012, "Advance Database Engineering"]
]

t4_data = [
    [1, 21610005, "Aaditya S. Patil"],
    [2, 21610018, "Omkar Penshanwar"],
    [3, 21610024, "Shamshad Choudhary"],
    [4, 21610026, "Chinmay Malkar"],
    [5, 21610022, "Rakesh Dharne"],
    [6, 22620003, "Shailendra Mahadule"],
    [7, 21610043, "Vishwas Nalawade"],
    [8, 21610047, "Kedarnath Chavan"],
    [9, 21610050, "Viraj Takone"],
    [10, 21610055, "Siddarth Khedkar"],
    [11, 21610067, "Pranav Kadam"],
    [12, 22620002, "Saurabh Salunke"],
    [13, 21610051, "Aaditya Khot"],
    [14, 21610069, "Rajat Munavalli"],
    [15, 21610006, "Kaustubh Suroshi"]
]

def local_join(result, pe_ade_data, t4_data, start, end):
    thread_id = threading.current_thread().name
    print(f"Thread {thread_id} executing data from index {start} to {end-1}")
    for i in range(start, end):
        pe_ade_row = pe_ade_data[i]
        student_id = pe_ade_row[1]
        for t4_row in t4_data:
            if t4_row[1] == student_id:
                print(f"Thread {thread_id} processing: {pe_ade_row} and {t4_row}")
                result.append(pe_ade_row + t4_row[2:])
                break

num_threads = 2
result = []

# Calculate chunk size based on the length of pe_ade_data
chunk_size = len(pe_ade_data) // num_threads

print(chunk_size)

# Split data range for each thread
ranges = [(i * chunk_size, min((i + 1) * chunk_size, len(pe_ade_data))) for i in range(num_threads)]

# Create and start threads
threads = []
for start, end in ranges:
    thread = threading.Thread(target=local_join, args=(result, pe_ade_data, t4_data, start, end))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Display the result in a table format
result_table = PrettyTable(["ID", "Student ID", "Course", "Name"])
for row in result:
    result_table.add_row(row)

print("Join Result:")
print(result_table)
