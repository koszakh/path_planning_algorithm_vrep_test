// Generated by gencpp from file path_planning_vrep_simulation/RobotMovement.msg
// DO NOT EDIT!


#ifndef PATH_PLANNING_VREP_SIMULATION_MESSAGE_ROBOTMOVEMENT_H
#define PATH_PLANNING_VREP_SIMULATION_MESSAGE_ROBOTMOVEMENT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <path_planning_vrep_simulation/Point2d.h>

namespace path_planning_vrep_simulation
{
template <class ContainerAllocator>
struct RobotMovement_
{
  typedef RobotMovement_<ContainerAllocator> Type;

  RobotMovement_()
    : id(0)
    , goal()
    , velocity(0.0)  {
    }
  RobotMovement_(const ContainerAllocator& _alloc)
    : id(0)
    , goal(_alloc)
    , velocity(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _id_type;
  _id_type id;

   typedef  ::path_planning_vrep_simulation::Point2d_<ContainerAllocator>  _goal_type;
  _goal_type goal;

   typedef float _velocity_type;
  _velocity_type velocity;





  typedef boost::shared_ptr< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> const> ConstPtr;

}; // struct RobotMovement_

typedef ::path_planning_vrep_simulation::RobotMovement_<std::allocator<void> > RobotMovement;

typedef boost::shared_ptr< ::path_planning_vrep_simulation::RobotMovement > RobotMovementPtr;
typedef boost::shared_ptr< ::path_planning_vrep_simulation::RobotMovement const> RobotMovementConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace path_planning_vrep_simulation

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'path_planning_vrep_simulation': ['/home/konst/path_planning_algorithm_vrep_test/src/path_planning_vrep_simulation-master/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9625b7e71a4bfc492ffa4c7b0efb8abe";
  }

  static const char* value(const ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9625b7e71a4bfc49ULL;
  static const uint64_t static_value2 = 0x2ffa4c7b0efb8abeULL;
};

template<class ContainerAllocator>
struct DataType< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >
{
  static const char* value()
  {
    return "path_planning_vrep_simulation/RobotMovement";
  }

  static const char* value(const ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 id\n"
"Point2d goal\n"
"float32 velocity\n"
"\n"
"================================================================================\n"
"MSG: path_planning_vrep_simulation/Point2d\n"
"float32 x\n"
"float32 y\n"
;
  }

  static const char* value(const ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.goal);
      stream.next(m.velocity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RobotMovement_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::path_planning_vrep_simulation::RobotMovement_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::path_planning_vrep_simulation::Point2d_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
    s << indent << "velocity: ";
    Printer<float>::stream(s, indent + "  ", v.velocity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PATH_PLANNING_VREP_SIMULATION_MESSAGE_ROBOTMOVEMENT_H
