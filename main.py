from transducer import Transducer

if __name__ == '__main__':
    """
    M = (states, alpha_in, alpha_out, transitions, start_state)
    transition = (state1, input_symbol, [output_symbol1, ..., output_symbolK], state2)
    """  
   
    M = ({'i','s','t','r','r1','v'}, \
           {'click','clickOnCanvas','clickRecenterButton','clickRecenterPane','clickRecenterTextBox','clickTriChooseButton','clickTriTypeChoice','documentReady','mouseDownVertex','mouseLeaveCanvas','mouseMove','mouseUpCanvas','recenterTextChange','recenterTextFail','recenterTextSucc'}, \
           {'noop 0','showTP 0','hideTP 0','resetT {data}','showCP 0','hideCP 0','checkCT {data}','errorCT 0','moveC {data}','selectV {data}','moveV {data}','resetV 0'}, \
           (('i','documentReady',['noop 0'],'s'),('s','clickRecenterButton',['showCP 0'],'r'),('s','mouseDownVertex',['selectV {data}'],'v'),('s','clickTriChooseButton',['showTP 0'],'t'),('t','clickOnCanvas',['hideTP 0'],'s'),('t','click',['hideTP 0'],'s'),('t','clickTriTypeChoice',['resetT {data}','hideTP 0'],'s'),('t','mouseDownVertex',['hideTP 0','selectV {data}'],'v'),('t','clickRecenterButton',['hideTP 0','showCP 0'],'r'),('r','click',['hideCP 0'],'s'),('r','clickOnCanvas',['hideCP 0'],'s'),('r','clickTriChooseButton',['hideCP 0','showTP 0'],'t'),('r','clickRecenterPane',['noop 0'],'r'),('r','clickRecenterTextBox',['noop 0'],'r'),('r','clickOnCanvas',['checkCT {data}'],'r1'),('r','recenterTextChange',['checkCT {data}'],'r1'),('r1','recenterTextFail',['errorCT 0'],'r'),('r1','recenterTextSucc',['moveC {data}','hideCP 0'],'s'),('v','mouseMove',['moveV {data}'],'v'),('v','mouseUpCanvas',['noop 0'],'s'),('v','mouseLeaveCanvas',['resetV 0'],'s'),('t','clickTriChooseButton',['hideTP 0'],'s'),('r','clickRecenterButton',['hideCP 0'],'s')), \
           'i'
        )

    T = Transducer(M, 'fromGUI', 'toGUI')
    #T.save("proj2.dotf")
    T.run()
    while T.isRunning():
        pass
