from bat.syn_scan import syn_scan

def go(argv):
    syn = syn_scan.SynScanner(argv)
    syn.execute()

