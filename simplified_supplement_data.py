def get_supplement_data():
    """Return basic supplement data"""
    supplements_data = {
        "vitamin_c": {
            "name": "Vitamin C",
            "benefits": "Immune support, antioxidant, collagen production, iron absorption",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "skin_health", "iron_deficiency", "longevity"]
            },
            "dosage": {
                "20s": "75-90 mg daily",
                "30s": "75-90 mg daily",
                "40s": "75-90 mg daily",
                "50s": "75-90 mg daily",
                "60s": "75-90 mg daily",
                "70plus": "75-90 mg daily (up to 500-1000 mg for immune support)"
            },
            "contraindications": ["history_of_kidney_stones"],
            "interactions": ["blood_thinners", "statins", "chemotherapy"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Ascorbic acid tablets",
                    "note": "Basic form for general immune support"
                },
                "good": {
                    "form": "Buffered vitamin C with bioflavonoids",
                    "note": "Gentler on stomach with enhanced absorption"
                },
                "ideal": {
                    "form": "Liposomal vitamin C or whole-food vitamin C complex",
                    "note": "Superior absorption and cellular delivery"
                }
            }
        },
        "vitamin_d": {
            "name": "Vitamin D",
            "benefits": "Bone health, immune function, mood regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "immune_support", "depression", "longevity"]
            },
            "dosage": {
                "20s": "1000-2000 IU daily",
                "30s": "1000-2000 IU daily",
                "40s": "1000-2000 IU daily",
                "50s": "1000-4000 IU daily",
                "60s": "1000-4000 IU daily",
                "70plus": "2000-4000 IU daily"
            },
            "contraindications": ["hypercalcemia", "kidney_disease"],
            "interactions": ["steroids", "weight_loss_drugs", "cholesterol_medication"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "D3 tablets",
                    "note": "Basic supplementation for most people"
                },
                "good": {
                    "form": "D3 + K2 combination",
                    "note": "Synergistic effects for calcium metabolism"
                },
                "ideal": {
                    "form": "Liposomal D3 + K2 with organic oils",
                    "note": "Maximum absorption and utilization"
                }
            }
        },
        "magnesium": {
            "name": "Magnesium",
            "benefits": "Muscle function, nerve function, energy production, sleep quality",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["muscle_cramps", "sleep_issues", "stress", "heart_health", "longevity"]
            },
            "dosage": {
                "20s": "310-400 mg daily",
                "30s": "310-420 mg daily",
                "40s": "320-420 mg daily",
                "50s": "320-420 mg daily",
                "60s": "320-420 mg daily",
                "70plus": "320-420 mg daily"
            },
            "contraindications": ["kidney_failure"],
            "interactions": ["antibiotics", "diuretics", "heart_medication"],
            "sources": ["https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Magnesium oxide",
                    "note": "Basic form with lower bioavailability"
                },
                "good": {
                    "form": "Magnesium citrate or glycinate",
                    "note": "Higher bioavailability with less GI distress"
                },
                "ideal": {
                    "form": "Magnesium threonate or glycinate complex with B6",
                    "note": "Superior bioavailability with brain and nervous system benefits"
                }
            }
        }
    }
    
    return supplements_data

def get_interactions_data():
    """Return the interactions data for supplements"""
    
    interactions_data = {
        "calcium": ["iron", "zinc", "magnesium"],
        "iron": ["calcium", "zinc"],
        "zinc": ["calcium", "iron", "copper"],
        "magnesium": ["calcium"],
        "vitamin_c": ["b12"],
        "vitamin_e": ["vitamin_k"]
    }
    
    return interactions_data

def get_age_health_concerns():
    """Return the age and gender-specific health concerns"""
    
    age_health_concerns = {
        "20s": {
            "male": ["immune_support", "fitness_performance", "stress", "energy_levels"],
            "female": ["immune_support", "iron_deficiency", "stress", "reproductive_health"],
            "prefer_not_to_say": ["immune_support", "stress", "fitness_performance", "energy_levels"]
        },
        "30s": {
            "male": ["energy_levels", "stress", "immune_support", "fitness_performance"],
            "female": ["energy_levels", "stress", "reproductive_health", "iron_deficiency"],
            "prefer_not_to_say": ["energy_levels", "stress", "immune_support", "fitness_performance"]
        },
        "40s": {
            "male": ["heart_health", "energy_levels", "stress", "longevity", "weight_management"],
            "female": ["energy_levels", "stress", "bone_health", "hormone_balance", "weight_management"],
            "prefer_not_to_say": ["energy_levels", "stress", "heart_health", "longevity", "weight_management"]
        },
        "50s": {
            "male": ["heart_health", "prostate_health", "joint_pain", "cognitive_function", "longevity"],
            "female": ["bone_health", "hormone_balance", "heart_health", "joint_pain", "longevity"],
            "prefer_not_to_say": ["heart_health", "joint_pain", "cognitive_function", "longevity", "bone_health"]
        },
        "60s": {
            "male": ["heart_health", "joint_pain", "cognitive_function", "prostate_health", "longevity"],
            "female": ["bone_health", "heart_health", "joint_pain", "cognitive_function", "longevity"],
            "prefer_not_to_say": ["heart_health", "joint_pain", "cognitive_function", "longevity", "bone_health"]
        },
        "70plus": {
            "male": ["heart_health", "cognitive_function", "bone_health", "immune_support", "longevity"],
            "female": ["bone_health", "heart_health", "cognitive_function", "immune_support", "longevity"],
            "prefer_not_to_say": ["heart_health", "cognitive_function", "bone_health", "immune_support", "longevity"]
        }
    }
    
    return age_health_concerns
