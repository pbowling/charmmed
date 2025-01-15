from datetime import datetime
from typing import Any, Dict, Optional
from dataclasses import dataclass, field

class RecordStatus():
    INPREP = 0
    COMPLETE = 1
    FAILURE = -999

class Record:
    status: RecordStatus = RecordStatus.INPREP
    start_time: Optional[datetime] = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    #properties: Optional[PropertySet] = None