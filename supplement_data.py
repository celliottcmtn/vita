def get_supplement_data():
    """Return a simplified supplement database"""
    supplements_data = {
        "vitamin_d": {
            "name": "Vitamin D",
            "benefits": "Bone health, immune function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "immune_support"]
            },
            "dosage": {
                "20s": "1000-2000 IU daily",
                "30s": "1000-2000 IU daily", 
                "40s": "1000-2000 IU daily",
                "50s": "1000-4000 IU daily",
                "60s": "1000-4000 IU daily",
                "70plus": "2000-4000 IU daily"
            },
            "contraindications": ["kidney_disease"],
            "interactions": ["steroids"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "D3 tablets",
                    "price_range": "$5-15"
                },
                "good": {
                    "form": "D3 + K2",
                    "price_range": "$15-25"
                },
                "ideal": {
                    "form": "Liposomal D3",
                    "price_range": "$25-40"
                }
            }
        },
        "magnesium": {
            "name": "Magnesium",
            "benefits": "Muscle function, sleep",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["sleep_issues", "muscle_cramps"]
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
            "interactions": ["antibiotics"],
            "sources": ["https://ods.od.nih.gov/factsheets/Magnes
