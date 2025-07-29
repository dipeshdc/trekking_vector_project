from pydantic import BaseModel, Field
from typing import List, Optional

class TrekInfo(BaseModel):
    Trek: Optional[str] = None
    Cost: Optional[str] = None
    Time: Optional[str] = None
    Trip_Grade: Optional[str] = Field(default=None, alias="Trip Grade")
    Max_Altitude: Optional[str] = Field(default=None, alias="Max Altitude")
    Accomodation: Optional[str] = None
    Best_Travel_Time: Optional[str] = Field(default=None, alias="Best Travel Time")
    Contact_or_Book_your_Trip: Optional[str] = Field(default=None, alias="Contact or Book your Trip")

    class Config:
        allow_population_by_field_name = True 

class SearchResponse(BaseModel):
    result: List[TrekInfo]
