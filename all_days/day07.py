# Day07: No Space Left On Device

# First star: You browse around the filesystem to assess the situation and save the resulting terminal output. The
# filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files).
# The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and
# listing the contents of the directory you're currently in.
# Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:
# - cd means change directory. This changes which directory is the current directory, but the specific result depends
#   on the argument:
#     - cd x moves in one level: it looks in the current directory for the directory named x and makes it the current
#       directory.
#     - cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory
#       the current directory.
#     - cd / switches the current directory to the outermost directory, /.
# - ls means list. It prints out all of the files and directories immediately contained by the current directory:
#     - 123 abc means that the current directory contains a file named abc with size 123.
#     - dir xyz means that the current directory contains a directory named xyz.
# Since the disk is full, your first step should probably be to find directories that are good candidates for deletion.
# To do this, you need to determine the total size of each directory. Find all of the directories with a total size of
# at most 100000. What is the sum of the total sizes of those directories?
#
# Second star: The total disk space available to the filesystem is 70000000. To run the update, you need unused space of
# at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.
# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is
# the total size of that directory?

class Directory:
    def __init__(self, name):
        self.name = name
        self.parentDir = None
        self.childrenDirs = []
        self.files = []

    def __copy__(self):
        directory = Directory(self.name)
        directory.parentDir = self.parentDir
        directory.childrenDirs = self.childrenDirs
        directory.files = self.files
        return directory


    def move_to(self, name):
        if name == '..':
            if self.parentDir is None:
                Warning("This directory doesn't have a parent. Stay in the same place.")
            else:
                parent = self.parentDir
                self.name = parent.name
                self.childrenDirs = parent.childrenDirs
                self.files = parent.files
                self.parentDir = parent.parentDir
        else:
            if name not in [directory.name for directory in self.childrenDirs]:
                Warning("This directory wasn't known as child dir. Added.")
                self.childrenDirs += [Directory(name)]
            child_directory = [directory for directory in self.childrenDirs if directory.name == name][0]
            self.parentDir = self.__copy__()
            self.name = name
            self.files = child_directory.files
            self.childrenDirs = child_directory.childrenDirs
        return None

    def add_child_dir(self, name):
        child_dir = Directory(name)
        child_dir.parentDir = self
        self.childrenDirs += [child_dir]
        return None

    def add_file(self, file):
        self.files += [file]
        return None

    def size(self):
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.childrenDirs:
            size += directory.size()
        return size

    def sub_dirs_sizes(self, sub_dirs_sizes=None):
        size = self.size()
        if sub_dirs_sizes is None:
            sub_dirs_sizes = []
        if self.name:
            sub_dirs_sizes += [size]
        for directory in self.childrenDirs:
            sub_dirs_sizes = directory.sub_dirs_sizes(sub_dirs_sizes)
        return sub_dirs_sizes


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def create_dir_tree(data):
    current_directory = Directory(None)
    for line in data:
        if line[0] == '$':
            if line[2:4] == 'cd':
                current_directory.move_to(line.split(' ')[2])
            elif line[2:4] != 'ls':
                Exception(f"The known commands are only ls and cd, not '{line[2:4]}' in '{line}'")
        elif line[:3] == 'dir':
            current_directory.add_child_dir(line.split(' ')[1])
        else:
            size, name = line.split(' ')
            current_directory.add_file(File(name, int(size)))
    while current_directory.parentDir:
        current_directory.move_to('..')
    return current_directory


def find_small_dirs(commands):
    return sum([size for size in create_dir_tree(commands).sub_dirs_sizes() if size <= 100000])


def find_dir_to_delete(commands, memory_space, needed_space):
    head_directory = create_dir_tree(commands)
    filling = head_directory.size()
    available_space = memory_space - filling
    return min([size for size in head_directory.sub_dirs_sizes() if size >= needed_space - available_space])


def run(data_dir, star):
    with open(f'{data_dir}/input-day07.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 1443806
        solution = find_small_dirs(data)
    elif star == 2:  # The final answer is: 942298
        solution = find_dir_to_delete(data, 70000000, 30000000)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
