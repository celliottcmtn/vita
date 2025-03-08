def get_supplement_priorities():
    """Return priority ratings (1-5) for supplements based on age group and gender
    
    Priority scale:
    1 - May provide minor benefits for some individuals
    2 - Generally beneficial for wellness
    3 - Important for most people
    4 - Very important, especially for specific demographics
    5 - Essential for optimal health in target demographics
    """
    
    supplement_priorities = {
        # Essential Vitamins
        "vitamin_a": {
            "default": 3,
            "age_gender_specific": {
                "20s_female": 3,
                "30s_female": 3,
                "pregnant_female": 4
            }
        },
        "vitamin_b1": {
            "default": 2,
            "age_gender_specific": {
                "40s_male": 3,
                "50s_male": 3,
                "60s_male": 3
            }
        },
        "vitamin_b2": {
            "default": 2,
            "age_gender_specific": {
                "30s_female": 3,
                "40s_female": 3
            }
        },
        "vitamin_b3": {
            "default": 3,
            "age_gender_specific": {
                "50s_male": 4,
                "60s_male": 4
            }
        },
        "vitamin_b5": {
            "default": 2
        },
        "vitamin_b6": {
            "default": 3,
            "age_gender_specific": {
                "20s_female": 4,
                "30s_female": 4,
                "40s_female": 4
            }
        },
        "folate": {
            "default": 3,
            "age_gender_specific": {
                "20s_female": 5,
                "30s_female": 5,
                "pregnant_female": 5
            }
        },
        "vitamin_b12": {
            "default": 4,
            "age_gender_specific": {
                "50s_male": 4,
                "50s_female": 4,
                "60s_male": 5,
                "60s_female": 5,
                "70plus_male": 5,
                "70plus_female": 5
            }
        },
        "biotin": {
            "default": 2
        },
        "vitamin_c": {
            "default": 4
        },
        "vitamin_d": {
            "default": 5,
            "age_gender_specific": {
                "50s_female": 5,
                "60s_female": 5,
                "70plus_female": 5,
                "50s_male": 5,
                "60s_male": 5,
                "70plus_male": 5
            }
        },
        "vitamin_e": {
            "default": 3
        },
        "vitamin_k": {
            "default": 3,
            "age_gender_specific": {
                "50s_female": 4,
                "60s_female": 4,
                "70plus_female": 4
            }
        },
        # Added Supplements
        "taurine": {
            "default": 3,
            "age_gender_specific": {
                "20s_male": 4,
                "30s_male": 4, 
                "40s_male": 4,
                "athletes_male": 5,
                "athletes_female": 5,
                "60s_male": 4,
                "60s_female": 4,
                "70plus_male": 4,
                "70plus_female": 4
            }
        },
        "choline": {
            "default": 3,
            "age_gender_specific": {
                "20s_female": 4,
                "30s_female": 4,
                "pregnant_female": 5,
                "20s_male": 3,
                "30s_male": 3,
                "40s_male": 3,
                "40s_female": 3
            }
        },
