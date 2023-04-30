# default factory example
from dataclasses import dataclass, field
 
 
def get_emp_id():
    id = 2345
    return id
 
# A class for holding an employees content
@dataclass(frozen=False)
# when frozen = True it mean cannot assign new value for a field in class
class employee:
    name: str
    age: int
       
    # default factory field
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(default="patna", init = False) #accept to init value of field or not
    # in this case the value of city alway patna and cannot be init
    short_info: str = field(repr=False, init=False)
    # repr = false it mean not appear when print class
    def __post_init__ (self) -> None:
        self.short_info = f"{self.name}-{self.age}"
    # create a value based on another
 
 
# object of dataclass
emp = employee("Satyam", 21)
print(emp)
print(emp.short_info)