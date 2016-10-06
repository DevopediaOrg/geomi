# Implicit absolute
import geomi
import geomi.solid
import geomi.planar.mod2

# Explicit absolute
from geomi import solid
from geomi.utils import algos
from geomi.planar.mod2 import func1

# Explicit relative
from . import mod2
from .mod2 import func1
from ..solid import mod1

# Implicit absolute (not allowed)
#import .mod2
#import .mod2.func
#import ..solid.mod1