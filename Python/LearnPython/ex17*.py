from sys import argv
from os.path import exists

script, from_file, to_file = argv

print 'Copying from %s to %s' % (from_file, to_file)
indata = open(from_file,'r')

print 'The input file is %d bytes long' % len(indata)

print 'Does the output file exists? % r' % exists(to_file)

print 'Ready, hit RETURN to continue, Ctrl - C to abort'
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print 'Alright, All done'

out_file.close()
indata.close()