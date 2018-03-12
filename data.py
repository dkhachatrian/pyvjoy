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
    
    def _reset(self):
        self._data = _sdk.CreateDataStructure(self._owner.rID)