def get_supplement_data():
    """Return the comprehensive supplement database with entries"""
    
    supplements_data = {
        # Essential Vitamins
        "vitamin_a": {
            "name": "Vitamin A",
            "benefits": "Vision health, immune function, skin health, cell growth",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["eye_health", "immune_support", "skin_health"]
            },
            "dosage": {
                "20s": "700-900 mcg RAE daily",
                "30s": "700-900 mcg RAE daily",
                "40s": "700-900 mcg RAE daily",
                "50s": "700-900 mcg RAE daily",
                "60s": "700-900 mcg RAE daily",
                "70plus": "700-900 mcg RAE daily"
            },
            "contraindications": ["pregnancy", "liver_disease"],
            "interactions": ["retinoid_medications", "certain_cholesterol_drugs"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/"]
        },
        "vitamin_b1": {
            "name": "Vitamin B1 (Thiamine)",
            "benefits": "Energy metabolism, nerve function, cognitive health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["fatigue", "cognitive_function", "alcoholism_recovery", "nerve_health"]
            },
            "dosage": {
                "20s": "1.1-1.2 mg daily",
                "30s": "1.1-1.2 mg daily",
                "40s": "1.1-1.2 mg daily",
                "50s": "1.1-1.2 mg daily",
                "60s": "1.1-1.2 mg daily",
                "70plus": "1.1-1.2 mg daily"
            },
            "contraindications": [],
            "interactions": ["certain_diuretics"],
            "sources": ["https://ods.od.nih.gov/factsheets/Thiamin-HealthProfessional/"]
        },
        "vitamin_d": {
            "name": "Vitamin D",
            "benefits": "Bone health, immune function, mood regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "immune_support", "depression", "longevity", "muscle_function"]
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
            "interactions": ["steroids", "weight_loss_drugs", "cholesterol_medication", "seizure_medications"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/"]
        },
        "vitamin_c": {
            "name": "Vitamin C",
            "benefits": "Immune support, antioxidant, collagen production, iron absorption",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "skin_health", "iron_deficiency", "longevity", "wound_healing"]
            },
            "dosage": {
                "20s": "75-90 mg daily",
                "30s": "75-90 mg daily",
                "40s": "75-90 mg daily",
                "50s": "75-90 mg daily",
                "60s": "75-90 mg daily",
                "70plus": "75-90 mg daily (up to 500-1000 mg for immune support)"
            },
            "contraindications": ["history_of_kidney_stones", "hemochromatosis"],
            "interactions": ["blood_thinners", "statins", "chemotherapy", "estrogen"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/"]
        },
        "magnesium": {
            "name": "Magnesium",
            "benefits": "Muscle function, nerve function, energy production, sleep quality",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["muscle_cramps", "sleep_issues", "stress", "heart_health", "longevity", "bone_health"]
            },
            "dosage": {
                "20s": "310-400 mg daily",
                "30s": "310-420 mg daily",
                "40s": "320-420 mg daily",
                "50s": "320-420 mg daily",
                "60s": "320-420 mg daily",
                "70plus": "320-420 mg daily"
            },
            "contraindications": ["kidney_failure", "myasthenia_gravis"],
            "interactions": ["antibiotics", "diuretics", "heart_medication", "bisphosphonates"],
            "sources": ["https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/"]
        },
        "zinc": {
            "name": "Zinc",
            "benefits": "Immune function, wound healing, DNA synthesis, taste and smell",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "skin_health", "reproductive_health", "wound_healing"]
            },
            "dosage": {
                "20s": "8-11 mg daily",
                "30s": "8-11 mg daily",
                "40s": "8-11 mg daily",
                "50s": "8-11 mg daily",
                "60s": "8-11 mg daily",
                "70plus": "8-11 mg daily"
            },
            "contraindications": ["excessive_supplementation"],
            "interactions": ["antibiotics", "penicillamine", "copper_supplements", "iron_supplements"],
            "sources": ["https://ods.od.nih.gov/factsheets/Zinc-HealthProfessional/"]
        },
        "omega_3": {
            "name": "Omega-3 Fatty Acids",
            "benefits": "Heart health, brain function, anti-inflammatory, joint support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "joint_pain", "cognitive_function", "depression", "longevity", "inflammation"]
            },
            "dosage": {
                "20s": "1000-2000 mg daily",
                "30s": "1000-2000 mg daily",
                "40s": "1000-3000 mg daily",
                "50s": "1000-3000 mg daily",
                "60s": "1000-3000 mg daily",
                "70plus": "1000-3000 mg daily"
            },
            "contraindications": ["bleeding_disorders"],
            "interactions": ["blood_thinners", "high_blood_pressure_medication"],
            "sources": ["https://ods.od.nih.gov/factsheets/Omega3FattyAcids-HealthProfessional/"]
        },
        "probiotics": {
            "name": "Probiotics",
            "benefits": "Gut health, immune function, digestion support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["digestive_issues", "antibiotic_recovery", "immune_support", "longevity"]
            },
            "dosage": {
                "20s": "10-30 billion CFU daily",
                "30s": "10-30 billion CFU daily",
                "40s": "10-30 billion CFU daily",
                "50s": "10-30 billion CFU daily",
                "60s": "10-30 billion CFU daily",
                "70plus": "10-30 billion CFU daily"
            },
            "contraindications": ["severe_immunodeficiency"],
            "interactions": ["antibiotics", "immunosuppressants"],
            "sources": ["https://www.nccih.nih.gov/health/probiotics-what-you-need-to-know"]
        },
        "vitamin_b12": {
            "name": "Vitamin B12 (Cobalamin)",
            "benefits": "Nerve function, red blood cell formation, DNA synthesis, energy metabolism",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["fatigue", "vegetarian_vegan", "anemia", "cognitive_function", "nerve_health"]
            },
            "dosage": {
                "20s": "2.4 mcg daily",
                "30s": "2.4 mcg daily",
                "40s": "2.4 mcg daily",
                "50s": "2.4 mcg daily",
                "60s": "2.4-1000 mcg daily",
                "70plus": "2.4-1000 mcg daily (higher doses for absorption issues)"
            },
            "contraindications": [],
            "interactions": ["metformin", "acid_reducers", "colchicine"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/"]
        },
        "iron": {
            "name": "Iron",
            "benefits": "Red blood cell formation, oxygen transport, energy metabolism",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s"],
                "genders": ["female", "prefer_not_to_say"],
                "health_concerns": ["anemia", "fatigue", "heavy_periods", "vegetarian_vegan"]
            },
            "dosage": {
                "20s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "30s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "40s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "50s": "8-18 mg daily (depends on menopause status)",
                "60s": "8 mg daily",
                "70plus": "8 mg daily"
            },
            "contraindications": ["hemochromatosis", "thalassemia"],
            "interactions": ["calcium_supplements", "antacids", "certain_antibiotics", "vitamin_e"],
            "sources": ["https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/"]
        },
        "calcium": {
            "name": "Calcium",
            "benefits": "Bone health, muscle function, nerve transmission, blood vessel function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "osteoporosis_risk", "muscle_function", "heart_health"]
            },
            "dosage": {
                "20s": "1000 mg daily",
                "30s": "1000 mg daily",
                "40s": "1000 mg daily",
                "50s": "1200 mg daily",
                "60s": "1200 mg daily",
                "70plus": "1200 mg daily"
            },
            "contraindications": ["hypercalcemia", "kidney_stones", "certain_heart_conditions"],
            "interactions": ["iron_supplements", "thyroid_medication", "certain_antibiotics", "zinc", "magnesium"],
            "sources": ["https://ods.od.nih.gov/factsheets/Calcium-HealthProfessional/"]
        },
        "vitamin_e": {
            "name": "Vitamin E",
            "benefits": "Antioxidant protection, skin health, immune function, heart and brain health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "heart_health", "longevity", "cognitive_function", "immune_support"]
            },
            "dosage": {
                "20s": "15 mg (22.5 IU) daily",
                "30s": "15 mg (22.5 IU) daily",
                "40s": "15 mg (22.5 IU) daily",
                "50s": "15 mg (22.5 IU) daily",
                "60s": "15 mg (22.5 IU) daily",
                "70plus": "15 mg (22.5 IU) daily"
            },
            "contraindications": ["vitamin_k_deficiency", "bleeding_disorders"],
            "interactions": ["blood_thinners", "certain_chemotherapy_drugs", "statins"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/"]
        }
    }
    
    return supplements_data

