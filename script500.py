import itertools
import subprocess
import random

max_permutations = 50 # Adjust the number of permutations as needed
max_instructions = 5500

numbers = list(range(1, 501))
all_good = True

for _ in range(max_permutations):
    random.shuffle(numbers)
    perm_str = ' '.join(map(str, numbers))

    result = subprocess.run(['./push_swap_sf/push_swap/push_swap', perm_str], capture_output=True, text=True)

    num_instructions = len(result.stdout.split('\n')) - 1

    if num_instructions > max_instructions:
        print(f"Permutation: {perm_str}")
        print(f"Number of instructions: {num_instructions}")
        print("--------------------")
        all_good = False

if all_good:
    print("All tests passed!")
else:
    print("Some tests failed.")