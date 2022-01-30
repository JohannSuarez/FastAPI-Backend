from pydantic import BaseModel

class FooItemBase(BaseModel):
    description: str

# This is the schema that the endpoint
# expects to receive from POST
class FooItemCreate(FooItemBase):
    public: bool

# Inherits from FooItemBase, this is used as
# a response model for the foo/ routes.
# Any response from whatever HTTP method you use on the route
# is going to be in this form.
class FooItem(FooItemBase):
    id: int

    class Config:
        orm_mode = True