def get_interactions_data():
    """Return the comprehensive interactions data for supplements"""
    
    interactions_data = {
        "calcium": ["iron", "zinc", "magnesium", "manganese"],
        "iron": ["calcium", "vitamin_e", "zinc", "green_tea", "quercetin"],
        "zinc": ["calcium", "iron", "copper", "folate", "tetracycline_antibiotics"],
        "magnesium": ["calcium", "potassium", "vitamin_d", "bisphosphonates", "fluoroquinolone_antibiotics"],
        "vitamin_c": ["vitamin_b12", "copper", "statins", "chemotherapy_drugs"],
        "vitamin_e": ["vitamin_k", "blood_thinners", "statins", "chemotherapy_drugs"],
        "vitamin_d": ["calcium", "magnesium", "corticosteroids", "weight_loss_drugs", "seizure_medications"],
        "vitamin_b12": ["vitamin_c", "acid_reducers", "metformin", "colchicine", "potassium_supplements"],
        "probiotics": ["antibiotics", "immunosuppressants", "antifungals"],
        "omega_3": ["blood_thinners", "vitamin_e", "ginkgo_biloba", "aspirin", "nsaids"],
        "vitamin_a": ["retinoid_medications", "certain_cholesterol_drugs", "tetracycline_antibiotics"]
    }
    
    return interactions_data

