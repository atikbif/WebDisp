class ObjState:
    def __init__(self,name,comment,upd_time):
        self.discr = list()
        self.analog = list()
        self.messages = list()
        self.name = name
        self.comment = comment
        self.upd_time = upd_time
        
    def add_discr(self,name,comment,state):
        di_state = name,comment,state
        self.discr.append(di_state)
        
    def add_analog(self,name,comment,measure,value):
        ai_state = name,comment,measure,value
        self.analog.append(ai_state)
        
    def add_message(self,mess,type_code):
        mess_state = mess,type_code
        self.messages.append(mess_state)
        
    