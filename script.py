import itertools
import subprocess

numbers = [1, 2, 3, 4]

permutations = list(itertools.permutations(numbers))
for permutation in permutations:
    perm_str = ' '.join(map(str, permutation))

    result = subprocess.run(['./push_swap', perm_str], capture_output=True, text=True)

    num_instructions = len(result.stdout.split('\n')) - 1
    l =  0

    if num_instructions > 12:
        print(f"Permutation: {perm_str}")
        print(f"Number of instructions: {num_instructions}")
        print("--------------------")
        l = l + 1

    
    if l == 0:
        print ("all good")

    
    