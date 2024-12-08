from transducer import Transducer

if __name__ == '__main__':
    """
    M = (states, alpha_in, alpha_out, transitions, start_state)
    transition = (state1, input_symbol, [output_symbol1, ..., output_symbolK], state2)
    """  
  
    """
    i = open file
    s = do nothing
    t = show different triangle types
    r = box turns red
    r1 = recenter at coord
    v = change area

    and change order of transitions
    """
    M = ({'open file','do nothing','show different triangle types','box turns red','recenter at coord','change area'}, \
           {'click','clickOnCanvas','clickRecenterButton','clickRecenterPane','clickRecenterTextBox','clickTriChooseButton','clickTriTypeChoice','documentReady','mouseDownVertex','mouseLeaveCanvas','mouseMove','mouseUpCanvas','recenterTextChange','recenterTextFail','recenterTextSucc'}, \
           {'noop 0','showTP 0','hideTP 0','resetT {data}','showCP 0','hideCP 0','checkCT {data}','errorCT 0','moveC {data}','selectV {data}','moveV {data}','resetV 0'}, \
           (('open file','documentReady','do nothing',['noop 0']),('do nothing','clickRecenterButton','box turns red',['showCP 0'],),('do nothing','mouseDownVertex','change area',['selectV {data}']),('do nothing','clickTriChooseButton','show different triangle types',['showTP 0']),('show different triangle types','clickOnCanvas','do nothing',['hideTP 0']),('show different triangle types','click','do nothing',['hideTP 0']),('show different triangle types','clickTriTypeChoice','do nothing',['resetT {data}','hideTP 0']),('show different triangle types','mouseDownVertex','change area',['hideTP 0','selectV {data}']),('show different triangle types','clickRecenterButton','box turns red',['hideTP 0','showCP 0']),('box turns red','click','do nothing',['hideCP 0']),('box turns red','clickOnCanvas','do nothing',['hideCP 0']),('box turns red','clickTriChooseButton','show different triangle types',['hideCP 0','showTP 0']),('box turns red','clickRecenterPane','box turns red',['noop 0']),('box turns red','clickRecenterTextBox','box turns red',['noop 0']),('box turns red','clickOnCanvas','recenter at coord',['checkCT {data}']),('box turns red','recenterTextChange','recenter at coord',['checkCT {data}']),('recenter at coord','recenterTextFail','box turns red',['errorCT 0']),('recenter at coord','recenterTextSucc','do nothing',['moveC {data}','hideCP 0']),('change area','mouseMove','change area',['moveV {data}']),('change area','mouseUpCanvas','do nothing',['noop 0']),('change area','mouseLeaveCanvas','do nothing',['resetV 0']),('show different triangle types','clickTriChooseButton','do nothing',['hideTP 0']),('box turns red','clickRecenterButton','do nothing',['hideCP 0'])), \
           'open file'
        )

    T = Transducer(M, 'fromGUI', 'toGUI')
    #T.save("proj2.dotf")
    T.run()
    while T.isRunning():
        pass
