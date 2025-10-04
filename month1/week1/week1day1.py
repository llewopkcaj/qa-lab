place = {"colour": "white", 
         "shape": "round",
         "x colour": "beige",
         "is laminate": True,
         "degree": "4",
         "angles": "2"
         }

place["degree"] = "5"
total_vol = int(place["degree"]) * int(place["angles"])
print(total_vol)
