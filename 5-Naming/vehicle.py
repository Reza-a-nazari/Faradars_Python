class vehicle :
    brand = None
    color = None 
    _engine_type = None # this is like a private , and sends a signal todevelopers
    def __str__(self):
        return f"vehicle (brand = {self.brand} , color = {self.color})"
    
    #In c# we used {public override string ToString()}

    def __repr__(self):
        return str(self) # for debugging , if you press V , it shows you the address of the object but 
                         # with this method , you can see str representation too ( app5.py )


def _test():
    pass