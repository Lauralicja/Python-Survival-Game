class SizeError(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        print(message)