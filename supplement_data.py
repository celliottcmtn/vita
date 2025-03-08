def get_supplement_data():
    """Return the comprehensive supplement database with 60+ entries"""
    
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
        "vitamin_b2": {
            "name": "Vitamin B2 (Riboflavin)",
            "benefits": "Energy metabolism, cellular function, antioxidant activity",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["migraines", "fatigue", "eye_health", "energy_metabolism"]
            },
            "dosage": {
                "20s": "1.1-1.3 mg daily",
                "30s": "1.1-1.3 mg daily",
                "40s": "1.1-1.3 mg daily",
                "50s": "1.1-1.3 mg daily",
                "60s": "1.1-1.3 mg daily",
                "70plus": "1.1-1.3 mg daily"
            },
            "contraindications": [],
            "interactions": ["antacids", "tricyclic_antidepressants"],
            "sources": ["https://ods.od.nih.gov/factsheets/Riboflavin-HealthProfessional/"]
        },
        "vitamin_b3": {
            "name": "Vitamin B3 (Niacin)",
            "benefits": "Energy metabolism, skin health, cholesterol management",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cholesterol_management", "skin_health", "energy_metabolism", "joint_mobility"]
            },
            "dosage": {
                "20s": "14-16 mg daily",
                "30s": "14-16 mg daily",
                "40s": "14-16 mg daily",
                "50s": "14-16 mg daily",
                "60s": "14-16 mg daily",
                "70plus": "14-16 mg daily"
            },
            "contraindications": ["liver_disease", "ulcers", "gout"],
            "interactions": ["statins", "diabetes_medications", "blood_pressure_medications"],
            "sources": ["https://ods.od.nih.gov/factsheets/Niacin-HealthProfessional/"]
        },
        "vitamin_b5": {
            "name": "Vitamin B5 (Pantothenic Acid)",
            "benefits": "Energy metabolism, hormone synthesis, stress response, skin health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["stress", "energy_metabolism", "skin_health", "adrenal_support"]
            },
            "dosage": {
                "20s": "5 mg daily",
                "30s": "5 mg daily",
                "40s": "5 mg daily",
                "50s": "5 mg daily",
                "60s": "5 mg daily",
                "70plus": "5 mg daily"
            },
            "contraindications": [],
            "interactions": ["certain_antibiotics"],
            "sources": ["https://ods.od.nih.gov/factsheets/PantothenicAcid-HealthProfessional/"]
        },
        "vitamin_b6": {
            "name": "Vitamin B6 (Pyridoxine)",
            "benefits": "Protein metabolism, cognitive development, immune function, hemoglobin formation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["pms_symptoms", "immune_support", "cognitive_function", "heart_health", "morning_sickness"]
            },
            "dosage": {
                "20s": "1.3 mg daily",
                "30s": "1.3 mg daily",
                "40s": "1.3 mg daily",
                "50s": "1.5-1.7 mg daily",
                "60s": "1.5-1.7 mg daily",
                "70plus": "1.5-1.7 mg daily"
            },
            "contraindications": ["high_doses_can_cause_neuropathy"],
            "interactions": ["certain_antibiotics", "anti_seizure_medications", "estrogen"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminB6-HealthProfessional/"]
        },
        "folate": {
            "name": "Folate (Vitamin B9)",
            "benefits": "DNA synthesis, cell division, red blood cell formation, neural tube development",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["pregnancy_support", "heart_health", "cognitive_function", "anemia", "depression"]
            },
            "dosage": {
                "20s": "400 mcg daily (600-800 mcg for pregnant women)",
                "30s": "400 mcg daily (600-800 mcg for pregnant women)",
                "40s": "400 mcg daily",
                "50s": "400 mcg daily",
                "60s": "400 mcg daily",
                "70plus": "400 mcg daily"
            },
            "contraindications": ["vitamin_b12_deficiency"],
            "interactions": ["methotrexate", "anticonvulsants", "sulfasalazine"],
            "sources": ["https://ods.od.nih.gov/factsheets/Folate-HealthProfessional/"]
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
        "biotin": {
            "name": "Biotin (Vitamin B7)",
            "benefits": "Energy metabolism, hair health, skin health, nail strength",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["hair_health", "skin_health", "nail_health", "metabolism_support"]
            },
            "dosage": {
                "20s": "30 mcg daily",
                "30s": "30 mcg daily",
                "40s": "30 mcg daily",
                "50s": "30 mcg daily",
                "60s": "30 mcg daily",
                "70plus": "30 mcg daily"
            },
            "contraindications": [],
            "interactions": ["anticonvulsants", "can_interfere_with_lab_tests"],
            "sources": ["https://ods.od.nih.gov/factsheets/Biotin-HealthProfessional/"]
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
        },
        "vitamin_k": {
            "name": "Vitamin K",
            "benefits": "Blood clotting, bone health, cardiovascular health, calcium regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "heart_health", "osteoporosis_risk", "longevity", "blood_health"]
            },
            "dosage": {
                "20s": "90-120 mcg daily",
                "30s": "90-120 mcg daily",
                "40s": "90-120 mcg daily",
                "50s": "90-180 mcg daily",
                "60s": "90-180 mcg daily",
                "70plus": "90-180 mcg daily"
            },
            "contraindications": ["taking_warfarin"],
            "interactions": ["blood_thinners", "certain_antibiotics", "weight_loss_drugs", "vitamin_e"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminK-HealthProfessional/"]
        },
        # Minerals
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
        "selenium": {
            "name": "Selenium",
            "benefits": "Antioxidant protection, thyroid function, immune support, reproductive health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["thyroid_health", "immune_support", "antioxidant_support", "heart_health", "male_fertility"]
            },
            "dosage": {
                "20s": "55 mcg daily",
                "30s": "55 mcg daily",
                "40s": "55 mcg daily",
                "50s": "55 mcg daily",
                "60s": "55 mcg daily",
                "70plus": "55 mcg daily"
            },
            "contraindications": ["excess_can_be_toxic"],
            "interactions": ["statins", "niacin", "chemotherapy_drugs"],
            "sources": ["https://ods.od.nih.gov/factsheets/Selenium-HealthProfessional/"]
        },
        "iodine": {
            "name": "Iodine",
            "benefits": "Thyroid function, metabolic regulation, cognitive development, immune support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["thyroid_health", "energy_levels", "cognitive_function", "breast_health", "pregnancy_support"]
            },
            "dosage": {
                "20s": "150 mcg daily",
                "30s": "150 mcg daily",
                "40s": "150 mcg daily",
                "50s": "150 mcg daily",
                "60s": "150 mcg daily",
                "70plus": "150 mcg daily"
            },
            "contraindications": ["hashimotos_thyroiditis", "graves_disease"],
            "interactions": ["thyroid_medications", "lithium", "antithyroid_drugs"],
            "sources": ["https://ods.od.nih.gov/factsheets/Iodine-HealthProfessional/"]
        },
        "copper": {
            "name": "Copper",
            "benefits": "Iron metabolism, connective tissue formation, nerve function, antioxidant activity",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["joint_health", "cardiovascular_health", "hair_pigmentation", "energy_metabolism", "immune_support"]
            },
            "dosage": {
                "20s": "900 mcg daily",
                "30s": "900 mcg daily",
                "40s": "900 mcg daily",
                "50s": "900 mcg daily",
                "60s": "900 mcg daily",
                "70plus": "900 mcg daily"
            },
            "contraindications": ["wilson_disease"],
            "interactions": ["zinc_supplements", "vitamin_c_high_doses", "penicillamine"],
            "sources": ["https://ods.od.nih.gov/factsheets/Copper-HealthProfessional/"]
        },
        "manganese": {
            "name": "Manganese",
            "benefits": "Enzyme function, bone formation, blood clotting, inflammation reduction",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "metabolism", "joint_health", "blood_sugar_management", "antioxidant_support"]
            },
            "dosage": {
                "20s": "1.8-2.3 mg daily",
                "30s": "1.8-2.3 mg daily",
                "40s": "1.8-2.3 mg daily",
                "50s": "1.8-2.3 mg daily",
                "60s": "1.8-2.3 mg daily",
                "70plus": "1.8-2.3 mg daily"
            },
            "contraindications": ["liver_disease", "iron_deficiency_anemia"],
            "interactions": ["certain_antibiotics", "antacids", "iron_supplements"],
            "sources": ["https://ods.od.nih.gov/factsheets/Manganese-HealthProfessional/"]
        },
        "chromium": {
            "name": "Chromium",
            "benefits": "Blood sugar regulation, macronutrient metabolism, insulin sensitivity",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["blood_sugar_management", "weight_management", "energy_metabolism", "cardiovascular_health"]
            },
            "dosage": {
                "20s": "25-35 mcg daily",
                "30s": "25-35 mcg daily",
                "40s": "25-35 mcg daily",
                "50s": "25-35 mcg daily",
                "60s": "25-35 mcg daily",
                "70plus": "25-35 mcg daily"
            },
            "contraindications": ["kidney_disease", "liver_disease"],
            "interactions": ["insulin", "other_diabetes_medications", "NSAIDs", "beta_blockers"],
            "sources": ["https://ods.od.nih.gov/factsheets/Chromium-HealthProfessional/"]
        },
        "potassium": {
            "name": "Potassium",
            "benefits": "Blood pressure regulation, muscle function, nerve signaling, fluid balance",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "blood_pressure", "muscle_cramps", "exercise_recovery", "electrolyte_balance"]
            },
            "dosage": {
                "20s": "2500-3400 mg daily (from food and supplements)",
                "30s": "2500-3400 mg daily (from food and supplements)",
                "40s": "2500-3400 mg daily (from food and supplements)",
                "50s": "2500-3400 mg daily (from food and supplements)",
                "60s": "2500-3400 mg daily (from food and supplements)",
                "70plus": "2500-3400 mg daily (from food and supplements)"
            },
            "contraindications": ["kidney_disease", "taking_potassium_sparing_diuretics", "adrenal_insufficiency"],
            "interactions": ["ACE_inhibitors", "potassium_sparing_diuretics", "blood_pressure_medications", "nsaids"],
            "sources": ["https://ods.od.nih.gov/factsheets/Potassium-HealthProfessional/"]
        },
        "molybdenum": {
            "name": "Molybdenum",
            "benefits": "Enzyme function, detoxification, sulfite metabolism",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["detoxification_support", "sulfite_sensitivity", "liver_health", "alcohol_metabolism"]
            },
            "dosage": {
                "20s": "45 mcg daily",
                "30s": "45 mcg daily",
                "40s": "45 mcg daily",
                "50s": "45 mcg daily",
                "60s": "45 mcg daily",
                "70plus": "45 mcg daily"
            },
            "contraindications": ["gout"],
            "interactions": ["copper_absorption", "sulfite_containing_medications"],
            "sources": ["https://ods.od.nih.gov/factsheets/Molybdenum-HealthProfessional/"]
        },
        # Fatty Acids
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
        "omega_6": {
            "name": "Omega-6 (GLA)",
            "benefits": "Skin health, hormonal balance, inflammation regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "pms_symptoms", "hormone_balance", "inflammation", "eczema", "rheumatoid_arthritis"]
            },
            "dosage": {
                "20s": "500-1000 mg daily",
                "30s": "500-1000 mg daily",
                "40s": "500-1000 mg daily",
                "50s": "500-1000 mg daily",
                "60s": "500-1000 mg daily",
                "70plus": "500-1000 mg daily"
            },
            "contraindications": ["seizure_disorders", "bleeding_disorders"],
            "interactions": ["blood_thinners", "anti_inflammatory_drugs", "epilepsy_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3257651/"]
        },
        "cla": {
            "name": "Conjugated Linoleic Acid (CLA)",
            "benefits": "Weight management, muscle retention, anti-inflammatory properties",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["weight_management", "body_composition", "inflammation", "metabolic_health"]
            },
            "dosage": {
                "20s": "3-6 g daily",
                "30s": "3-6 g daily",
                "40s": "3-6 g daily",
                "50s": "3-6 g daily",
                "60s": "3-6 g daily",
                "70plus": "3-6 g daily"
            },
            "contraindications": ["insulin_resistance", "diabetes", "metabolic_syndrome"],
            "interactions": ["diabetes_medications", "blood_pressure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2826589/"]
        },
        # Probiotics
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
        "prebiotics": {
            "name": "Prebiotics",
            "benefits": "Gut microbiome support, digestive health, immune function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["digestive_issues", "gut_health", "immune_support", "weight_management"]
            },
            "dosage": {
                "20s": "3-5 g daily",
                "30s": "3-5 g daily",
                "40s": "3-5 g daily",
                "50s": "3-5 g daily",
                "60s": "3-5 g daily",
                "70plus": "3-5 g daily"
            },
            "contraindications": ["FODMAP_sensitivity", "certain_IBS_cases"],
            "interactions": [],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6041804/"]
        },
        # Antioxidants and Specialized Nutrients
        "coq10": {
            "name": "Coenzyme Q10 (CoQ10)",
            "benefits": "Cellular energy production, antioxidant, heart health, anti-aging",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "fatigue", "statin_users", "longevity", "migraine_prevention", "gum_health", "exercise_performance"]
            },
            "dosage": {
                "40s": "100-200 mg daily",
                "50s": "100-200 mg daily",
                "60s": "100-300 mg daily",
                "70plus": "100-300 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "insulin", "chemotherapy", "beta_blockers"],
            "sources": ["https://www.mayoclinic.org/drugs-supplements-coenzyme-q10/art-20362602"]
        },
        "alpha_lipoic_acid": {
            "name": "Alpha Lipoic Acid (ALA)",
            "benefits": "Antioxidant, glucose metabolism, nerve health, liver support",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["nerve_health", "blood_sugar_management", "liver_health", "longevity", "skin_health", "metabolic_syndrome"]
            },
            "dosage": {
                "30s": "300-600 mg daily",
                "40s": "300-600 mg daily",
                "50s": "300-600 mg daily",
                "60s": "300-600 mg daily",
                "70plus": "300-600 mg daily"
            },
            "contraindications": ["thiamine_deficiency"],
            "interactions": ["diabetes_medications", "chemotherapy", "thyroid_medications", "vitamin_b1"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6723188/"]
        },
        "dhea": {
            "name": "DHEA",
            "benefits": "Hormone precursor, adrenal support, anti-aging, immune function",
            "recommended_for": {
                "age_groups": ["50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["hormone_balance", "bone_health", "adrenal_support", "longevity", "autoimmune_conditions", "mood_support"]
            },
            "dosage": {
                "50s": "25-50 mg daily",
                "60s": "25-50 mg daily",
                "70plus": "25-50 mg daily"
            },
            "contraindications": ["hormone_sensitive_cancers", "liver_disease", "PCOS", "pregnancy"],
            "interactions": ["hormone_therapies", "anticoagulants", "insulin", "antidepressants"],
            "sources": ["https://www.mayoclinic.org/drugs-supplements-dhea/art-20364199"]
        },
        "pqq": {
            "name": "Pyrroloquinoline Quinone (PQQ)",
            "benefits": "Mitochondrial biogenesis, neuroprotection, antioxidant, energy production",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "cognitive_function", "energy_levels", "longevity", "mitochondrial_health"]
            },
            "dosage": {
                "40s": "10-20 mg daily",
                "50s": "10-20 mg daily",
                "60s": "10-20 mg daily",
                "70plus": "10-20 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "certain_medications_metabolized_by_liver"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2908954/"]
        },
        "nac": {
            "name": "N-Acetyl Cysteine (NAC)",
            "benefits": "Antioxidant, liver support, respiratory health, detoxification",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["liver_health", "respiratory_health", "detoxification", "immune_support", "addiction_support", "mental_health"]
            },
            "dosage": {
                "20s": "600-1200 mg daily",
                "30s": "600-1200 mg daily",
                "40s": "600-1200 mg daily",
                "50s": "600-1200 mg daily",
                "60s": "600-1200 mg daily",
                "70plus": "600-1200 mg daily"
            },
            "contraindications": ["asthma_in_some_cases"],
            "interactions": ["nitroglycerin", "blood_thinners", "certain_cancer_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5241507/"]
        },
        "resveratrol": {
            "name": "Resveratrol",
            "benefits": "Antioxidant, longevity, cardiovascular health, blood sugar regulation",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "longevity", "blood_sugar_management", "cognitive_function", "inflammation"]
            },
            "dosage": {
                "30s": "100-500 mg daily",
                "40s": "100-500 mg daily",
                "50s": "100-500 mg daily",
                "60s": "100-500 mg daily",
                "70plus": "100-500 mg daily"
            },
            "contraindications": ["bleeding_disorders", "hormone_sensitive_conditions"],
            "interactions": ["blood_thinners", "certain_medications_metabolized_by_liver", "estrogen_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6164842/"]
        },
        "glutathione": {
            "name": "Glutathione",
            "benefits": "Master antioxidant, detoxification, immune support, skin health",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["detoxification", "immune_support", "skin_health", "liver_health", "respiratory_health", "neurodegeneration"]
            },
            "dosage": {
                "30s": "250-500 mg daily",
                "40s": "250-500 mg daily",
                "50s": "250-500 mg daily",
                "60s": "250-500 mg daily",
                "70plus": "250-500 mg daily"
            },
            "contraindications": ["asthma_in_some_cases"],
            "interactions": ["immunosuppressants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6596244/"]
        },
        "astaxanthin": {
            "name": "Astaxanthin",
            "benefits": "Powerful antioxidant, skin health, eye health, anti-inflammatory",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "eye_health", "joint_pain", "exercise_recovery", "longevity", "brain_health", "cardiovascular_health"]
            },
            "dosage": {
                "30s": "4-12 mg daily",
                "40s": "4-12 mg daily",
                "50s": "4-12 mg daily",
                "60s": "4-12 mg daily",
                "70plus": "4-12 mg daily"
            },
            "contraindications": [],
            "interactions": ["hormone_therapies", "medications_metabolized_by_liver", "blood_pressure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5946307/"]
        },
        "lutein_zeaxanthin": {
            "name": "Lutein & Zeaxanthin",
            "benefits": "Eye health, macular protection, cognitive function, skin health",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["eye_health", "vision_support", "cognitive_function", "skin_health", "brain_health"]
            },
            "dosage": {
                "30s": "10-20 mg lutein and 2-4 mg zeaxanthin daily",
                "40s": "10-20 mg lutein and 2-4 mg zeaxanthin daily",
                "50s": "10-20 mg lutein and 2-4 mg zeaxanthin daily",
                "60s": "10-20 mg lutein and 2-4 mg zeaxanthin daily",
                "70plus": "10-20 mg lutein and 2-4 mg zeaxanthin daily"
            },
            "contraindications": [],
            "interactions": ["smoking_may_reduce_efficacy"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6164534/"]
        },
        "lycopene": {
            "name": "Lycopene",
            "benefits": "Prostate health, cardiovascular health, skin protection, antioxidant",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["prostate_health", "heart_health", "skin_health", "sun_protection", "longevity"]
            },
            "dosage": {
                "30s": "6-15 mg daily",
                "40s": "6-15 mg daily",
                "50s": "6-30 mg daily",
                "60s": "6-30 mg daily",
                "70plus": "6-30 mg daily"
            },
            "contraindications": [],
            "interactions": ["lycopene_absorption_reduced_by_beta_carotene"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6073292/"]
        },
        # Herbs & Botanicals
        "ashwagandha": {
            "name": "Ashwagandha",
            "benefits": "Stress reduction, thyroid support, muscle strength, cognitive function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["stress", "thyroid_health", "muscle_strength", "cognitive_function", "sleep_quality", "hormone_balance"]
            },
            "dosage": {
                "20s": "300-600 mg daily",
                "30s": "300-600 mg daily",
                "40s": "300-600 mg daily",
                "50s": "300-600 mg daily",
                "60s": "300-600 mg daily",
                "70plus": "300-600 mg daily"
            },
            "contraindications": ["pregnancy", "autoimmune_conditions", "certain_hormone_sensitive_cancers"],
            "interactions": ["thyroid_medications", "sedatives", "immunosuppressants", "blood_pressure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6979308/"]
        },
        "turmeric_curcumin": {
            "name": "Turmeric/Curcumin",
            "benefits": "Anti-inflammatory, antioxidant, joint health, cognitive support, digestive health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["inflammation", "joint_pain", "cognitive_function", "digestive_health", "heart_health", "skin_health"]
            },
            "dosage": {
                "20s": "500-1000 mg curcumin daily",
                "30s": "500-1000 mg curcumin daily",
                "40s": "500-1000 mg curcumin daily",
                "50s": "500-1500 mg curcumin daily",
                "60s": "500-1500 mg curcumin daily",
                "70plus": "500-1500 mg curcumin daily"
            },
            "contraindications": ["gallbladder_disease", "blood_clotting_disorders", "scheduled_surgery"],
            "interactions": ["blood_thinners", "diabetes_medications", "certain_chemotherapy_drugs"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5664031/"]
        },
        "ginkgo_biloba": {
            "name": "Ginkgo Biloba",
            "benefits": "Cognitive function, circulation, eye health, tinnitus relief",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cognitive_function", "circulation", "eye_health", "tinnitus", "vertigo", "memory_support"]
            },
            "dosage": {
                "40s": "120-240 mg daily",
                "50s": "120-240 mg daily",
                "60s": "120-240 mg daily",
                "70plus": "120-240 mg daily"
            },
            "contraindications": ["bleeding_disorders", "seizure_disorders", "scheduled_surgery", "pregnancy"],
            "interactions": ["blood_thinners", "NSAIDs", "certain_antidepressants", "seizure_medications"],
            "sources": ["https://www.nccih.nih.gov/health/ginkgo"]
        },
        "rhodiola": {
            "name": "Rhodiola Rosea",
            "benefits": "Stress adaptation, energy, mental performance, exercise recovery",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["stress", "fatigue", "cognitive_function", "exercise_recovery", "mood_support", "altitude_sickness"]
            },
            "dosage": {
                "20s": "200-600 mg daily",
                "30s": "200-600 mg daily",
                "40s": "200-600 mg daily",
                "50s": "200-600 mg daily",
                "60s": "200-600 mg daily",
                "70plus": "200-600 mg daily"
            },
            "contraindications": ["bipolar_disorder", "hormonal_cancers"],
            "interactions": ["blood_pressure_medications", "diabetes_medications", "immunosuppressants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5674483/"]
        },
        "bacopa": {
            "name": "Bacopa Monnieri",
            "benefits": "Cognitive enhancement, memory, anxiety reduction, neuroprotection",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cognitive_function", "memory_support", "stress", "brain_health", "focus_and_attention"]
            },
            "dosage": {
                "20s": "300-600 mg daily",
                "30s": "300-600 mg daily",
                "40s": "300-600 mg daily",
                "50s": "300-600 mg daily",
                "60s": "300-600 mg daily",
                "70plus": "300-600 mg daily"
            },
            "contraindications": ["pregnancy", "breastfeeding", "slow_heart_rate"],
            "interactions": ["thyroid_medications", "calcium_channel_blockers", "anticonvulsants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3746283/"]
        },
        "milk_thistle": {
            "name": "Milk Thistle",
            "benefits": "Liver support, detoxification, antioxidant, skin health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["liver_health", "detoxification", "skin_health", "diabetes_support", "alcoholism_recovery"]
            },
            "dosage": {
                "20s": "140-800 mg silymarin daily",
                "30s": "140-800 mg silymarin daily",
                "40s": "140-800 mg silymarin daily",
                "50s": "140-800 mg silymarin daily",
                "60s": "140-800 mg silymarin daily",
                "70plus": "140-800 mg silymarin daily"
            },
            "contraindications": ["ragweed_allergy"],
            "interactions": ["statins", "certain_diabetes_medications", "hormone_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4310066/"]
        },
        "lions_mane": {
            "name": "Lion's Mane Mushroom",
            "benefits": "Cognitive function, nerve regeneration, mood support, immune function",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cognitive_function", "nerve_health", "mood_support", "digestive_health", "immune_support"]
            },
            "dosage": {
                "30s": "500-3000 mg daily",
                "40s": "500-3000 mg daily",
                "50s": "500-3000 mg daily",
                "60s": "500-3000 mg daily",
                "70plus": "500-3000 mg daily"
            },
            "contraindications": ["mushroom_allergies"],
            "interactions": ["blood_thinners", "immunosuppressants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6593314/"]
        },
        "berberine": {
            "name": "Berberine",
            "benefits": "Blood sugar regulation, lipid management, gut health, weight management",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["blood_sugar_management", "heart_health", "gut_health", "weight_management", "cholesterol_management"]
            },
            "dosage": {
                "30s": "500-1500 mg daily",
                "40s": "500-1500 mg daily",
                "50s": "500-1500 mg daily",
                "60s": "500-1500 mg daily",
                "70plus": "500-1500 mg daily"
            },
            "contraindications": ["pregnancy", "breastfeeding", "jaundice_in_newborns"],
            "interactions": ["diabetes_medications", "blood_thinners", "certain_antibiotics", "statins"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6111450/"]
        },
        "melatonin": {
            "name": "Melatonin",
            "benefits": "Sleep regulation, antioxidant, immune modulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["sleep_issues", "jet_lag", "shift_work", "longevity", "seasonal_depression", "immune_support"]
            },
            "dosage": {
                "20s": "0.5-3 mg before bed",
                "30s": "0.5-3 mg before bed",
                "40s": "0.5-3 mg before bed",
                "50s": "0.5-5 mg before bed",
                "60s": "0.5-5 mg before bed",
                "70plus": "0.5-5 mg before bed"
            },
            "contraindications": ["autoimmune_disorders", "seizure_disorders", "depression", "pregnancy"],
            "interactions": ["blood_thinners", "immunosuppressants", "diabetes_medications", "contraceptives", "caffeine"],
            "sources": ["https://www.nccih.nih.gov/health/melatonin-what-you-need-to-know"]
        },
        "l_theanine": {
            "name": "L-Theanine",
            "benefits": "Stress reduction, focus with calmness, sleep quality, cognitive performance",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["stress", "anxiety", "sleep_issues", "focus", "cognitive_function"]
            },
            "dosage": {
                "20s": "100-400 mg daily",
                "30s": "100-400 mg daily",
                "40s": "100-400 mg daily",
                "50s": "100-400 mg daily",
                "60s": "100-400 mg daily",
                "70plus": "100-400 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_pressure_medications", "stimulants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6836118/"]
        },
        "l_carnitine": {
            "name": "L-Carnitine",
            "benefits": "Energy production, recovery, heart health, exercise performance, brain function",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["energy_levels", "heart_health", "exercise_performance", "brain_health", "vegetarian_vegan", "weight_management"]
            },
            "dosage": {
                "30s": "500-2000 mg daily",
                "40s": "500-2000 mg daily",
                "50s": "500-2000 mg daily",
                "60s": "1000-3000 mg daily",
                "70plus": "1000-3000 mg daily"
            },
            "contraindications": ["hypothyroidism", "seizure_disorders"],
            "interactions": ["thyroid_medications", "blood_thinners", "seizure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5872767/"]
        },
        "l_glutamine": {
            "name": "L-Glutamine",
            "benefits": "Gut health, muscle recovery, immune function, wound healing",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["gut_health", "exercise_recovery", "immune_support", "wound_healing", "digestive_issues", "stress"]
            },
            "dosage": {
                "20s": "5-10 g daily",
                "30s": "5-10 g daily",
                "40s": "5-10 g daily",
                "50s": "5-10 g daily",
                "60s": "5-10 g daily",
                "70plus": "5-10 g daily"
            },
            "contraindications": ["liver_disease", "kidney_disease", "MSG_sensitivity"],
            "interactions": ["cancer_medications", "anti_seizure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5946426/"]
        },
        "creatine": {
            "name": "Creatine",
            "benefits": "Muscle strength, exercise performance, cognitive function, energy production",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["muscle_strength", "exercise_performance", "cognitive_function", "energy_levels", "vegetarian_vegan", "muscle_preservation"]
            },
            "dosage": {
                "20s": "3-5 g daily",
                "30s": "3-5 g daily",
                "40s": "3-5 g daily",
                "50s": "3-5 g daily",
                "60s": "3-5 g daily",
                "70plus": "3-5 g daily"
            },
            "contraindications": ["kidney_disease"],
            "interactions": ["nephrotoxic_medications", "diuretics", "NSAIDs"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6950288/"]
        },
        "citrulline": {
            "name": "Citrulline",
            "benefits": "Blood flow, exercise performance, blood pressure, erectile function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["exercise_performance", "blood_pressure", "erectile_function", "heart_health"]
            },
            "dosage": {
                "20s": "3-6 g daily",
                "30s": "3-6 g daily",
                "40s": "3-6 g daily",
                "50s": "3-6 g daily",
                "60s": "3-6 g daily",
                "70plus": "3-6 g daily"
            },
            "contraindications": [],
            "interactions": ["blood_pressure_medications", "ED_medications", "nitrates"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5537866/"]
        },
        "beta_alanine": {
            "name": "Beta-Alanine",
            "benefits": "Exercise endurance, muscle performance, delayed fatigue",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["exercise_performance", "muscle_endurance", "fatigue", "fitness_performance"]
            },
            "dosage": {
                "20s": "3-6 g daily",
                "30s": "3-6 g daily",
                "40s": "3-6 g daily",
                "50s": "3-6 g daily",
                "60s": "3-6 g daily",
                "70plus": "3-6 g daily"
            },
            "contraindications": [],
            "interactions": [],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6027492/"]
        },
        "collagen": {
            "name": "Collagen Peptides",
            "benefits": "Skin elasticity, joint health, bone strength, hair and nail support",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "joint_pain", "bone_health", "hair_health", "nail_health", "gut_health", "wound_healing"]
            },
            "dosage": {
                "30s": "5-10 g daily",
                "40s": "10-15 g daily",
                "50s": "10-20 g daily",
                "60s": "10-20 g daily",
                "70plus": "10-20 g daily"
            },
            "contraindications": ["alpha-gal_syndrome", "certain_food_allergies"],
            "interactions": [],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6835901/"]
        },
        "maca": {
            "name": "Maca Root",
            "benefits": "Energy, hormone balance, libido, mood, fertility",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["energy_levels", "hormone_balance", "libido", "mood_support", "fertility", "menopause_symptoms"]
            },
            "dosage": {
                "20s": "1500-3000 mg daily",
                "30s": "1500-3000 mg daily",
                "40s": "1500-3000 mg daily",
                "50s": "1500-3000 mg daily",
                "60s": "1500-3000 mg daily",
                "70plus": "1500-3000 mg daily"
            },
            "contraindications": ["hormone_sensitive_conditions", "high_blood_pressure"],
            "interactions": ["hormone_therapies", "blood_pressure_medications", "thyroid_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3614644/"]
        },
        "reishi": {
            "name": "Reishi Mushroom",
            "benefits": "Immune support, stress reduction, sleep improvement, longevity, anti-inflammatory",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "stress", "sleep_issues", "longevity", "inflammatory_conditions", "liver_health"]
            },
            "dosage": {
                "20s": "1.5-9 g dried mushroom daily",
                "30s": "1.5-9 g dried mushroom daily",
                "40s": "1.5-9 g dried mushroom daily",
                "50s": "1.5-9 g dried mushroom daily",
                "60s": "1.5-9 g dried mushroom daily",
                "70plus": "1.5-9 g dried mushroom daily"
            },
            "contraindications": ["bleeding_disorders", "scheduled_surgery", "mushroom_allergies"],
            "interactions": ["blood_thinners", "blood_pressure_medications", "immunosuppressants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6010034/"]
        },
        "fiber": {
            "name": "Fiber Supplement",
            "benefits": "Digestive health, cholesterol management, blood sugar regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["digestive_issues", "heart_health", "blood_sugar_management", "weight_management", "gut_microbiome_health", "colon_health"]
            },
            "dosage": {
                "20s": "5-10 g per serving, 25-38 g total daily",
                "30s": "5-10 g per serving, 25-38 g total daily",
                "40s": "5-10 g per serving, 25-38 g total daily",
                "50s": "5-10 g per serving, 25-38 g total daily",
                "60s": "5-10 g per serving, 25-38 g total daily",
                "70plus": "5-10 g per serving, 25-38 g total daily"
            },
            "contraindications": ["intestinal_narrowing", "difficulty_swallowing", "bowel_obstruction"],
            "interactions": ["diabetes_medications", "certain_antibiotics", "cholesterol_medications", "mineral_absorption"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3705355/"]
        },
        "5htp": {
            "name": "5-HTP",
            "benefits": "Mood support, sleep quality, appetite regulation, headache prevention",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["depression", "sleep_issues", "weight_management", "migraines", "fibromyalgia"]
            },
            "dosage": {
                "20s": "50-300 mg daily",
                "30s": "50-300 mg daily",
                "40s": "50-300 mg daily",
                "50s": "50-300 mg daily",
                "60s": "50-300 mg daily",
                "70plus": "50-300 mg daily"
            },
            "contraindications": ["taking_antidepressants", "taking_MAO_inhibitors", "down_syndrome", "pregnancy"],
            "interactions": ["antidepressants", "dextromethorphan", "tramadol", "carbidopa"],
            "sources": ["https://examine.com/supplements/5-htp/"]
        },
        "choline": {
            "name": "Choline",
            "benefits": "Brain development, liver function, metabolism, nerve function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["brain_health", "liver_health", "pregnancy_support", "cognitive_function", "memory_support", "muscle_function"]
            },
            "dosage": {
                "20s": "425-550 mg daily",
                "30s": "425-550 mg daily",
                "40s": "425-550 mg daily",
                "50s": "425-550 mg daily",
                "60s": "425-550 mg daily",
                "70plus": "425-550 mg daily"
            },
            "contraindications": ["trimethylaminuria"],
            "interactions": ["methotrexate"],
            "sources": ["https://ods.od.nih.gov/factsheets/Choline-HealthProfessional/"]
        },
        "inositol": {
            "name": "Inositol",
            "benefits": "Mental health, fertility, insulin sensitivity, PCOS management",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["anxiety", "depression", "pcos", "fertility", "insulin_resistance", "obsessive_thoughts"]
            },
            "dosage": {
                "20s": "2-18 g daily",
                "30s": "2-18 g daily",
                "40s": "2-18 g daily",
                "50s": "2-18 g daily",
                "60s": "2-18 g daily",
                "70plus": "2-18 g daily"
            },
            "contraindications": [],
            "interactions": ["diabetes_medications", "lithium"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5418896/"]
        },
        "msm": {
            "name": "MSM (Methylsulfonylmethane)",
            "benefits": "Joint health, anti-inflammatory, allergies, skin health",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["joint_pain", "inflammation", "seasonal_allergies", "skin_health", "exercise_recovery"]
            },
            "dosage": {
                "30s": "1-3 g daily",
                "40s": "1-3 g daily",
                "50s": "1-3 g daily",
                "60s": "1-3 g daily",
                "70plus": "1-3 g daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5372953/"]
        },
        "bpc_157": {
            "name": "BPC-157",
            "benefits": "Wound healing, gut health, tissue repair, joint recovery",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["gut_health", "wound_healing", "joint_pain", "exercise_recovery", "tendon_repair"]
            },
            "dosage": {
                "20s": "250-500 mcg daily",
                "30s": "250-500 mcg daily",
                "40s": "250-500 mcg daily",
                "50s": "250-500 mcg daily",
                "60s": "250-500 mcg daily",
                "70plus": "250-500 mcg daily"
            },
            "contraindications": ["cancer_concerns"],
            "interactions": ["NSAIDs", "blood_thinners"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6583303/"]
        },
        "quercetin": {
            "name": "Quercetin",
            "benefits": "Antioxidant, anti-inflammatory, allergy relief, immune support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["allergies", "inflammation", "immune_support", "heart_health", "longevity", "exercise_recovery"]
            },
            "dosage": {
                "20s": "500-1000 mg daily",
                "30s": "500-1000 mg daily",
                "40s": "500-1000 mg daily",
                "50s": "500-1000 mg daily",
                "60s": "500-1000 mg daily",
                "70plus": "500-1000 mg daily"
            },
            "contraindications": ["pregnancy", "breastfeeding"],
            "interactions": ["antibiotics", "blood_thinners", "corticosteroids", "cyclosporine"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7254783/"]
        },
        "spirulina": {
            "name": "Spirulina",
            "benefits": "Protein source, antioxidant, immune support, detoxification",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "vegetarian_vegan", "detoxification", "energy_levels", "allergy_relief", "exercise_recovery"]
            },
            "dosage": {
                "20s": "1-8 g daily",
                "30s": "1-8 g daily",
                "40s": "1-8 g daily",
                "50s": "1-8 g daily",
                "60s": "1-8 g daily",
                "70plus": "1-8 g daily"
            },
            "contraindications": ["autoimmune_disorders", "phenylketonuria", "seafood_allergies"],
            "interactions": ["immunosuppressants", "anticoagulants", "diabetes_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3136577/"]
        },
        "chlorella": {
            "name": "Chlorella",
            "benefits": "Detoxification, immune support, antioxidant, blood pressure regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["detoxification", "immune_support", "cholesterol_management", "blood_pressure", "digestive_health"]
            },
            "dosage": {
                "20s": "2-3 g daily",
                "30s": "2-3 g daily",
                "40s": "2-3 g daily",
                "50s": "2-3 g daily",
                "60s": "2-3 g daily",
                "70plus": "2-3 g daily"
            },
            "contraindications": ["iodine_sensitivity", "autoimmune_disorders"],
            "interactions": ["warfarin", "immunosuppressants", "blood_sugar_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6478772/"]
        },
        "ginseng": {
            "name": "Ginseng",
            "benefits": "Energy, cognitive function, immune support, stress adaptation",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["energy_levels", "cognitive_function", "immune_support", "stress", "sexual_health", "blood_sugar_management"]
            },
            "dosage": {
                "30s": "200-400 mg daily",
                "40s": "200-400 mg daily",
                "50s": "200-400 mg daily",
                "60s": "200-400 mg daily",
                "70plus": "200-400 mg daily"
            },
            "contraindications": ["autoimmune_disorders", "bleeding_disorders", "hormone_sensitive_conditions", "insomnia"],
            "interactions": ["diabetes_medications", "stimulants", "blood_thinners", "MAO_inhibitors", "immunosuppressants"],
            "sources": ["https://www.nccih.nih.gov/health/asian-ginseng"]
        },
        "boswellia": {
            "name": "Boswellia (Frankincense)",
            "benefits": "Anti-inflammatory, joint health, digestive health, asthma support",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["joint_pain", "inflammation", "digestive_issues", "asthma", "inflammatory_bowel_disease"]
            },
            "dosage": {
                "30s": "300-500 mg (65% boswellic acids) daily",
                "40s": "300-500 mg (65% boswellic acids) daily",
                "50s": "300-500 mg (65% boswellic acids) daily",
                "60s": "300-500 mg (65% boswellic acids) daily",
                "70plus": "300-500 mg (65% boswellic acids) daily"
            },
            "contraindications": ["pregnancy", "breastfeeding"],
            "interactions": ["anticoagulants", "antiplatelet_drugs", "certain_liver_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3309643/"]
        },
        "cinnamon": {
            "name": "Cinnamon",
            "benefits": "Blood sugar regulation, antioxidant, anti-inflammatory, antimicrobial",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["blood_sugar_management", "inflammation", "heart_health", "digestive_health", "cognitive_function"]
            },
            "dosage": {
                "20s": "1-6 g daily",
                "30s": "1-6 g daily",
                "40s": "1-6 g daily",
                "50s": "1-6 g daily",
                "60s": "1-6 g daily",
                "70plus": "1-6 g daily"
            },
            "contraindications": ["liver_disease", "scheduled_surgery"],
            "interactions": ["diabetes_medications", "blood_thinners", "liver_metabolized_drugs"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4003790/"]
        },
        "aloe_vera": {
            "name": "Aloe Vera (Internal)",
            "benefits": "Digestive health, immune support, skin health, anti-inflammatory",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["digestive_issues", "skin_health", "immune_support", "diabetes_support", "cholesterol_management"]
            },
            "dosage": {
                "20s": "100-200 mg aloe extract daily",
                "30s": "100-200 mg aloe extract daily",
                "40s": "100-200 mg aloe extract daily",
                "50s": "100-200 mg aloe extract daily",
                "60s": "100-200 mg aloe extract daily",
                "70plus": "100-200 mg aloe extract daily"
            },
            "contraindications": ["pregnancy", "breastfeeding", "kidney_disease", "electrolyte_imbalances", "scheduled_surgery"],
            "interactions": ["diabetes_medications", "diuretics", "digoxin", "sevoflurane"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6349368/"]
        },
        "ginger": {
            "name": "Ginger",
            "benefits": "Digestive health, anti-inflammatory, nausea relief, immune support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["digestive_issues", "nausea", "inflammation", "immune_support", "joint_pain", "motion_sickness"]
            },
            "dosage": {
                "20s": "500-2000 mg daily",
                "30s": "500-2000 mg daily",
                "40s": "500-2000 mg daily",
                "50s": "500-2000 mg daily",
                "60s": "500-2000 mg daily",
                "70plus": "500-2000 mg daily"
            },
            "contraindications": ["gallstones", "bleeding_disorders", "scheduled_surgery"],
            "interactions": ["blood_thinners", "diabetes_medications", "blood_pressure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7019938/"]
        },
        "phosphatidylserine": {
            "name": "Phosphatidylserine",
            "benefits": "Cognitive function, memory, stress reduction, brain health",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cognitive_function", "memory_support", "stress", "exercise_recovery", "age_related_cognitive_decline"]
            },
            "dosage": {
                "40s": "100-300 mg daily",
                "50s": "100-300 mg daily",
                "60s": "100-300 mg daily",
                "70plus": "100-300 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "cognitive_medications", "acetylcholinesterase_inhibitors"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4596514/"]
        },
        "glucosamine": {
            "name": "Glucosamine",
            "benefits": "Joint health, cartilage support, anti-inflammatory",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["joint_pain", "osteoarthritis", "sports_injuries", "aging_joints", "joint_health"]
            },
            "dosage": {
                "40s": "1500 mg daily",
                "50s": "1500 mg daily",
                "60s": "1500 mg daily",
                "70plus": "1500 mg daily"
            },
            "contraindications": ["shellfish_allergy", "glaucoma", "asthma"],
            "interactions": ["blood_thinners", "diabetes_medications", "cancer_treatments"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3150191/"]
        }
    }
    
    return supplements_datagroups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["detoxification", "immune_support", "cholesterol_management", "blood_pressure", "digestive_health"]
            },
            "dosage": {
                "20s": "2-3 g daily",
                "30s": "2-3 g daily",
                "40s": "2-3 g daily",
                "50s": "2-3 g daily",
                "60s": "2-3 g daily",
                "70plus": "2-3 g daily"
            },
            "contraindications": ["iodine_sensitivity", "autoimmune_disorders"],
            "interactions": ["warfarin", "immunosuppressants", "blood_sugar_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6478772/"]
        },
