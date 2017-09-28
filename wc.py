#encoding: utf-8
from optparse import OptionParser
import sys,os
 
def opt():
    parser = OptionParser()
    parser.add_option('-c', '--char',
                      dest='chars',
                      action='store_true',
                      default=False,
                      help='only count chars')
 
    parser.add_option('-w', '--word',
                      dest='words',
                      action='store_true',
                      default=False,
                      help='only count words')
 
    parser.add_option('-l', '--line',
                      dest='lines',
                      action='store_true',
                      default=False,
                      help='only count lines')
     
    parser.add_option('-n', '--nototal',
                      dest='nototal',
                      action='store_true',
                      default=False,
                      help='don\'t print total information')
 
    options, args = parser.parse_args()
    return options, args
 
#print options
def get_count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines, words, chars
 
#if not options.chars and not options.words and not options
 
def print_wc(options, lines, words, chars, fn):
    if options.lines:
        print lines,
    if options.words:
        print words,
    if options.chars:
        print chars,
    print fn
 
def main():
    options, args = opt()
     
    if not (options.lines or options.words or options.chars):
        options.lines, options.words, options.chars = True, True, True
     
     
    if args:
        total_lines, total_words, total_chars = 0, 0, 0
        for fn in args:
            if os.path.isfile(fn):
                with open(fn) as fd:
                    data = fd.read()
                lines, words, chars = get_count(data)
                print_wc(options, lines, words, chars, fn)
                total_lines += lines
                total_words += words
                total_chars += chars
            elif os.path.isdir(fn):
                print >> sys.stderr, '%s is a directory' %fn
            else:
                sys.stderr.write('%s: No such file or directory\n' % fn)
        # 只有多个文件的时候会计算出total字段
        if len(args) > 1 and not options.nototal:
            print_wc(options, total_lines, total_words, total_chars, 'total')
    else:
        fn = ''
        data = sys.stdin.read()
        lines, words, chars = get_count(data)
        print_wc(options, lines, words, chars, fn)
     
if __name__ == '__main__':
    main()
