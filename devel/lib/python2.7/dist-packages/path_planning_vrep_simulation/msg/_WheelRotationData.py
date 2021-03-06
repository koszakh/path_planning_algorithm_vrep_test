# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from path_planning_vrep_simulation/WheelRotationData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class WheelRotationData(genpy.Message):
  _md5sum = "16794a3f07ee22fddbfe509a3034e43c"
  _type = "path_planning_vrep_simulation/WheelRotationData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 id
float32 left_velocity
float32 right_velocity
bool rotation
bool goal_reached
"""
  __slots__ = ['id','left_velocity','right_velocity','rotation','goal_reached']
  _slot_types = ['int32','float32','float32','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,left_velocity,right_velocity,rotation,goal_reached

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WheelRotationData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.left_velocity is None:
        self.left_velocity = 0.
      if self.right_velocity is None:
        self.right_velocity = 0.
      if self.rotation is None:
        self.rotation = False
      if self.goal_reached is None:
        self.goal_reached = False
    else:
      self.id = 0
      self.left_velocity = 0.
      self.right_velocity = 0.
      self.rotation = False
      self.goal_reached = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_i2f2B().pack(_x.id, _x.left_velocity, _x.right_velocity, _x.rotation, _x.goal_reached))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.id, _x.left_velocity, _x.right_velocity, _x.rotation, _x.goal_reached,) = _get_struct_i2f2B().unpack(str[start:end])
      self.rotation = bool(self.rotation)
      self.goal_reached = bool(self.goal_reached)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_i2f2B().pack(_x.id, _x.left_velocity, _x.right_velocity, _x.rotation, _x.goal_reached))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.id, _x.left_velocity, _x.right_velocity, _x.rotation, _x.goal_reached,) = _get_struct_i2f2B().unpack(str[start:end])
      self.rotation = bool(self.rotation)
      self.goal_reached = bool(self.goal_reached)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i2f2B = None
def _get_struct_i2f2B():
    global _struct_i2f2B
    if _struct_i2f2B is None:
        _struct_i2f2B = struct.Struct("<i2f2B")
    return _struct_i2f2B
