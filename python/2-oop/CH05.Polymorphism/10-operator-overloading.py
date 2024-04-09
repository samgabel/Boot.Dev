class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze":
            if other.sword_type == "bronze":
                return Sword("iron")
            raise Exception("can not craft")
        if self.sword_type == "iron":
            if other.sword_type == "iron":
                return Sword("steel")
            raise Exception("can not craft")
        raise Exception("can not craft")


s1 = Sword("iron")
s2 = Sword("iron")

try:
    s3 = s1 + s2
    print(s3.sword_type)
except Exception as e:
    print(e)
