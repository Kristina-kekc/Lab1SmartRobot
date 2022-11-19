IDLE = 0
TASK_RECEIVED = 1
MOVING = 2
TURN = 3
TIMEOUT = 4
NUMEVENTS = 5

EVENTNAMES = ("IDLE", "TASK_RECEIVED", "MOVING", "TURN", "TIMEOUT", )

class Model:
    def __init__(self, numstates, handler, debug =False):
        self._numstate = numstates
        self._running = False
        self._transition = []
        for i in range (0, numstates):
            self._transitions.append([None]*NUMEVENTS)
        self._curState = -1
        self._handler = handler
        self._debug = debug

    def start(self):
        self._curState = 0
        self._running = True
        self._handler.stateEntered(self._curState)

    def stop(self):
        if self._running:
            self._handler.stateLeft(self._curState)
        self._running = False
        self._curState = -1

    def gotoState(self, newState):
        if (newState < self._numstates):
            if self._debug:
                print(f"Going from State {self._curState} to State {newState}")
            self._handler.stateLeft(self._curState)
            self._curState = newState
            self._handler.stateEntered(self._curState)

    def addTransition(self, fromState, event, toState):
        self._transitions[fromState][event] = toState

    def processEvent(self, event):
        if (event < NUMEVENTS):
            newstate = self._transitions[self._curState][event]
            if newstate is None:
                if self._debug:
                    print(f"Ignoring event {EVENTNAMES[event]}")
            else:
                if self._debug:
                    print(f"Processing event {EVENTNAMES[event]}")
                self.gotoState(self._transitions[self._curState][event])