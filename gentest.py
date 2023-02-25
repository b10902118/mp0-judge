import random

# Define the character set
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789.aaaaaa"

# Generate 20 random strings of length 10 containing characters from the character set
d = set()
while len(d) < 20:
    d.add("".join(random.choices(charset, k=10)))
d = list(d)
# Generate 20 unique filenames of length 10 containing characters from the character set
f = set()
while len(f) < 20:
    f.add("".join(random.choices(charset, k=10)))
f = list(f)

# Calculate the number of 'a's in each string in d

# Print the strings and their corresponding 'a' counts
# for i, string in enumerate(d):
#    print(f"String {i+1}: {string}, 'a' count: {na[i]}")

# Define the maximum number of directories and files in each depth
max_dirs_per_depth = [1, 2, 1, 2, 1]
max_files_per_depth = [0, 1, 1, 0, 1]

# Generate the directory hierarchy in memory as a list of strings
root = d[0]
paths = []
dirs_in_depth = [""]
di = 0
fi = 0
for depth in range(1, 6):
    new_dirs = []
    for parent_dir in dirs_in_depth:
        for i in range(min(max_dirs_per_depth[depth-1], 20-len(paths))):
            new_dir = f"{parent_dir}/{d[di]}"
            di += 1
            paths.append((new_dir, False))
            new_dirs.append(new_dir)
        for j in range(min(max_files_per_depth[depth-1], 20-len(paths))):
            # filename = random.choice(list(f))
            filepath = f"{parent_dir}/{f[fi]}"
            fi += 1
            paths.append((filepath, True))
    dirs_in_depth = new_dirs
    if len(paths) >= 20:
        break

# Sort the list of paths in alphabetical order
paths = [(path[0][1:], path[1]) for path in paths]
paths.sort()

# na = [string.count("a") for string in paths]
# Print the full paths of all files and directories in alphabetical order

# generate c code
with open("user/test.c", 'w') as f:
    f.write("void test() {\n")
    for i in range(20):
        if paths[i][1]:
            f.write('mkfile("'+paths[i][0]+'");\n')
        else:
            f.write('mkd("'+paths[i][0]+'");\n')
    f.write('}')

# generate python code
answer = ""
for path in paths:
    answer += "'{} {}',\n".format(path[0], path[0].count("a"))
answer += f"'',\n'{di-1} directories, {fi} files',\n"

print(answer)
with open("grade-mp0.py", 'w') as f:
    f.write('''from gradelib import *
r = Runner()
@test(5, "max path len")
def test_mp0_0():
    r.run_qemu(shell_script(['testgen', 'mp0 ''' + root + " a',]))" +
            '''
    r.match(
''' +
            answer +
            '''
    )

run_tests()
'''
            )
