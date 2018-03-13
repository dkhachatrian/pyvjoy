import pyvjoy._sdk as _sdk
import ctypes



class Data:
    """Wrapper class for _sdk._JOYSTICK_POSITION_V2()"""
    def __init__(self, device):
        self._owner = device
        self._data = _sdk.CreateDataStructure(self._owner.rID)
        self._label_to_type = dict(self._data._fields_)
        self.labels = list(self._label_to_type.keys())
    
    def modify_value(self, label, value):
        """Modify labeled axis/button with the specified value.
        Use Data().labels() to see a list of all labels.
        Does *not* update gamepad state until the VJoyDevice
        """
        # wrap the value as the proper ctype first
        c_val = self._label_to_type[label].__call__(value)
        self._data.__setattr__(label, c_val)
    
    def set_data(self, data_struct):
        """
        Set the data of the controller to the vJoy-conforming struct data_struct.
        The Python implementation of the struct can be found at _sdk._VJOYSTICK_POSITION_V2.

        Will cause problems if the passed-in data_struct is not in a proper state! Use with care.
        """
        self._data = data_struct

    def _reset(self):
    	self._data = _sdk.CreateDataStructure(self._owner.rID)