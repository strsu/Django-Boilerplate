from .base import *

if WHOAMI == "prod":
    from .prod import *
elif WHOAMI == "dev":
    from .dev import *
elif WHOAMI == "local":
    from .local import *
else:
    print("Unknown WHOAMI -", WHOAMI)
    exit()

print(f"Running - {WHOAMI}")
