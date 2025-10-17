place: dict[str, str | int | bool] = {
    "colour": "white",
    "shape": "round",
    "x colour": "beige",
    "is laminate": True,
    "degree": "4",
    "angles": "2",
}

place["degree"] = "5"

degree_str: str = str(place["degree"])
angles_str: str = str(place["angles"])

total_vol: int = int(degree_str) * int(angles_str)
print(total_vol)