def get_age_health_concerns():
    """Return the expanded age and gender-specific health concerns"""
    
    age_health_concerns = {
        "20s": {
            "male": ["immune_support", "fitness_performance", "stress", "energy_levels", "mental_clarity", "digestive_health", "sleep_quality", "muscle_growth"],
            "female": ["immune_support", "iron_deficiency", "stress", "reproductive_health", "skin_health", "digestive_health", "sleep_quality", "hormone_balance"],
            "prefer_not_to_say": ["immune_support", "stress", "fitness_performance", "energy_levels", "digestive_health", "mental_clarity", "sleep_quality"]
        },
        "30s": {
            "male": ["energy_levels", "stress", "immune_support", "fitness_performance", "metabolism_support", "cardiovascular_health", "digestive_health", "fertility"],
            "female": ["energy_levels", "stress", "reproductive_health", "iron_deficiency", "metabolism_support", "skin_health", "digestive_health", "fertility"],
            "prefer_not_to_say": ["energy_levels", "stress", "immune_support", "fitness_performance", "metabolism_support", "digestive_health"]
        },
        "40s": {
            "male": ["heart_health", "energy_levels", "stress", "longevity", "weight_management", "prostate_health", "muscle_maintenance", "metabolic_health", "vision_support"],
            "female": ["energy_levels", "stress", "bone_health", "hormone_balance", "weight_management", "breast_health", "metabolic_health", "vision_support", "digestive_health"],
            "prefer_not_to_say": ["energy_levels", "stress", "heart_health", "longevity", "weight_management", "metabolic_health", "joint_health", "vision_support"]
        },
        "50s": {
            "male": ["heart_health", "prostate_health", "joint_pain", "cognitive_function", "longevity", "blood_sugar_balance", "vision_support", "stress_management", "immune_function"],
            "female": ["bone_health", "hormone_balance", "heart_health", "joint_pain", "longevity", "blood_sugar_balance", "vision_support", "weight_management", "cognitive_function"],
            "prefer_not_to_say": ["heart_health", "joint_pain", "cognitive_function", "longevity", "bone_health", "blood_sugar_balance", "vision_support", "stress_management"]
        },
        "60s": {
            "male": ["heart_health", "joint_pain", "cognitive_function", "prostate_health", "longevity", "bone_density", "muscle_preservation", "immune_resilience", "digestive_efficiency"],
            "female": ["bone_health", "heart_health", "joint_pain", "cognitive_function", "longevity", "bladder_function", "immune_resilience", "skin_elasticity", "vision_health"],
            "prefer_not_to_say": ["heart_health", "joint_pain", "cognitive_function", "longevity", "bone_health", "immune_resilience", "digestive_efficiency", "sleep_quality"]
        },
        "70plus": {
            "male": ["heart_health", "cognitive_function", "bone_health", "immune_support", "longevity", "digestive_function", "physical_mobility", "muscle_maintenance", "prostate_health", "vision_health"],
            "female": ["bone_health", "heart_health", "cognitive_function", "immune_support", "longevity", "physical_mobility", "digestive_function", "bladder_health", "vision_health", "skin_integrity"],
            "prefer_not_to_say": ["heart_health", "cognitive_function", "bone_health", "immune_support", "longevity", "physical_mobility", "digestive_function", "sleep_quality", "vision_health"]
        }
    }
    
    return age_health_concerns
