k = 31
scaled = 1000

num_files_each_iteration = 5000

list_filename = 'filelist'
script_filename = 'script.sh'

if __name__ == "__main__":
    f = open(list_filename, 'r')
    lines = f.readlines()
    f.close()

    num_files = len(lines)
    num_iterations = int(num_files/num_files_each_iteration+1)

    f = open(script_filename, 'w')

    for i in range(num_iterations):
        start = i*num_files_each_iteration
        end = min( (i+1)*num_files_each_iteration, num_files )
        lines_this_iteration = lines[start:end]

        cmd = f'sourmash sketch dna -p k={k},scaled={scaled}'
        for line in lines_this_iteration:
            line_stripped = line.strip()
            cmd = cmd + ' ../refseq/' + line_stripped

        f.write(cmd + '\n')

    f.close()
