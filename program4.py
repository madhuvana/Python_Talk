
def print_header():
    print('---------------------------------------')
    print( 'Journal App  P4 ')
    print('---------------------------------------')

def run_event_loop():
    print('What do you want with this journal ')
    cmd = None
    journal_data = [] #list ()

    while cmd != 'x':
        cmd=input('[L]ist the entries,  [A]dd the entries, E[x]it: ')
        cmd =cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry , we dont understand '{}'.".format(cmd))

    print ('Done, Goodbye. ')

def list_entries(data):
    print('Your Jounnal Entriees .. ')
    entries = reversed(data)
    for idx, entry in  enumerate(entries):
        print('* [{}] {}' .format(idx + 1, entry))

def add_entry(data):
    text = input("Type your entery , <enter> to exit: ")
    data.append(text)

def main():
    print_header()
    run_event_loop()




main()



