#give output file names:
def files():
    n = 0
    while True:
        n += 1
        yield open('/Daniel/%d.part' % n, 'w')

#search for pattern "["
pat = '['
fs = files()
outfile = next(fs) 

with open('IData/Users/pipelinerun/jobs/20160729_PID_TestJobs.osreg.txt') as infile:
    for line in infile:
        if pat not in line:
            outfile.write(line)
        else:
            items = line.split(pat)
            outfile.write(items[0])
            for item in items[1:]:
                outfile = next(fs)
                outfile.write(pat + item)