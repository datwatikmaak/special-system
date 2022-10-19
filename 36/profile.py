def get_profile(name: str, age: int, *sports, **awards):
    if type(age) != int:
        raise ValueError("Age must be an integer")
    if len(sports) > 5:
        raise ValueError("Maximum of 5 sports allowed")
    profile = {"name": name, "age": age}
    if sports:
        profile["sports"] = sorted(list(sports))
    if awards:
        profile["awards"] = awards
    return profile
