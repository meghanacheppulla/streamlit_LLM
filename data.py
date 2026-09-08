"""
Static fallback data for Foodie Explorer.
Structure:
COUNTRIES = {
    "Country Name": {
        "flag": "emoji",
        "blurb": "one line about the country's food culture",
        "regions": {
            "Region/State Name": {
                "restaurants": {
                    "Restaurant Name": {
                        "desc": "short description",
                        "menu": [
                            {"dish": "Dish name", "price": "₹XXX", "rating": 4.5},
                            ...
                        ]
                    }
                }
            }
        }
    }
}
This data is used whenever the LLM (LangChain) is not configured, or as a
seed/example so the LLM has something to imitate.
"""

COUNTRIES = {
    "India": {
        "flag": "🇮🇳",
        "blurb": "A vast land of regional cuisines, spices and thalis.",
        "regions": {
            "Andhra Pradesh": {
                "restaurants": {
                    "Southern Spice": {
                        "desc": "Legendary for fiery Andhra-style curries and biryani.",
                        "menu": [
                            {"dish": "Andhra Chicken Curry", "price": "₹280", "rating": 4.7},
                            {"dish": "Gongura Mutton", "price": "₹350", "rating": 4.8},
                            {"dish": "Pesarattu", "price": "₹120", "rating": 4.5},
                            {"dish": "Bobbatlu (Sweet)", "price": "₹90", "rating": 4.4},
                        ],
                    },
                    "Minerva Coffee Shop": {
                        "desc": "An institution for authentic Andhra breakfast and tiffins.",
                        "menu": [
                            {"dish": "Masala Dosa", "price": "₹110", "rating": 4.6},
                            {"dish": "Pulihora", "price": "₹90", "rating": 4.3},
                            {"dish": "Filter Coffee", "price": "₹40", "rating": 4.7},
                        ],
                    },
                }
            },
            "Telangana": {
                "restaurants": {
                    "Paradise Biryani": {
                        "desc": "Hyderabad's most iconic name for dum biryani.",
                        "menu": [
                            {"dish": "Hyderabadi Chicken Biryani", "price": "₹300", "rating": 4.8},
                            {"dish": "Mutton Biryani", "price": "₹380", "rating": 4.9},
                            {"dish": "Double Ka Meetha", "price": "₹100", "rating": 4.5},
                        ],
                    },
                    "Bawarchi": {
                        "desc": "Famous local favourite for spicy, generous biryani plates.",
                        "menu": [
                            {"dish": "Veg Biryani", "price": "₹220", "rating": 4.4},
                            {"dish": "Chicken 65", "price": "₹210", "rating": 4.6},
                        ],
                    },
                }
            },
            "Tamil Nadu": {
                "restaurants": {
                    "Murugan Idli Shop": {
                        "desc": "Soft idlis and authentic Chettinad flavours since decades.",
                        "menu": [
                            {"dish": "Soft Idli with Sambar", "price": "₹90", "rating": 4.6},
                            {"dish": "Chettinad Chicken", "price": "₹260", "rating": 4.7},
                            {"dish": "Filter Kaapi", "price": "₹35", "rating": 4.8},
                        ],
                    },
                    "Saravana Bhavan": {
                        "desc": "World-famous vegetarian South Indian chain.",
                        "menu": [
                            {"dish": "Ghee Roast Dosa", "price": "₹130", "rating": 4.7},
                            {"dish": "Rava Kesari", "price": "₹80", "rating": 4.4},
                        ],
                    },
                }
            },
            "Karnataka": {
                "restaurants": {
                    "MTR (Mavalli Tiffin Room)": {
                        "desc": "Bengaluru heritage restaurant, iconic for breakfast tiffins.",
                        "menu": [
                            {"dish": "Rava Idli", "price": "₹100", "rating": 4.7},
                            {"dish": "Masala Dosa", "price": "₹120", "rating": 4.6},
                        ],
                    },
                    "Vidyarthi Bhavan": {
                        "desc": "Old-school crispy dosas loved across generations.",
                        "menu": [
                            {"dish": "Benne Masala Dosa", "price": "₹90", "rating": 4.8},
                        ],
                    },
                }
            },
            "Kerala": {
                "restaurants": {
                    "Kayees Rahmathulla Cafe": {
                        "desc": "Legendary for Kozhikode-style biryani.",
                        "menu": [
                            {"dish": "Kozhikodan Biryani", "price": "₹250", "rating": 4.8},
                            {"dish": "Chicken Roast", "price": "₹180", "rating": 4.5},
                        ],
                    },
                    "Dhe Puttu": {
                        "desc": "Modern take on traditional Kerala breakfast.",
                        "menu": [
                            {"dish": "Puttu & Kadala Curry", "price": "₹140", "rating": 4.6},
                        ],
                    },
                }
            },
            "Maharashtra": {
                "restaurants": {
                    "Shree Thaker Bhojanalay": {
                        "desc": "Classic Gujarati-Maharashtrian unlimited thali.",
                        "menu": [
                            {"dish": "Maharashtrian Thali", "price": "₹350", "rating": 4.6},
                            {"dish": "Puran Poli", "price": "₹90", "rating": 4.4},
                        ],
                    },
                    "Prakash Upahar Kendra": {
                        "desc": "Mumbai's go-to for misal pav.",
                        "menu": [
                            {"dish": "Misal Pav", "price": "₹110", "rating": 4.7},
                        ],
                    },
                }
            },
            "Gujarat": {
                "restaurants": {
                    "Agashiye": {
                        "desc": "Rooftop restaurant serving royal Gujarati thalis.",
                        "menu": [
                            {"dish": "Gujarati Thali", "price": "₹500", "rating": 4.7},
                            {"dish": "Undhiyu", "price": "₹200", "rating": 4.5},
                        ],
                    },
                    "Das Khaman House": {
                        "desc": "Beloved local spot for khaman and fafda.",
                        "menu": [
                            {"dish": "Khaman Dhokla", "price": "₹60", "rating": 4.6},
                        ],
                    },
                }
            },
            "Punjab": {
                "restaurants": {
                    "Kesar Da Dhaba": {
                        "desc": "Century-old dhaba famous for buttery makhani dal.",
                        "menu": [
                            {"dish": "Dal Makhani", "price": "₹220", "rating": 4.8},
                            {"dish": "Amritsari Kulcha", "price": "₹90", "rating": 4.6},
                        ],
                    },
                    "Bharawan Da Dhaba": {
                        "desc": "Traditional Punjabi flavours since 1912.",
                        "menu": [
                            {"dish": "Butter Chicken", "price": "₹320", "rating": 4.7},
                        ],
                    },
                }
            },
            "West Bengal": {
                "restaurants": {
                    "6 Ballygunge Place": {
                        "desc": "Iconic destination for authentic Bengali cuisine.",
                        "menu": [
                            {"dish": "Kosha Mangsho", "price": "₹350", "rating": 4.8},
                            {"dish": "Bhapa Ilish", "price": "₹450", "rating": 4.7},
                        ],
                    },
                    "Balaram Mullick & Radharaman Mullick": {
                        "desc": "Century-old sweet shop famous for Bengali mishti.",
                        "menu": [
                            {"dish": "Rosogolla", "price": "₹15/pc", "rating": 4.9},
                        ],
                    },
                }
            },
            "Rajasthan": {
                "restaurants": {
                    "Chokhi Dhani": {
                        "desc": "Ethnic village-resort experience with royal Rajasthani thali.",
                        "menu": [
                            {"dish": "Rajasthani Thali", "price": "₹600", "rating": 4.6},
                            {"dish": "Dal Baati Churma", "price": "₹250", "rating": 4.7},
                        ],
                    },
                    "Laxmi Misthan Bhandar (LMB)": {
                        "desc": "Jaipur landmark for sweets and snacks since 1727.",
                        "menu": [
                            {"dish": "Pyaaz Kachori", "price": "₹40", "rating": 4.5},
                        ],
                    },
                }
            },
        },
    },
    "Nepal": {
        "flag": "🇳🇵",
        "blurb": "Himalayan flavours built around momos, dal-bhat and thukpa.",
        "regions": {
            "Kathmandu": {
                "restaurants": {
                    "Thakali Kitchen": {
                        "desc": "Authentic Thakali-style set meals.",
                        "menu": [
                            {"dish": "Dal Bhat Set", "price": "NPR 450", "rating": 4.7},
                            {"dish": "Chicken Momo", "price": "NPR 220", "rating": 4.8},
                        ],
                    }
                }
            },
            "Pokhara": {
                "restaurants": {
                    "Godfather's Restaurant": {
                        "desc": "Lakeside favourite for Nepali-Continental fusion.",
                        "menu": [
                            {"dish": "Thukpa", "price": "NPR 350", "rating": 4.6},
                        ],
                    }
                }
            },
            "Lalitpur": {
                "restaurants": {
                    "Bhojan Griha": {
                        "desc": "Traditional Newari cuisine in a heritage house.",
                        "menu": [
                            {"dish": "Newari Khaja Set", "price": "NPR 700", "rating": 4.7},
                        ],
                    }
                }
            },
            "Bhaktapur": {
                "restaurants": {
                    "Café Nyatapola": {
                        "desc": "Views of Nyatapola temple with local snacks.",
                        "menu": [
                            {"dish": "Juju Dhau (Yogurt)", "price": "NPR 150", "rating": 4.5},
                        ],
                    }
                }
            },
            "Chitwan": {
                "restaurants": {
                    "Tharu Kitchen": {
                        "desc": "Indigenous Tharu community cuisine.",
                        "menu": [
                            {"dish": "Ghonghi (Snail curry)", "price": "NPR 300", "rating": 4.3},
                        ],
                    }
                }
            },
        },
    },
    "Bhutan": {
        "flag": "🇧🇹",
        "blurb": "Bold chilies, cheese and hearty mountain fare.",
        "regions": {
            "Thimphu": {
                "restaurants": {
                    "Folk Heritage Restaurant": {
                        "desc": "Traditional Bhutanese thali in a rustic setting.",
                        "menu": [
                            {"dish": "Ema Datshi", "price": "Nu 250", "rating": 4.8},
                        ],
                    }
                }
            },
            "Paro": {
                "restaurants": {
                    "Bukhari Restaurant": {
                        "desc": "Fine dining Bhutanese cuisine near Paro valley.",
                        "menu": [
                            {"dish": "Red Rice with Pork", "price": "Nu 400", "rating": 4.6},
                        ],
                    }
                }
            },
            "Punakha": {
                "restaurants": {
                    "Meri Puensum Resort": {
                        "desc": "River-view dining with organic local produce.",
                        "menu": [
                            {"dish": "Kewa Datshi", "price": "Nu 220", "rating": 4.5},
                        ],
                    }
                }
            },
            "Wangdue": {
                "restaurants": {
                    "Dragon's Nest Cafe": {
                        "desc": "Cosy stop for travellers with local snacks.",
                        "menu": [
                            {"dish": "Momos", "price": "Nu 180", "rating": 4.4},
                        ],
                    }
                }
            },
            "Bumthang": {
                "restaurants": {
                    "Swiss Bakery": {
                        "desc": "Local bakery famous for buckwheat bread.",
                        "menu": [
                            {"dish": "Buckwheat Pancake", "price": "Nu 150", "rating": 4.3},
                        ],
                    }
                }
            },
        },
    },
    "Sri Lanka": {
        "flag": "🇱🇰",
        "blurb": "Coconut, spice-laden curries and fresh seafood.",
        "regions": {
            "Colombo": {
                "restaurants": {
                    "Ministry of Crab": {
                        "desc": "World-renowned seafood restaurant.",
                        "menu": [
                            {"dish": "Sri Lankan Crab Curry", "price": "LKR 4500", "rating": 4.9},
                        ],
                    }
                }
            },
            "Kandy": {
                "restaurants": {
                    "The Empire Cafe": {
                        "desc": "Local favourite for rice and curry sets.",
                        "menu": [
                            {"dish": "Rice & Curry Set", "price": "LKR 900", "rating": 4.5},
                        ],
                    }
                }
            },
            "Galle": {
                "restaurants": {
                    "Poonie's Kitchen": {
                        "desc": "Home-style Sri Lankan cooking near the Fort.",
                        "menu": [
                            {"dish": "Hoppers with Curry", "price": "LKR 700", "rating": 4.6},
                        ],
                    }
                }
            },
            "Jaffna": {
                "restaurants": {
                    "Malayan Cafe": {
                        "desc": "Iconic for authentic Jaffna-style crab curry.",
                        "menu": [
                            {"dish": "Jaffna Crab Curry", "price": "LKR 1800", "rating": 4.8},
                        ],
                    }
                }
            },
            "Negombo": {
                "restaurants": {
                    "Lords Restaurant": {
                        "desc": "Beachside seafood spot popular with travellers.",
                        "menu": [
                            {"dish": "Grilled Prawns", "price": "LKR 1600", "rating": 4.5},
                        ],
                    }
                }
            },
        },
    },
    "Bangladesh": {
        "flag": "🇧🇩",
        "blurb": "River-fed cuisine centred on rice, fish and mustard.",
        "regions": {
            "Dhaka": {
                "restaurants": {
                    "Kasturi Restaurant": {
                        "desc": "Old Dhaka favourite for Mughlai-style biryani.",
                        "menu": [
                            {"dish": "Kacchi Biryani", "price": "BDT 350", "rating": 4.8},
                        ],
                    }
                }
            },
            "Chittagong": {
                "restaurants": {
                    "Well Food": {
                        "desc": "Famous for Chittagonian Mezban beef.",
                        "menu": [
                            {"dish": "Mezbani Beef", "price": "BDT 300", "rating": 4.6},
                        ],
                    }
                }
            },
            "Sylhet": {
                "restaurants": {
                    "Panshi Restaurant": {
                        "desc": "Known for seven-layer tea and local fish curries.",
                        "menu": [
                            {"dish": "Shatkora Beef Curry", "price": "BDT 280", "rating": 4.5},
                        ],
                    }
                }
            },
            "Khulna": {
                "restaurants": {
                    "Royal International": {
                        "desc": "Popular for river fish delicacies.",
                        "menu": [
                            {"dish": "Hilsa Fish Curry", "price": "BDT 400", "rating": 4.7},
                        ],
                    }
                }
            },
            "Rajshahi": {
                "restaurants": {
                    "Radhuni Restaurant": {
                        "desc": "Local favourite for traditional Bengali thalis.",
                        "menu": [
                            {"dish": "Bhuna Khichuri", "price": "BDT 150", "rating": 4.3},
                        ],
                    }
                }
            },
        },
    },
    "Pakistan": {
        "flag": "🇵🇰",
        "blurb": "Rich Mughlai-influenced grills, karahi and biryani.",
        "regions": {
            "Lahore": {
                "restaurants": {
                    "Butt Karahi": {
                        "desc": "Legendary for spicy mutton karahi.",
                        "menu": [
                            {"dish": "Mutton Karahi", "price": "PKR 2200", "rating": 4.8},
                        ],
                    }
                }
            },
            "Karachi": {
                "restaurants": {
                    "Kolachi Restaurant": {
                        "desc": "Seaside dining famous for BBQ platters.",
                        "menu": [
                            {"dish": "Seekh Kebab Platter", "price": "PKR 1800", "rating": 4.6},
                        ],
                    }
                }
            },
            "Islamabad": {
                "restaurants": {
                    "Monal Restaurant": {
                        "desc": "Hilltop dining with a view over the capital.",
                        "menu": [
                            {"dish": "Chicken Tikka", "price": "PKR 1400", "rating": 4.5},
                        ],
                    }
                }
            },
            "Peshawar": {
                "restaurants": {
                    "Namak Mandi": {
                        "desc": "Street-food hub famous for tikka and naan.",
                        "menu": [
                            {"dish": "Peshawari Tikka", "price": "PKR 1000", "rating": 4.7},
                        ],
                    }
                }
            },
            "Multan": {
                "restaurants": {
                    "Chotu Sweets & Restaurant": {
                        "desc": "Renowned for Multani sohan halwa and local dishes.",
                        "menu": [
                            {"dish": "Sohan Halwa", "price": "PKR 500", "rating": 4.4},
                        ],
                    }
                }
            },
        },
    },
    "China": {
        "flag": "🇨🇳",
        "blurb": "Diverse regional cuisines from Sichuan spice to Cantonese dim sum.",
        "regions": {
            "Beijing": {
                "restaurants": {
                    "Quanjude": {
                        "desc": "The original home of Peking Duck since 1864.",
                        "menu": [
                            {"dish": "Peking Duck", "price": "¥288", "rating": 4.8},
                        ],
                    }
                }
            },
            "Shanghai": {
                "restaurants": {
                    "Din Tai Fung": {
                        "desc": "World-famous for delicate soup dumplings.",
                        "menu": [
                            {"dish": "Xiaolongbao", "price": "¥68", "rating": 4.9},
                        ],
                    }
                }
            },
            "Chengdu": {
                "restaurants": {
                    "Chen Mapo Tofu": {
                        "desc": "Birthplace of the iconic mapo tofu dish.",
                        "menu": [
                            {"dish": "Mapo Tofu", "price": "¥38", "rating": 4.7},
                        ],
                    }
                }
            },
            "Guangzhou": {
                "restaurants": {
                    "Guangzhou Restaurant": {
                        "desc": "Century-old institution for Cantonese dim sum.",
                        "menu": [
                            {"dish": "Har Gow (Shrimp Dumplings)", "price": "¥42", "rating": 4.6},
                        ],
                    }
                }
            },
            "Xi'an": {
                "restaurants": {
                    "De Fa Chang": {
                        "desc": "Famous for traditional dumpling banquets.",
                        "menu": [
                            {"dish": "Biang Biang Noodles", "price": "¥30", "rating": 4.5},
                        ],
                    }
                }
            },
        },
    },
    "Myanmar": {
        "flag": "🇲🇲",
        "blurb": "A crossroads cuisine blending Indian, Chinese and Thai influences.",
        "regions": {
            "Yangon": {
                "restaurants": {
                    "Feel Myanmar Food": {
                        "desc": "Buffet-style spot for authentic Burmese curries.",
                        "menu": [
                            {"dish": "Mohinga", "price": "MMK 3000", "rating": 4.7},
                        ],
                    }
                }
            },
            "Mandalay": {
                "restaurants": {
                    "Aye Myit Tar": {
                        "desc": "Popular local chain for Burmese curry sets.",
                        "menu": [
                            {"dish": "Shan Noodles", "price": "MMK 2500", "rating": 4.5},
                        ],
                    }
                }
            },
            "Bagan": {
                "restaurants": {
                    "Black Bamboo": {
                        "desc": "Garden restaurant serving Shan-style specialities.",
                        "menu": [
                            {"dish": "Tea Leaf Salad", "price": "MMK 3500", "rating": 4.6},
                        ],
                    }
                }
            },
            "Naypyidaw": {
                "restaurants": {
                    "Yatha Restaurant": {
                        "desc": "Traditional Burmese dining near the capital.",
                        "menu": [
                            {"dish": "Burmese Fish Curry", "price": "MMK 4000", "rating": 4.4},
                        ],
                    }
                }
            },
            "Taunggyi": {
                "restaurants": {
                    "Lyan Ta Yar": {
                        "desc": "Shan-state specialities including hot pot.",
                        "menu": [
                            {"dish": "Shan Tofu Salad", "price": "MMK 2000", "rating": 4.3},
                        ],
                    }
                }
            },
        },
    },
    "Maldives": {
        "flag": "🇲🇻",
        "blurb": "Tropical island cuisine built around fish, coconut and spice.",
        "regions": {
            "Male": {
                "restaurants": {
                    "Symphony Restaurant": {
                        "desc": "Popular local spot for Maldivian curries.",
                        "menu": [
                            {"dish": "Mas Huni", "price": "MVR 120", "rating": 4.6},
                        ],
                    }
                }
            },
            "Hulhumale": {
                "restaurants": {
                    "Salt Cafe": {
                        "desc": "Casual dining with island seafood specials.",
                        "menu": [
                            {"dish": "Reef Fish Curry", "price": "MVR 220", "rating": 4.5},
                        ],
                    }
                }
            },
            "Addu City": {
                "restaurants": {
                    "Shaviyani Cafe": {
                        "desc": "Local favourite for grilled tuna dishes.",
                        "menu": [
                            {"dish": "Garudhiya (Fish Soup)", "price": "MVR 150", "rating": 4.4},
                        ],
                    }
                }
            },
            "Fuvahmulah": {
                "restaurants": {
                    "Thundi Kitchen": {
                        "desc": "Fresh catch of the day, island-style.",
                        "menu": [
                            {"dish": "Fihunu Mas (Grilled Fish)", "price": "MVR 180", "rating": 4.6},
                        ],
                    }
                }
            },
            "Kulhudhuffushi": {
                "restaurants": {
                    "North Star Cafe": {
                        "desc": "Cosy spot known for coconut-based curries.",
                        "menu": [
                            {"dish": "Coconut Fish Curry", "price": "MVR 200", "rating": 4.3},
                        ],
                    }
                }
            },
        },
    },
    "Thailand": {
        "flag": "🇹🇭",
        "blurb": "A perfect balance of spicy, sour, sweet and salty.",
        "regions": {
            "Bangkok": {
                "restaurants": {
                    "Thipsamai": {
                        "desc": "The most famous Pad Thai restaurant in Bangkok.",
                        "menu": [
                            {"dish": "Pad Thai", "price": "THB 100", "rating": 4.8},
                        ],
                    }
                }
            },
            "Chiang Mai": {
                "restaurants": {
                    "Huen Phen": {
                        "desc": "Authentic Northern Thai (Lanna) cuisine.",
                        "menu": [
                            {"dish": "Khao Soi", "price": "THB 80", "rating": 4.7},
                        ],
                    }
                }
            },
            "Phuket": {
                "restaurants": {
                    "Raya Restaurant": {
                        "desc": "Heritage house serving Phuketian-Peranakan dishes.",
                        "menu": [
                            {"dish": "Moo Hong", "price": "THB 220", "rating": 4.6},
                        ],
                    }
                }
            },
            "Pattaya": {
                "restaurants": {
                    "Mantra Restaurant": {
                        "desc": "Beachfront fusion dining with fresh seafood.",
                        "menu": [
                            {"dish": "Tom Yum Goong", "price": "THB 180", "rating": 4.5},
                        ],
                    }
                }
            },
            "Krabi": {
                "restaurants": {
                    "Ruen Mai Restaurant": {
                        "desc": "Local favourite tucked away serving Thai classics.",
                        "menu": [
                            {"dish": "Green Curry", "price": "THB 150", "rating": 4.4},
                        ],
                    }
                }
            },
        },
    },
}
