# need to get rid of lambda transitions (blank symbol)
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
        # delta element = (q in Q, x in Sigma_in, p in Q, [o for o in Sigma_out])
        self.transitions = {}
        for q, x, p, o in T[3]:
            if q not in self.states:
                raise Exception(f'"{q}" is not a valid state')
            if x not in self.alphaIn: 
                raise Exception(f'"{x}" is not a valid input symbol')
            if any([x not in self.alphaOut for x in o]): 
                raise Exception(f'some value in "{o}" is not a valid output symbol')
            if p not in self.states:
                raise Exception(f'"{p}" is not a valid state')

            if q not in self.transitions:
                self.transitions[q] = {x: (p, o)}
            else:
                self.transitions[q][x] = (p, o)

        self.curState = T[4]
        
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
    
    # halt the machine when there is no more input
    def stop(self):
        print("Stopping the machine")
        self.running = False
        self.inputFile.close()
        self.outputFile.close()

    # to tell if the machine is currently active 
    def isRunning(self):
        return self.running
    
    # main loop for the machine
    def run(self):
        # start the machine running
        self.running = True
        print("Transducer running")
        while self.running:
            # read event message
            try:
                msg, data = self.inputFile.readline().split(maxsplit=1)
                self.transition(msg, data)
            except Exception as e:
                pass

    # how to move between states following the encoded table
    def transition(self, msg, data):
        if msg not in self.alphaIn:# and msg != self.blank:
            raise Exception(f'{msg} is not a valid command')

        if msg not in self.transitions[self.curState]:
            raise Exception(f'{self.curState} doesn\'t handle {msg}')
     
        # machine hit a dead end, no use keeping it alive
        if len(self.transitions[self.curState]) == 0:
            self.stop()

        nextState, outputs = self.transitions[self.curState][msg]
       
        print(f'{self.curState} --{msg}:{outputs}--> {nextState}')
        self.curState = nextState
               
        for output in outputs:
            if '{data}' in output:
                output = output.format(data = data)
            print(output, file=self.outputFile, flush=True)

