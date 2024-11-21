from transducer import Transducer

if __name__ == '__main__':
    M = ({'i','s','t','t1','r','r1','r2','v'}, \
         {'click','clickOnCanvas','clickRecenterButton', 'clickRecenterPane','clickRecenterTextBox','clickTriChooseButton','clickTriTypeChoice','documentReady','mouseDownVertex','mouseLeaveCanvas','mouseMove','mouseUpCanvas','recenterTextChange','recenterTextFail','recenterTextSucc'}, \
         {'noop','showTP','hideTP','resetT','showCP','hideCP','checkCT','errorCT','moveC','selectV','moveV','resetV'}, \
         (('i','documentReady','noop 0','s'),('s','clickTriChooseButton','showTP X', 't'),('t','clickTriTypeChoice','resetT {data}','t1'),('t','click','hideTP X','s'),('t','clickOnCanvas','hideTP X','s'),('t1','e','hideTP X','s'),('s','clickRecenterButton','showCP {data}','r'), ('r','clickRecenterTextBox','noop 0','r'),('r','clickRecenterPane','noop 0','r'),('r','recenterTextChange','checkCT {data}','r1'),('r','click','hideCP X','s'),('r','clickOnCanvas','hideCP X','s'),('r1','recenterTextFail','errorCT X','r'),('r1','recenterTextSucc','moveC {data}','r2'),('r2','e','hideCP X','s'),('s','mouseDownVertex','selectV {data}','v'),('v','mouseMoveVertex','moveV {data}','v'),('v','mouseUpCanvas','selectV {name}:{data}','s'),('v','mouseLeaveCanvas','resetV X','s')), \
         'i',
         'e') 
    T = Transducer(M, 'fromGUI', 'toGUI')

    while T.isRunning():
        pass
