from sys import argv

script, filename = argv

print 'Were \s going to erase %r' % filename
print 'If you do not want that, hit CRTL-C'
print 'if you want that, hit RETURN'

raw_input('?')

print 'Opening the file...'
target = open(filename, 'w')

print 'Truncating the file, bai bai'
target.truncate()

print 'Now i am going to ask you for three lines'

line1 = raw_input('Line 1:')
line2 = raw_input('>')
line3 = raw_input('>')

print 'Writting'

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print 'Close it'
target.close()