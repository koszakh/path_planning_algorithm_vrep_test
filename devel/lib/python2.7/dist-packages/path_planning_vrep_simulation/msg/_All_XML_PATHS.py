# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from path_planning_vrep_simulation/All_XML_PATHS.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import path_planning_vrep_simulation.msg

class All_XML_PATHS(genpy.Message):
  _md5sum = "059b622873eff4f7b4831c208d9e7cc2"
  _type = "path_planning_vrep_simulation/All_XML_PATHS"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """XML_PATH[] paths

================================================================================
MSG: path_planning_vrep_simulation/XML_PATH
int32  robot_id
Step[] path

================================================================================
MSG: path_planning_vrep_simulation/Step
int32   number
Point2d start
Point2d finish
float32 duration
================================================================================
MSG: path_planning_vrep_simulation/Point2d
float32 x
float32 y
"""
  __slots__ = ['paths']
  _slot_types = ['path_planning_vrep_simulation/XML_PATH[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       paths

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(All_XML_PATHS, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.paths is None:
        self.paths = []
    else:
      self.paths = []

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
      length = len(self.paths)
      buff.write(_struct_I.pack(length))
      for val1 in self.paths:
        buff.write(_get_struct_i().pack(val1.robot_id))
        length = len(val1.path)
        buff.write(_struct_I.pack(length))
        for val2 in val1.path:
          buff.write(_get_struct_i().pack(val2.number))
          _v1 = val2.start
          _x = _v1
          buff.write(_get_struct_2f().pack(_x.x, _x.y))
          _v2 = val2.finish
          _x = _v2
          buff.write(_get_struct_2f().pack(_x.x, _x.y))
          buff.write(_get_struct_f().pack(val2.duration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.paths is None:
        self.paths = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.paths = []
      for i in range(0, length):
        val1 = path_planning_vrep_simulation.msg.XML_PATH()
        start = end
        end += 4
        (val1.robot_id,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.path = []
        for i in range(0, length):
          val2 = path_planning_vrep_simulation.msg.Step()
          start = end
          end += 4
          (val2.number,) = _get_struct_i().unpack(str[start:end])
          _v3 = val2.start
          _x = _v3
          start = end
          end += 8
          (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
          _v4 = val2.finish
          _x = _v4
          start = end
          end += 8
          (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
          start = end
          end += 4
          (val2.duration,) = _get_struct_f().unpack(str[start:end])
          val1.path.append(val2)
        self.paths.append(val1)
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
      length = len(self.paths)
      buff.write(_struct_I.pack(length))
      for val1 in self.paths:
        buff.write(_get_struct_i().pack(val1.robot_id))
        length = len(val1.path)
        buff.write(_struct_I.pack(length))
        for val2 in val1.path:
          buff.write(_get_struct_i().pack(val2.number))
          _v5 = val2.start
          _x = _v5
          buff.write(_get_struct_2f().pack(_x.x, _x.y))
          _v6 = val2.finish
          _x = _v6
          buff.write(_get_struct_2f().pack(_x.x, _x.y))
          buff.write(_get_struct_f().pack(val2.duration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.paths is None:
        self.paths = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.paths = []
      for i in range(0, length):
        val1 = path_planning_vrep_simulation.msg.XML_PATH()
        start = end
        end += 4
        (val1.robot_id,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.path = []
        for i in range(0, length):
          val2 = path_planning_vrep_simulation.msg.Step()
          start = end
          end += 4
          (val2.number,) = _get_struct_i().unpack(str[start:end])
          _v7 = val2.start
          _x = _v7
          start = end
          end += 8
          (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
          _v8 = val2.finish
          _x = _v8
          start = end
          end += 8
          (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
          start = end
          end += 4
          (val2.duration,) = _get_struct_f().unpack(str[start:end])
          val1.path.append(val2)
        self.paths.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f