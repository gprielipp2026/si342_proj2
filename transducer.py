
class Transducer:
    """
    @param T - transducer in tuple form (Q, Sigma_in, Sigma_out, delta, s, blank symbol)
    @param inputFilename - string for filename
    @param outputFilename - string for filename
    """
    def __init__(self, T, inputFilename, outputFilename):
        self.states = {x for x in T[0]}
        self.alphaIn = {x for x in T[1]}
        self.alphaOut = {x for x in T[2]}
        # delta element = (q in Q, x in Sigma_in, o in Sigma_out, p in Q)
        self.transitions = {}
        for q, x, o, p in T[3]:
            if q not in self.transitions:
                self.transitions[q] = {x: (p, o)}
            else:
                self.transitions[q][x] = (p, o)

        self.curState = T[4]
        # blank symbol?
        self.blank = T[5]
        
        self.inputFile = open(inputFilename, 'r')
        self.outputFile = open(outputFilename, 'w')

    # write the internal data in .DOT format
    def save(self, fn):
        print("Saving transducer to '" + str(fn) + "'")
        with open(fn, 'w') as fd:
            fd.write('digraph {\n')
            
            for state in self.states:
                for inp in self.alphaIn:
                    if state in self.transitions and inp in self.transitions[state]:
                        p, outp = self.transitions[state][inp]
                        fd.write(f'{state} -> {p} [label="{inp}:{outp}"]\n')

            fd.write('}')

    def stop(self):
        self.running = False
        self.inputFile.close()
        self.outputFile.close()

    def isRunning(self):
        return self.running

    def run(self):
        # start the machine running
        self.running = True
        print("Transducer running")
        print(self.transitions)
        while self.running:
            # read event message
            try:
                msg, data = self.inputFile.readline().split(maxsplit=1)
                print('received:', msg, data)
                self.transition(msg, data)
            except Exception as e:
                pass
                #print('Error:', e) 

    def transition(self, msg, data):
        print(f'{self.curState} {msg} {data}', flush=True)
        if msg not in self.alphaIn and msg != self.blank:
            raise Exception(f'{msg} is not a valid command')

        if msg not in self.transitions[self.curState]:
            raise Exception(f'{self.curState} doesn\'t handle {msg}')
     
        if ':' in msg:
            self.saveVertName = msg.split(':')[0]

        # machine hit a dead end
        if len(self.transitions[self.curState]) == 0:
            self.stop()

        nextState, output = self.transitions[self.curState][msg]
        self.curState = nextState
        
        if output != self.blank:
            if '{data}' in output:
                output = output.format(data = data)
            #if '{name}' in output:
                #output = output.format(name = self.saveVertName)
            print(output, file=self.outputFile, flush=True)

if __name__ == '__main__':
    M = ({0,1,3}, {'a','b','c'}, {'a','ba','b'}, \
            ((0,'b','b {data}',0),(0,'a','e',1),(1,'a','a',1),(1,'b','ba',0),(1,'c','a',3)), 0, 'e')
    T = Transducer(M, "fromGUI", "toGUI")

    while T.isRunning():
        pass
