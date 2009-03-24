def hanoi(disc, src, aux, dst):
    if disc > 0:
        hanoi(disc - 1, src, dst, aux)
        print "Move disc %d from %s to %s" % (disc, src, dst)
        hanoi(disc - 1, aux, src, dst)

hanoi(3, 'Src', 'Aux', 'Dst')
